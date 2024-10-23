"""
Qualys Scan information
"""

import concurrent

# pylint: disable=C0415
import re
from typing import Any, Optional, TypeVar

from regscale.core.app import create_logger
from regscale.core.app.application import Application
from regscale.core.app.utils.app_utils import convert_datetime_to_regscale_string, get_current_datetime
from regscale.models import Issue
from regscale.models.integration_models.flat_file_importer import FlatFileImporter
from regscale.models.regscale_models import Asset, Vulnerability

T = TypeVar("T")
QG_HOST_ID = "QG Host ID"
CVE_ID = "CVE ID"


class Qualys(FlatFileImporter):
    """Qualys Scan information"""

    title = "Qualys Scanner Export Integration"
    asset_identifier_field = "name"

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.vuln_title = "Title"
        self.fmt = "%Y-%m-%d"
        self.dt_format = "%Y-%m-%d %H:%M:%S"
        self.headers = [
            "IP",
            "DNS",
            "NetBIOS",
            QG_HOST_ID,
            "IP Interfaces",
            "Tracking Method",
            "OS",
            "IP Status",
            "QID",
            "Title",
            "Vuln Status",
            "Type",
            "Severity",
            "Port",
            "Protocol",
            "FQDN",
            "SSL",
            "First Detected",
            "Last Detected",
            "Times Detected",
            "Date Last Fixed",
            "First Reopened",
            "Last Reopened",
            "Times Reopened",
            CVE_ID,
            "Vendor Reference",
            "Bugtraq ID",
            "CVSS3.1",
            "CVSS3.1 Base",
            "CVSS3.1 Temporal",
            "Threat",
            "Impact",
            "Solution",
            "Exploitability",
            "Associated Malware",
            "Results",
            "PCI Vuln",
            "Ticket State",
            "Instance",
            "Category",
            "Associated Tags",
            "EC2 Instance ID",
            "Public Hostname",
            "Image ID",
            "VPC ID",
            "Instance State",
            "Private Hostname",
            "Instance Type",
            "Account ID",
            "Region Code",
            "Subnet ID",
            "QDS",
            "ARS",
            "ACS",
            "TruRisk Score",
        ]
        logger = create_logger()
        super().__init__(
            logger=logger,
            app=Application(),
            headers=self.headers,
            header_line_number=129,
            asset_func=self.create_asset,
            vuln_func=self.create_vuln,
            **kwargs,
        )
        # header is line# 11
        # start self.file_data from line #12

    def create_issue(self, dat: Optional[dict] = None) -> Optional[Issue]:
        """
        Create an issue from a row in the Qualys file

        :param Optional[dict] dat: Data row from CSV file
        :return: RegScale Issue object or None
        :rtype: Optional[Issue]
        """
        from regscale.integrations.commercial.qualys import map_qualys_severity_to_regscale

        severity = dat["Severity"]
        regscale_severity = map_qualys_severity_to_regscale(int(severity))[1]
        status = "Open" if regscale_severity in ["moderate", "high", "critical"] else "Closed"
        name = dat["Title"]
        description = dat["Exploitability"]
        cve = dat[CVE_ID]
        solution = dat["Solution"]
        # create an issue
        if self.attributes.app.config["issues"][self.name.lower()]["useKev"]:
            kev_due_date = self.lookup_kev(cve)
        iss = Issue(
            isPoam=severity in ["low", "moderate", "high", "critical"],
            title=f"CVE: {cve} Associated with asset {name}",
            description=description,
            identification="Other",
            status=status,
            severityLevel=regscale_severity,
            issueOwnerId=self.attributes.app.config["userId"],
            pluginId=cve,
            assetIdentifier=name,
            securityPlanId=(self.attributes.parent_id if self.attributes.parent_module == "securityplans" else None),
            recommendedActions=(solution if solution else "Upgrade affected package"),
            cve=cve,
            dateCompleted=convert_datetime_to_regscale_string(self.scan_date) if status == "Closed" else None,
            autoApproved="No",
            parentId=self.attributes.parent_id,
            parentModule=self.attributes.parent_module,
            extra_data={"link": description} if description else {},
            originalRiskRating=Issue.assign_risk_rating(severity),
            dateFirstDetected=convert_datetime_to_regscale_string(self.scan_date),
            basisForAdjustment=f"{self.name} import",
            # Set issue due date to the kev date if it is in the kev list
        )
        iss = self.update_due_dt(iss=iss, kev_due_date=kev_due_date, scanner="ecr", severity=severity)
        return iss

    def create_asset(self, dat: Optional[dict] = None) -> Optional[Asset]:
        """
        Create an asset from a row in the Qualys file

        :param Optional[dict] dat: Data row from CSV file
        :return: RegScale Issue object or None
        :rtype: Optional[Asset]
        """
        return Asset(
            **{
                "id": 0,
                "name": dat["DNS"],
                "ipAddress": dat["IP"],
                "isPublic": True,
                "status": "Active (On Network)",
                "assetCategory": "Hardware",
                "qualysId": dat[QG_HOST_ID],  # UUID from Nessus HostProperties tag
                "bLatestScan": True,
                "bAuthenticatedScan": True,
                "scanningTool": "Qualys",
                "assetOwnerId": self.attributes.app.config["userId"],
                "netBIOS": dat["NetBIOS"],
                "assetType": "Other",
                "fqdn": dat["FQDN"],
                "operatingSystem": Asset.find_os(dat["OS"]),
                "operatingSystemVersion": dat["OS"],
                "systemAdministratorId": self.attributes.app.config["userId"],
                "parentId": self.attributes.parent_id,
                "parentModule": self.attributes.parent_module,
            }
        )

    def create_vuln(self, dat: Optional[dict] = None, **kwargs: dict) -> None:
        """
        Create a vuln from a row in the Qualys file

        :param Optional[dict] dat: Data row from CSV file, defaults to None
        :param dict **kwargs: Additional keyword arguments
        :rtype: None
        """
        from regscale.integrations.commercial.qualys import map_qualys_severity_to_regscale

        dns: str = dat.get("DNS")
        other_id: str = dat.get(QG_HOST_ID)
        distro: str = dat.get("OS")
        cve: str = dat.get(CVE_ID)
        description: str = dat.get("Threat")
        title = dat.get(self.vuln_title)
        regscale_vuln = None
        severity = dat.get("Severity")
        regscale_severity = map_qualys_severity_to_regscale(int(severity))[1]
        config = self.attributes.app.config
        asset_match = [asset for asset in self.data["assets"] if asset.name == dns]
        asset = asset_match[0] if asset_match else None
        if dat and asset_match:
            regscale_vuln = Vulnerability(
                id=0,
                scanId=0,  # set later
                parentId=asset.id,
                parentModule="assets",
                ipAddress=dat.get("IP"),
                lastSeen=dat.get("Last Detected"),
                firstSeen=dat.get("First Detected"),
                daysOpen=None,
                dns=dat.get("DNS", other_id),
                mitigated=None,
                operatingSystem=(Asset.find_os(distro) if Asset.find_os(distro) else None),
                severity=regscale_severity,
                plugInName=dat.get(self.vuln_title),
                plugInId=dat.get("QID"),
                cve=cve,
                vprScore=None,
                cvsSv3BaseScore=self.extract_float(dat.get("CVSS3.1 Base", 0.0)),
                tenantsId=0,
                title=title,
                description=description,
                plugInText=title,
                createdById=config["userId"],
                lastUpdatedById=config["userId"],
                dateCreated=get_current_datetime(),
            )
        return regscale_vuln

    @staticmethod
    def determine_cvss_severity(dat: dict) -> str:
        """
        Determine the CVSS severity of the vulnerability

        :param dict dat: Data row from CSV file
        :return: A severity derived from the CVSS scores
        :rtype: str
        """
        precedence_order = [
            "NVD CVSS v3 Severity",
            "NVD CVSS v2 Severity",
            "Vendor CVSS v3 Severity",
            "Vendor CVSS v2 Severity",
        ]
        severity = "info"
        for key in precedence_order:
            if dat.get(key):
                severity = dat[key].lower()
                break
        # remap crits to highs
        if severity == "critical":
            severity = "high"
        return severity

    def extract_float(self, s: str) -> Any:
        """
        Extract a float from a string

        :param str s: String to extract float from
        :return: Float extracted from string or None
        :rtype: Any
        """
        matches = re.findall(r"[-+]?[0-9]*\.?[0-9]+", s)
        if matches:
            return float(matches[0])
        else:
            return None
