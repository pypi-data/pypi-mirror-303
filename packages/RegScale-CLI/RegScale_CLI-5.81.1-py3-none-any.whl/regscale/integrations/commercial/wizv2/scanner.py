"""Module for Wiz vulnerability scanning integration."""

import datetime
import json
import logging
import os
import re
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union

from regscale.core.app.utils.app_utils import check_file_path, get_current_datetime
from regscale.core.utils import get_base_protocol_from_port
from regscale.integrations.commercial.wiz import (
    INVENTORY_FILE_PATH,
    INVENTORY_QUERY,
    create_asset_type,
    get_notes_from_wiz_props,
    handle_management_type,
    map_category,
    wiz_authenticate,
)
from regscale.integrations.commercial.wiz.vulnerabilities import VulnerabilitiesIntegration, WizVulnerabilityType
from regscale.integrations.commercial.wizv2.constants import VULNERABILITY_QUERY
from regscale.integrations.commercial.wizv2.parsers import (
    collect_components_to_create,
    fetch_wiz_data,
    get_disk_storage,
    get_ip_address_from_props,
    get_latest_version,
    get_network_info,
    get_product_ids,
    get_software_name_from_cpe,
    handle_os_version,
    handle_provider,
    handle_software_version,
    pull_resource_info_from_props,
)
from regscale.integrations.commercial.wizv2.variables import WizVariables
from regscale.integrations.scanner_integration import IntegrationAsset, IntegrationFinding, ScannerIntegration
from regscale.integrations.variables import ScannerVariables
from regscale.models import regscale_models

logger = logging.getLogger("rich")
# logger.setLevel(logging.DEBUG)


