""" Wiz Issue Integration class """

import json
import logging
import os
from datetime import timedelta, datetime
from typing import List, Dict

from regscale.core.app.application import Application
from regscale.core.app.utils.app_utils import create_progress_object, check_file_path
from regscale.core.utils.date import date_str, days_from_today
from regscale.integrations.integration.issue import IntegrationIssue
from regscale.models import (
    Issue,
    IssueSeverity,
    Link,
    IssueStatus,
    Data,
    DataDataType,
    Comment,
    regscale_models,
)
from regscale.utils.dict_utils import get_value
from regscale.utils.graphql_client import PaginatedGraphQLClient
from .constants import (
    CONTENT_TYPE,
    ISSUE_QUERY,
    DATASOURCE,
    ISSUES_FILE_PATH,
    SEVERITY_MAP,
)
from .utils import convert_first_seen_to_days
from ...variables import ScannerVariables

logger = logging.getLogger(__name__)

CLOUD_PROVIDER_URL_FIELD = "entitySnapshot.cloudProviderURL"
WIZ_ASSET_NAME = "entitySnapshot.name"
SOURCE_ID = "sourceRule.id"
WIZ_ASSET_ID = "entitySnapshot.id"


class WizIssue(IntegrationIssue):
    """
    Wiz Issue class
    """

    def __init__(
        self,
        filter_by,
        regscale_id: int,
        regscale_module: str,
        wiz_url: str,
        first: int = 100,
        wiz_projects=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        if wiz_projects is None:
            wiz_projects = []
        self.variables = {
            "first": first,
            "filterBy": filter_by,
        }
        self.regscale_id = regscale_id
        self.regscale_module = regscale_module
        self.wiz_projects = wiz_projects
        self.wiz_url = wiz_url
        app = Application()
        self.config = app.config
        self.asset_dict = {}
        self.assets: List[regscale_models.Asset] = []
        self.control_impl_controlid_dict = {}
        self.pull_limit_hours = self.config.get("wizFullPullLimitHours", 8)
        self.low_days = self.config.get("issues.wiz.high", 60)
        self.medium_days = self.config.get("issues.wiz.medium", 210)
        self.high_days = self.config.get("issues.wiz.low", 394)
        self.due_date_map = {
            regscale_models.IssueSeverity.High: date_str(days_from_today(self.low_days)),
            regscale_models.IssueSeverity.Moderate: date_str(days_from_today(self.medium_days)),
            regscale_models.IssueSeverity.Low: date_str(days_from_today(self.high_days)),
        }

    def pull(self):
        """
        Pull issues from Wiz for the given project ids
        """
        wiz_issues = self.fetch_wiz_data_if_needed()
        logger.info(f"Found {len(wiz_issues)} issues from Wiz")
        self.assets = regscale_models.Asset.get_all_by_parent(
            parent_id=self.regscale_id, parent_module=self.regscale_module
        )
        self.asset_dict = {asset.wizId: asset for asset in self.assets}
        self.control_impl_controlid_dict = regscale_models.ControlImplementation.get_control_label_map_by_plan(
            plan_id=self.regscale_id
        )
        num_processed = self.create_issues(
            wiz_issues=wiz_issues,
        )

        logger.info(f"Total issues processed: {num_processed}")

    def fetch_wiz_data_if_needed(self) -> List[Dict]:
        """
        Fetch Wiz data if needed or return cached data if still valid.
        :return: The fetched or cached Wiz data
        :rtype: List[Dict]
        """
        current_time = datetime.now()
        cache_valid = False

        if os.path.exists(ISSUES_FILE_PATH):
            file_mod_time = datetime.fromtimestamp(os.path.getmtime(ISSUES_FILE_PATH))
            cache_valid = (current_time - file_mod_time) < timedelta(hours=self.pull_limit_hours)

        if cache_valid:
            with open(ISSUES_FILE_PATH, "r", encoding="utf-8") as file:
                return json.load(file)

        nodes = self.fetch_wiz_data(
            query=ISSUE_QUERY,
            variables=self.variables,
            api_endpoint_url=self.wiz_url,
            topic_key="issues",
        )

        check_file_path("artifacts")
        with open(ISSUES_FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(nodes, file)

        return nodes

    @staticmethod
    def fetch_wiz_data(query: str, variables: Dict, api_endpoint_url: str, topic_key: str) -> List[Dict]:
        """
        Fetch Wiz data for the given query and variables
        :param str query: The query to fetch data
        :param Dict variables: The variables for the query
        :param str api_endpoint_url: The Wiz API endpoint URL
        :param str topic_key: The key for the topic in the response data
        :raises ValueError: If the Wiz access token is missing
        :return: The fetched data
        :rtype: List[Dict]
        """
        logger.debug("Sending a paginated request to Wiz API")
        app = Application()
        api_endpoint_url = app.config["wizUrl"] if api_endpoint_url is None else api_endpoint_url

        if token := app.config.get("wizAccessToken"):
            client = PaginatedGraphQLClient(
                endpoint=api_endpoint_url,
                query=query,
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Authorization": "Bearer " + token,
                },
            )

            # Fetch all results using the client's pagination logic
            data = client.fetch_all(variables=variables, topic_key=topic_key)

            return data
        raise ValueError("Your Wiz access token is missing.")

    def create_issues(self, wiz_issues: List[Dict]) -> int:
        """
        Map Wiz issues to RegScale issues
        :param List[Dict] wiz_issues: List of Wiz issues
        :return int: The number of issues created
        :rtype: int
        """
        user_id = ScannerVariables.userId
        create_progress = create_progress_object()
        total_items = len(wiz_issues)
        create_job = create_progress.add_task("[#f68d1f]Mapping RegScale issues...", total=total_items)
        processed_issues = 0
        with create_progress:
            for wiz_issue in wiz_issues:
                self.create_or_update_issue(
                    wiz_issue=wiz_issue,
                    user_id=user_id,
                    parent_id=self.regscale_id,
                    parent_module=self.regscale_module,
                    identifier=f"<p>{get_value(wiz_issue, WIZ_ASSET_NAME)}</p>",
                )
                processed_issues += 1
                create_progress.advance(create_job, advance=1)

            Issue.bulk_save(progress_context=create_progress)
            Comment.bulk_save(progress_context=create_progress)
            Data.bulk_save(progress_context=create_progress)
            Link.bulk_save(progress_context=create_progress)
        return processed_issues

    def determine_is_poam_from_days_since_last_seen_and_severity(
        self, days_since_last_seen: int, severity: str
    ) -> bool:
        """
        Determines if the issue is a POAM from the days since last seen
        :param int days_since_last_seen: Days since last seen
        :param str severity: Severity of the issue
        :returns: True if the issue is a POAM, False otherwise
        :rtype: bool
        """
        if severity.lower().__contains__("low"):
            return days_since_last_seen > self.low_days
        elif severity.lower().__contains__("moderate"):
            return days_since_last_seen > self.medium_days
        elif severity.lower().__contains__("high") or severity.lower().__contains__("critical"):
            return days_since_last_seen > self.high_days
        return False

    def set_is_poam_and_due_date_on_issue(self, issue: Issue):
        """
        Set the isPoam and dueDate on the issue
        :param Issue issue: Issue object
        """
        days_open = convert_first_seen_to_days(issue.dateFirstDetected)
        due_date: str = self.due_date_map.get(issue.severityLevel, date_str(days_from_today(days_open)))
        days_since_first_seen = convert_first_seen_to_days(issue.dateFirstDetected)
        is_poam = self.determine_is_poam_from_days_since_last_seen_and_severity(
            days_since_first_seen, issue.severityLevel
        )
        issue.isPoam = is_poam
        issue.dueDate = due_date

    def create_or_update_additional_data(self, wiz_issue: dict, issue: Issue):
        """
        Prepare additional data for a Wiz issue before creating or updating the RegScale issue.
        :param Dict wiz_issue: Wiz issue dictionary
        :param Issue issue: Issue object
        :return Dict: Additional data
        :rtype Dict: Dict
        """
        user_id = ScannerVariables.userId
        for note in get_value(wiz_issue, "notes"):
            comment = Comment(
                parentID=issue.id,
                parentModule="issues",
                comment=f"{note.get('email')}: {note.get('text')}" if note.get("email") else note.get("text"),
                commentDate=note.get("createdAt"),
                createdById=user_id,
                lastUpdatedById=user_id,
            )
            comment.create_or_update(bulk_create=True, bulk_update=True)
        if url := get_value(wiz_issue, CLOUD_PROVIDER_URL_FIELD):
            link = Link(
                parentID=issue.id,
                parentModule=Issue.get_module_string(),
                url=url,
                title=f"Wiz Entity: {get_value(wiz_issue, WIZ_ASSET_NAME)}",
                createdById=user_id,
                lastUpdatedById=user_id,
            )
            link.create_or_update(bulk_create=True, bulk_update=True)
        data = Data(
            parentId=issue.id,
            parentModule=Issue.get_module_string(),
            dataSource=DATASOURCE,
            dataType=DataDataType.JSON.value,
            rawData=json.dumps(wiz_issue),
            createdById=user_id,
            lastUpdatedById=user_id,
        )
        data.create_or_update(bulk_create=True, bulk_update=True)

    def get_control_impl_id_from_control_id_string(self, control_id_string: str) -> int:
        """
        Get the control ID from the control ID string
        :param str control_id_string: The control ID string
        :return: The control implementation ID
        :rtype: int
        """
        return self.control_impl_controlid_dict.get(control_id_string.lower())

    def create_or_update_issue(
        self, wiz_issue: Dict, user_id: str, parent_id: int, parent_module: str, identifier: str
    ):
        """
        Create or update a RegScale issue from a Wiz issue
        :param Dict wiz_issue: Wiz issue dictionary
        :param str user_id: User ID to assign the issue to
        :param int parent_id: The regscale model to which the issue is attached
        :param str parent_module: The regscale model to which the issue is attached
        :param str identifier: Asset identifiers
        """
        wiz_id = get_value(wiz_issue, WIZ_ASSET_ID)
        asset = self.asset_dict.get(wiz_id)
        subcategories = get_value(wiz_issue, "sourceRule.securitySubCategories") or []

        control_ids = [
            self.get_control_impl_id_from_control_id_string(subcat.get("externalId", "").lower())
            for subcat in subcategories
        ]
        control_ids = control_ids or [self.get_control_impl_id_from_control_id_string("CM-6(5)")]

        for control_id in control_ids:
            new_issue = Issue(
                title=get_value(wiz_issue, "sourceRule.name")
                or f"unknown - {wiz_issue.get('id')} - type: {wiz_issue.get('type')} - entity_id: {wiz_id}",
                description=get_value(wiz_issue, "sourceRule.cloudConfigurationRuleDescription"),
                dateCreated=get_value(wiz_issue, "createdAt"),
                dateLastUpdated=get_value(wiz_issue, "updatedAt"),
                status=self.map_status(get_value(wiz_issue, "status")),
                severityLevel=self.map_severity_level(wiz_issue),
                recommendedActions=get_value(wiz_issue, "sourceRule.remediationInstructions"),
                assetIdentifier=identifier,
                dueDate=self.process_issue_due_date(get_value(wiz_issue, "severity")),
                issueOwnerId=user_id,
                createdById=user_id,
                dateFirstDetected=get_value(wiz_issue, "createdAt"),
                lastUpdatedById=user_id,
                parentId=asset.id if asset else parent_id,
                securityPlanId=self.regscale_id,
                parentModule=asset.get_module_slug() if asset else parent_module,
                dateCompleted=(
                    get_value(wiz_issue, "resolvedAt")
                    if get_value(wiz_issue, "resolvedAt") and self.map_status(get_value(wiz_issue, "status")) != "Open"
                    else None
                ),
                identification="Wiz",
                sourceReport="Wiz",
                wizId=wiz_id,
                securityChecks=get_value(wiz_issue, SOURCE_ID),
                pluginId=get_value(wiz_issue, SOURCE_ID),
                otherIdentifier=get_value(wiz_issue, "entitySnapshot.externalId"),
                controlId=control_id,
            )
            new_issue.create_or_update(bulk_update=True)

            self.set_is_poam_and_due_date_on_issue(new_issue)
            self.create_or_update_additional_data(wiz_issue, new_issue)

    @staticmethod
    def map_status(status: str) -> str:
        """
        Map Wiz status to RegScale status
        :param str status: Wiz status
        :return str: RegScale status
        """
        status_map = {
            "OPEN": IssueStatus.Open.value,
            "RESOLVED": IssueStatus.Closed.value,
            "IN_PROGRESS": IssueStatus.Open.value,
            "REJECTED": IssueStatus.Cancelled.value,
        }
        return status_map.get(status, IssueStatus.Open.value)

    @staticmethod
    def process_issue_due_date(severity_level: str) -> str:
        """
        Process issue due date
        :param str severity_level: Severity level
        :return: Due date string
        """
        app = Application()
        config = app.config

        # Get days from config, default to 0 if not found or invalid
        days = config.get("issues", {}).get("wiz", {}).get(severity_level.lower(), 0)
        try:
            days = int(days)
        except (ValueError, TypeError):
            days = 0

        return date_str(days_from_today(days))

    @staticmethod
    def map_severity_level(wiz_issue: Dict) -> str:
        """
        Map Wiz severity level to RegScale severity level
        :param Dict wiz_issue: Wiz issue dictionary containing the severity level
        :return str: RegScale severity level
        """
        severity = get_value(wiz_issue, "severity") or "NotAssigned"
        return SEVERITY_MAP.get(severity, IssueSeverity.Low.value)
