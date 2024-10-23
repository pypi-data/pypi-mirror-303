"""
IBM Scan information
"""

from typing import Optional
from urllib.parse import urlparse

from regscale.core.app.application import Application
from regscale.core.app.logz import create_logger
from regscale.core.app.utils.app_utils import epoch_to_datetime, get_current_datetime, is_valid_fqdn
from regscale.models.integration_models.flat_file_importer import FlatFileImporter
from regscale.models.regscale_models import Asset, Vulnerability

ISSUE_TYPE = "Issue Type"
VULNERABILITY_TITLE = ISSUE_TYPE
VULNERABILITY_ID = ISSUE_TYPE


class AppScan(FlatFileImporter):
    """
    IBM Scan information
    """

    severity_map = {
        "Critical": "critical",
        "High": "high",
        "Medium": "medium",
        "Low": "low",
        "Informational": "low",
    }

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        regscale_ssp_id = kwargs.get("plan_id")
        self.vuln_title = VULNERABILITY_TITLE
        self.vuln_id = VULNERABILITY_ID
        logger = create_logger()
        headers = ["Status", "Severity", ISSUE_TYPE, "URL", "Tested Element", "Entity Type"]
        super().__init__(
            logger=logger,
            app=Application(),
            headers=headers,
            parent_id=regscale_ssp_id,
            parent_module="securityplans",
            asset_func=self.create_asset,
            vuln_func=self.create_vuln,
            extra_headers_allowed=True,
            **kwargs,
        )

    def create_asset(self, dat: Optional[dict] = None) -> Asset:
        """
        Create an asset from a row in the IBM csv file

        :param Optional[dict] dat: Data row from CSV file, defaults to None
        :return: RegScale Asset object
        :rtype: Asset
        """
        parsed_url = urlparse(dat.get("URL"))
        hostname: str = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return Asset(
            **{
                "id": 0,
                "name": hostname,
                "isPublic": True,
                "status": "Active (On Network)",
                "assetCategory": "Software",
                "bLatestScan": True,
                "bAuthenticatedScan": True,
                "scanningTool": self.name,
                "assetOwnerId": self.config["userId"],
                "assetType": "Other",
                "fqdn": hostname if is_valid_fqdn(hostname) else None,
                "systemAdministratorId": self.config["userId"],
                "parentId": self.attributes.parent_id,
                "parentModule": self.attributes.parent_module,
            }
        )

    def create_vuln(self, dat: Optional[dict] = None, **kwargs: dict) -> Optional[Vulnerability]:
        """
        Create a vulnerability from a row in the IBM csv file

        :param Optional[dict] dat: Data row from CSV file, defaults to None
        :param dict **kwargs: Additional keyword arguments
        :return: RegScale Vulnerability object or None
        :rtype: Optional[Vulnerability]
        """
        regscale_vuln = None
        parsed_url = urlparse(dat.get("URL"))
        hostname: str = f"{parsed_url.scheme}://{parsed_url.netloc}"
        description: str = dat.get(ISSUE_TYPE)
        app_scan_severity = dat.get("Severity")
        severity = self.severity_map.get(app_scan_severity, "Informational")
        config = self.attributes.app.config
        asset_match = [asset for asset in self.data["assets"] if asset.name == hostname]
        asset = asset_match[0] if asset_match else None
        if dat and asset_match:
            regscale_vuln = Vulnerability(
                id=0,
                scanId=0,  # set later
                parentId=asset.id,
                parentModule="assets",
                ipAddress="0.0.0.0",  # No ip address available
                lastSeen=get_current_datetime(),
                firstSeen=epoch_to_datetime(self.create_epoch),
                daysOpen=None,
                dns=hostname,
                mitigated=None,
                severity=severity,
                plugInName=description,
                cve="",
                vprScore=None,
                tenantsId=0,
                title=description[:255],
                description=description,
                plugInText=description,
                createdById=config["userId"],
                lastUpdatedById=config["userId"],
                dateCreated=get_current_datetime(),
            )
        return regscale_vuln