class WizVulnerabilityIntegration(ScannerIntegration):
    """Integration class for Wiz vulnerability scanning."""

    title = "Wiz"
    asset_identifier_field = "wizId"
    finding_severity_map = {
        "Critical": regscale_models.IssueSeverity.High,
        "High": regscale_models.IssueSeverity.High,
        "Medium": regscale_models.IssueSeverity.Moderate,
        "Low": regscale_models.IssueSeverity.Low,
    }
    asset_lookup = "vulnerableAsset"
    wiz_token = None

    def get_variables(self):
        return {
            "first": 100,
            "filterBy": {},
        }

    def authenticate(self, client_id: Optional[str] = None, client_secret: Optional[str] = None) -> None:
        """
        Authenticates to Wiz using the client ID and client secret

        :param Optional[str] client_id: Wiz client ID
        :param Optional[str] client_secret: WiZ client secret
        :rtype: None
        """
        client_id = client_id or WizVariables.wizClientId
        client_secret = client_secret or WizVariables.wizClientSecret
        logger.info("Authenticating to Wiz...")
        self.wiz_token = wiz_authenticate(client_id, client_secret)

    def fetch_findings(self, *args: Tuple, **kwargs: dict) -> List[IntegrationFinding]:
        """
        Fetches Wiz findings using the GraphQL API

        :param Tuple *args: Tuple of arguments
        :param dict **kwargs: Keyword arguments
        :return: List of IntegrationFinding objects
        :rtype: List[IntegrationFinding]
        """
        self.authenticate(kwargs.get("client_id"), kwargs.get("client_secret"))
        project_id = kwargs.get("wiz_project_id")
        logger.info("Fetching Wiz findings...")
        vulnerabilities_integration = VulnerabilitiesIntegration(
            wiz_project_id=project_id,
            parent_id=self.plan_id,
            scan_tool="Wiz",
            parent_module=regscale_models.SecurityPlan.get_module_slug(),
        )

        findings = []
        for wiz_vulnerability_type in vulnerabilities_integration.wiz_vulnerability_types:
            logger.info("Fetching Wiz findings for %s...", wiz_vulnerability_type["type"])
            variables = self.get_variables()
            variables["filterBy"]["projectId"] = [project_id]

            nodes = self.fetch_wiz_data_if_needed(
                query=VULNERABILITY_QUERY,
                variables=variables,
                topic_key=wiz_vulnerability_type["topic_key"],
                file_path=wiz_vulnerability_type["file_path"],
            )
            for node in nodes:
                finding = self.parse_finding(node, wiz_vulnerability_type["type"])
                if finding:
                    findings.append(finding)

        logger.info("Fetched %d Wiz findings.", len(findings))
        return findings

    def parse_finding(
        self, node: Dict[str, Any], vulnerability_type: WizVulnerabilityType
    ) -> Optional[IntegrationFinding]:
        """
        Parses a Wiz finding node into an IntegrationFinding object

        :param Dict[str, Any] node: The Wiz finding node to parse
        :param WizVulnerabilityType vulnerability_type: The type of vulnerability
        :return: The parsed IntegrationFinding or None if parsing fails
        :rtype: Optional[IntegrationFinding]
        """
        try:
            asset_id = node.get(self.asset_lookup, {}).get("id")
            if not asset_id:
                return None

            severity = self.finding_severity_map.get(
                node.get("severity", "Low").capitalize(), regscale_models.IssueSeverity.Low
            )
            status = self.map_status_to_issue_status(node.get("status", "Open"))
            name: str = node.get("name")
            cve = (
                name
                if name and (name.startswith("CVE") or name.startswith("GHSA")) and not node.get("cve")
                else node.get("cve")
            )
            #  get_value(node, "vulnerableAsset.name")
            return IntegrationFinding(
                control_labels=[],  # Add an empty list for control_labels
                category="Wiz Vulnerability",  # Add a default category
                title=node.get("name", "Unknown vulnerability"),
                description=node.get("description", ""),
                severity=severity,
                status=status,
                asset_identifier=asset_id,
                external_id=f"{node.get('sourceRule', {'id': cve}).get('id')}",
                first_seen=node.get("firstDetectedAt") or node.get("firstSeenAt") or get_current_datetime(),
                last_seen=node.get("lastDetectedAt") or node.get("analyzedAt") or get_current_datetime(),
                remediation=node.get("description", ""),
                cvss_score=node.get("score"),
                cve=cve,
                plugin_name=cve,
                cvs_sv3_base_score=node.get("score"),
                source_rule_id=node.get("sourceRule", {}).get("id"),
                vulnerability_type=vulnerability_type.value,
            )
        except (KeyError, TypeError, ValueError) as e:
            logger.error("Error parsing Wiz finding: %s", str(e), exc_info=True)
            return None

    @staticmethod
    def map_status_to_issue_status(status: str) -> str:
        """
        Maps the Wiz status to issue status
        :param str status: Status of the vulnerability
        :returns: Issue status
        :rtype: str
        """
        if status.lower() == "open":
            return "Open"
        elif status.lower() in ["resolved", "rejected"]:
            return "Closed"
        return "Open"

    def fetch_assets(self, *args: Any, **kwargs: Any) -> Iterator[IntegrationAsset]:
        """
        Fetches Wiz assets using the GraphQL API

        :yields: Iterator[IntegrationAsset]
        """
        self.authenticate(kwargs.get("client_id"), kwargs.get("client_secret"))
        wiz_project_id = kwargs.get("wiz_project_id")
        logger.info("Fetching Wiz assets...")
        filter_by_override = kwargs.get("filter_by_override") or WizVariables.wizInventoryFilterBy
        if filter_by_override:
            filter_by = json.loads(filter_by_override) if isinstance(filter_by_override, str) else filter_by_override
        else:
            filter_by = {
                "project": wiz_project_id,  # Use the first project ID as a string
            }
            if WizVariables.wizLastInventoryPull and not WizVariables.wizFullPullLimitHours:
                filter_by["updatedAt"] = {"after": WizVariables.wizLastInventoryPull}

        variables = self.get_variables()
        variables["filterBy"].update(filter_by)

        nodes = self.fetch_wiz_data_if_needed(
            query=INVENTORY_QUERY, variables=variables, topic_key="cloudResources", file_path=INVENTORY_FILE_PATH
        )
        logger.info("Fetched %d Wiz assets.", len(nodes))
        self.num_assets_to_process = len(nodes)

        for node in nodes:
            asset = self.parse_asset(node)
            if asset:
                yield asset

    def parse_asset(self, node: Dict[str, Any]) -> Optional[IntegrationAsset]:
        """
        Parses Wiz assets

        :param Dict[str, Any] node: The Wiz asset to parse
        :return: The parsed IntegrationAsset
        :rtype: Optional[IntegrationAsset]
        """
        name = node.get("name")
        wiz_entity = node.get("graphEntity", {})
        if not wiz_entity:
            logger.info(node)
            logger.warning("No graph entity found for asset %s", name)
            return None
        wiz_entity_properties = wiz_entity.get("properties", {})
        network_dict = get_network_info(wiz_entity_properties)
        handle_provider_dict = handle_provider(wiz_entity_properties)
        software_name_dict = get_software_name_from_cpe(wiz_entity_properties, name)
        software_list = self.create_name_version_dict(wiz_entity_properties.get("installedPackages", []))
        # Ports
        start_port = wiz_entity_properties.get("portStart")
        ports_and_protocols = []
        if start_port:
            end_port = wiz_entity_properties.get("portEnd") or start_port
            protocol = wiz_entity_properties.get("protocols", wiz_entity_properties.get("protocol"))
            if protocol in ["other", None]:
                protocol = get_base_protocol_from_port(start_port)
            ports_and_protocols = [{"start_port": start_port, "end_port": end_port, "protocol": protocol}]
        return IntegrationAsset(
            name=name,
            external_id=node.get("name"),
            asset_tag_number=node.get("subscriptionExternalId"),
            other_tracking_number=node.get("subscriptionExternalId"),
            identifier=node.get("id"),
            asset_type=create_asset_type(node.get("type")),
            asset_owner_id=ScannerVariables.userId,
            parent_id=self.plan_id,
            parent_module=regscale_models.SecurityPlan.get_module_slug(),
            asset_category=map_category(node.get("type")),
            date_last_updated=wiz_entity.get("lastSeen", ""),
            management_type=handle_management_type(wiz_entity_properties),
            status=self.map_wiz_status(wiz_entity_properties.get("status")),
            ip_address=get_ip_address_from_props(wiz_entity_properties),
            software_vendor=(
                software_name_dict.get("software_vendor") or wiz_entity_properties.get("cloudPlatform")
                if map_category(node.get("type")) == "Software"
                else None
            ),
            software_version=(
                handle_software_version(wiz_entity_properties, map_category(node.get("type"))) or "1.0"
                if map_category(node.get("type")) == "Software"
                else None
            ),
            software_name=(
                software_name_dict.get("software_name") or wiz_entity_properties.get("nativeType")
                if map_category(node.get("type")) == "Software"
                else None
            ),
            location=wiz_entity_properties.get("region"),
            notes=get_notes_from_wiz_props(wiz_entity_properties, node.get("id")),
            model=wiz_entity_properties.get("nativeType"),
            serial_number=get_product_ids(wiz_entity_properties),
            is_public_facing=wiz_entity_properties.get("directlyInternetFacing", False),
            azure_identifier=handle_provider_dict.get("azureIdentifier"),
            mac_address=wiz_entity_properties.get("macAddress"),
            fqdn=wiz_entity_properties.get("dnsName") or network_dict.get("dns"),
            disk_storage=get_disk_storage(wiz_entity_properties) or 0,
            cpu=pull_resource_info_from_props(wiz_entity_properties)[1] or 0,
            ram=pull_resource_info_from_props(wiz_entity_properties)[0] or 0,
            operating_system=wiz_entity_properties.get("operatingSystem"),
            os_version=handle_os_version(wiz_entity_properties, map_category(node.get("type"))),
            end_of_life_date=wiz_entity_properties.get("versionEndOfLifeDate"),
            vlan_id=wiz_entity_properties.get("zone"),
            uri=network_dict.get("url"),
            aws_identifier=handle_provider_dict.get("awsIdentifier"),
            google_identifier=handle_provider_dict.get("googleIdentifier"),
            other_cloud_identifier=handle_provider_dict.get("otherCloudIdentifier"),
            patch_level=get_latest_version(wiz_entity_properties),
            cpe=wiz_entity_properties.get("cpe"),
            component_names=collect_components_to_create([node], []),
            source_data=node,
            url=wiz_entity_properties.get("cloudProviderURL"),
            ports_and_protocols=ports_and_protocols,
            software_inventory=software_list,
        )

    @staticmethod
    def create_name_version_dict(package_list: List[str]) -> List[Dict[str, str]]:
        """
        Creates a dictionary of package names and their versions from a list of strings in the format "name (version)".

        :param List[str] package_list: A list of strings containing package names and versions.
        :return Dict[str, str]: A dictionary with package names as keys and versions as values.
        """
        software_inventory = []

        for package in package_list:
            # Use regex to extract the name and version
            match = re.match(r"(.+?) \((.+?)\)", package)
            if match:
                name, version = match.groups()
                software_inventory.append({"name": name, "version": version})

        return software_inventory

    @staticmethod
    def map_wiz_status(wiz_status: Union[str, None]) -> str:
        """
        Map Wiz status to RegScale status
        """
        return "Active (On Network)" if wiz_status != "Inactive" else "Off-Network"

    def fetch_wiz_data_if_needed(self, query: str, variables: Dict, topic_key: str, file_path: str) -> List[Dict]:
        """
        Fetch Wiz data if needed and save to file if not already fetched within the last 8 hours and return the data

        :param str query: GraphQL query string
        :param Dict variables: Query variables
        :param str topic_key: The key for the data in the response
        :param str file_path: Path to save the fetched data
        :return: List of nodes as dictionaries
        :rtype: List[Dict]
        """
        fetch_interval = datetime.timedelta(hours=WizVariables.wizFullPullLimitHours or 8)  # Interval to fetch new data
        current_time = datetime.datetime.now()
        check_file_path(os.path.dirname(file_path))

        # Check if the file exists and its last modified time
        if os.path.exists(file_path):
            file_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if current_time - file_mod_time < fetch_interval:
                logger.info("File %s is newer than %s hours. Using cached data...", file_path, fetch_interval)
                with open(file_path, "r", encoding="utf-8") as file:
                    nodes = json.load(file)
                return nodes
            else:
                logger.info("File %s is older than %s hours. Fetching new data...", file_path, fetch_interval)
        else:
            logger.info("File %s does not exist. Fetching new data...", file_path)

        nodes = fetch_wiz_data(
            query=query,
            variables=variables,
            api_endpoint_url=WizVariables.wizUrl,
            token=self.wiz_token,
            topic_key=topic_key,
        )
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(nodes, file)

        return nodes
