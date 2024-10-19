"""
Aqua Scan information
"""

import logging
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from itertools import groupby
from operator import attrgetter, itemgetter
from typing import Any, List, Optional

from dateutil.parser import ParserError, parse

from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.core.app.utils.app_utils import get_current_datetime, is_valid_fqdn
from regscale.core.utils.date import datetime_str
from regscale.models.app_models.mapping import Mapping
from regscale.models.integration_models.flat_file_importer import FlatFileImporter
from regscale.models.regscale_models.asset import Asset
from regscale.models.regscale_models.vulnerability import Vulnerability


class Aqua(FlatFileImporter):
    """Aqua Scan information"""

    def __init__(self, **kwargs: dict):
        self.name = kwargs.get("name")
        regscale_ssp_id = kwargs.get("regscale_ssp_id")
        self.vuln_title = "Vulnerability Name"
        self.fmt = "%m/%d/%Y"
        self.dt_format = "%Y-%m-%d %H:%M:%S"
        self.image_name = "Image Name"
        self.ffi = "First Found on Image"
        self.last_image_scan = "Last Image Scan"
        self.installed_version = "Installed Version"
        self.vendor_cvss_v2_severity = "Vendor CVSS v2 Severity"
        self.vendor_cvss_v3_severity = "Vendor CVSS v3 Severity"
        self.vendor_cvss_v3_score = "Vendor CVSS v3 Score"
        self.nvd_cvss_v2_severity = "NVD CVSS v2 Severity"
        self.nvd_cvss_v3_severity = "NVD CVSS v3 Severity"
        self.headers = [
            "Registry",
            self.image_name,
            "Image Build Date",
            "Image Digest",
            "OS",
            "Resource",
            "Resource Type",
            self.installed_version,
            self.vuln_title,
            "Publish Date",
            "Referenced By",
            self.vendor_cvss_v2_severity,
            "Vendor CVSS v2 Score",
            "Vendor CVSS v2 Vectors",
            self.vendor_cvss_v3_severity,
            self.vendor_cvss_v3_score,
            "Vendor CVSS v3 Vectors",
            "Vendor URL",
            self.nvd_cvss_v2_severity,
            "NVD CVSS v2 Score",
            "NVD CVSS v2 Vectors",
            self.nvd_cvss_v3_severity,
            "NVD CVSS v3 Score",
            "NVD CVSS v3 Vectors",
            "NVD URL",
            "Fix Version",
            "Solution",
            "Qualys IDs",
            "Description",
            "Applied By",
            "Applied On",
            "Reverted By",
            "Reverted On",
            "Enforced By",
            "Enforced On",
            "vShield Status",
            "Suppression Date",
            "Base Image Vulnerability",
            "Base Image Name",
            "Aqua score",
            "Aqua severity",
            "Aqua Vectors",
            "Aqua custom severity",
            "Aqua custom notes",
            self.ffi,
            self.last_image_scan,
            "Exploit Availability",
            "Temporal Vector",
            "Exploit Type",
            "Namespace",
            "Resource Path",
        ]
        logger = create_logger()
        self.logger = logger
        kwargs, mapping = self.update_mapping(kwargs)
        self.mapping = mapping
        super().__init__(
            logger=logger,
            headers=mapping.to_header(),
            parent_id=regscale_ssp_id,
            parent_module="securityplans",
            asset_func=self.create_asset,
            vuln_func=self.create_vuln,
            app=Application(),
            ignore_validation=True,
            **kwargs,
        )

    def create_asset(self, dat: Optional[dict] = None) -> Optional[Asset]:
        """
        Create an asset from a row in the Aqua file

        :param Optional[dict] dat: Data row from CSV file, defaults to None
        :return: RegScale Asset object or None
        :rtype: Optional[Asset]
        """
        name = dat[self.image_name]
        if not name:
            return None
        return Asset(
            **{
                "id": 0,
                "name": name,
                "description": "",
                "operatingSystem": Asset.find_os(dat["OS"]),
                "operatingSystemVersion": dat["OS"],
                "ipAddress": "0.0.0.0",
                "isPublic": True,
                "status": "Active (On Network)",
                "assetCategory": "Hardware",
                "bLatestScan": True,
                "bAuthenticatedScan": True,
                "scanningTool": self.name,
                "assetOwnerId": self.config["userId"],
                "assetType": "Other",
                "fqdn": name if is_valid_fqdn(name) else None,
                "systemAdministratorId": self.config["userId"],
                "parentId": self.attributes.parent_id,
                "parentModule": self.attributes.parent_module,
                "extra_data": {"software_inventory": self.generate_software_inventory(name)},
            }
        )

    def generate_software_inventory(self, name: str) -> List[dict]:
        """
        Create and post a list of software inventory for a given asset

        :param str name: The name of the asset
        :return: List of software inventory
        :rtype: List[dict]
        """
        inventory: List[dict] = []

        image_group = {k: list(g) for k, g in groupby(self.file_data, key=itemgetter("Image Name"))}

        softwares = image_group[name]
        for software in softwares:
            inv = {
                "name": software["Resource"],
                "version": str(software[self.installed_version]),
            }
            if (inv.get("name"), inv.get("version")) not in {
                (soft.get("name"), soft.get("version")) for soft in inventory
            }:
                inventory.append(inv)

        return inventory

    def current_datetime_w_log(self, field: str) -> str:
        """
        Get the current date and time with a log message

        :param str field: The field that is missing the date
        :return: The current date and time
        :rtype: str
        """
        self.logger.info(f"Unable to determine date for the %s field, falling back to current date and time: {field}")
        return get_current_datetime()

    def create_vuln(self, dat: Optional[dict] = None, **kwargs: dict) -> Optional[Vulnerability]:
        """
        Create a vulnerability from a row in the Aqua csv file

        :param Optional[dict] dat: Data row from CSV file, defaults to None
        :param dict **kwargs: Additional keyword arguments
        :return: RegScale Vulnerability object or None
        :rtype: Optional[Vulnerability]
        """

        regscale_vuln = None
        severity = self.determine_cvss_severity(dat)
        hostname = dat[self.image_name]
        description = dat["Description"]
        solution = dat["Solution"] if dat.get("Solution") else "Upgrade affected package"
        config = self.attributes.app.config
        asset_match = [asset for asset in self.data["assets"] if asset.name == hostname]
        asset = asset_match[0] if asset_match else None
        if asset_match and self.validate(ix=kwargs.get("index"), dat=dat):
            regscale_vuln = Vulnerability(
                id=0,
                scanId=0,
                parentId=asset.id,
                parentModule="assets",
                ipAddress="0.0.0.0",
                lastSeen=datetime_str(dat.get(self.last_image_scan))
                or self.current_datetime_w_log(self.last_image_scan),
                firstSeen=datetime_str(dat.get(self.ffi)) or self.current_datetime_w_log(self.ffi),
                daysOpen=None,
                dns=hostname,
                mitigated=None,
                operatingSystem=asset.operatingSystem,
                severity=severity,
                plugInName=description,
                cve=dat[self.vuln_title],
                cvsSv3BaseScore=dat[self.vendor_cvss_v3_score],
                tenantsId=0,
                title=description[:255],
                description=description,
                plugInText=dat[self.vuln_title],
                createdById=config["userId"],
                lastUpdatedById=config["userId"],
                dateCreated=get_current_datetime(),
                extra_data={"solution": solution},
            )
        return regscale_vuln

    def determine_cvss_severity(self, dat: dict) -> str:
        """
        Determine the CVSS severity of the vulnerability

        :param dict dat: Data row from CSV file
        :return: A severity derived from the CVSS scores
        :rtype: str
        """
        precedence_order = [
            self.nvd_cvss_v3_severity,
            self.nvd_cvss_v2_severity,
            self.vendor_cvss_v3_severity,
            # This field may or may not be available in the file (Coalfire has it, BMC does not.)
            self.vendor_cvss_v2_severity if dat.get(self.vendor_cvss_v2_severity) else None,
        ]
        severity = "info"
        for key in precedence_order:
            if key and dat.get(key):
                severity = dat[key].lower()
                break
        # remap crits to highs
        if severity == "critical":
            severity = "high"
        return severity

    def default_mapping(self) -> Mapping:
        """
        Default mapping for the Nexpose csv file if one is not provided
        """
        headers = [
            "Registry",
            self.image_name,
            "Image Build Date",
            "Image Digest",
            "OS",
            "Resource",
            "Resource Type",
            self.installed_version,
            self.vuln_title,
            "Publish Date",
            "Referenced By",
            self.vendor_cvss_v2_severity,
            "Vendor CVSS v2 Score",
            "Vendor CVSS v2 Vectors",
            self.vendor_cvss_v3_severity,
            self.vendor_cvss_v3_score,
            "Vendor CVSS v3 Vectors",
            "Vendor URL",
            self.nvd_cvss_v2_severity,
            "NVD CVSS v2 Score",
            "NVD CVSS v2 Vectors",
            self.nvd_cvss_v3_severity,
            "NVD CVSS v3 Score",
            "NVD CVSS v3 Vectors",
            "NVD URL",
            "Fix Version",
            "Solution",
            "Qualys IDs",
            "Description",
            "Applied By",
            "Applied On",
            "Reverted By",
            "Reverted On",
            "Enforced By",
            "Enforced On",
            "vShield Status",
            "Suppression Date",
            "Base Image Vulnerability",
            "Base Image Name",
            "Aqua score",
            "Aqua severity",
            "Aqua Vectors",
            "Aqua custom severity",
            "Aqua custom notes",
            self.ffi,
            self.last_image_scan,
            "Exploit Availability",
            "Temporal Vector",
            "Exploit Type",
            "Namespace",
            "Resource Path",
        ]
        expected = [
            self.image_name,
            "OS",
            self.last_image_scan,
            self.ffi,
            self.vuln_title,
            self.vendor_cvss_v3_score,
            "Description",
            "Solution",
            self.nvd_cvss_v3_severity,
            self.nvd_cvss_v2_severity,
            self.vendor_cvss_v3_severity,
        ]
        mapping_dict = {"mapping": {header: header for header in headers}, "expected_field_names": expected}
        return Mapping(**mapping_dict)

    def validate(self, ix: Optional[int], dat: dict) -> bool:
        """
        Validate the row of data, if it is missing any required fields, return False

        :param Optional[int] ix: index
        :param dict dat: Data row from CSV file
        :return: True if the row is valid, False otherwise
        :rtype: bool
        """
        required_or_break = ["Description"]
        val = True
        for key in required_or_break:
            if not dat.get(key):
                val = False
                row_skip = f"skipping row #{ix + 1}" if isinstance(ix, int) else "skipping row.."
                self.attributes.logger.warning(f"Missing value for required field: {key}, {row_skip}")
                break
        return val
