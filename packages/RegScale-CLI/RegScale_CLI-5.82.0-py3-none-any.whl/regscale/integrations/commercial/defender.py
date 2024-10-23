#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" RegScale Microsoft Defender recommendations and alerts integration"""

# standard python imports
from datetime import datetime, timedelta
from json import JSONDecodeError
from os import PathLike
from pathlib import Path
from typing import Literal, Optional, Tuple, Union

import click
import requests
from rich.console import Console

from regscale.core.app.api import Api
from regscale.core.app.application import Application
from regscale.core.app.internal.login import is_valid
from regscale.core.app.logz import create_logger
from regscale.core.app.utils.app_utils import (
    check_license,
    create_progress_object,
    error_and_exit,
    flatten_dict,
    get_current_datetime,
    reformat_str_date,
    uncamel_case,
)
from regscale.models import regscale_id, regscale_module
from regscale.models.integration_models.defender import Defender
from regscale.models.integration_models.defender_data import DefenderData
from regscale.models.integration_models.flat_file_importer import FlatFileImporter
from regscale.models.regscale_models.issue import Issue
from regscale.validation.record import validate_regscale_object

LOGIN_ERROR = "Login Invalid RegScale Credentials, please login for a new token."
console = Console()
job_progress = create_progress_object()
logger = create_logger()
unique_recs = []
new_issues = []
closed = []
updated = []
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
IDENTIFICATION_TYPE = "Vulnerability Assessment"


######################################################################################################
#
# Adding application to Microsoft Defender API:
#   https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exposed-apis-create-app-webapp
# Microsoft Defender 365 APIs Docs:
#   https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exposed-apis-list?view=o365-worldwide
# Microsoft Defender for Cloud API Docs:
#   https://learn.microsoft.com/en-us/rest/api/defenderforcloud/
#
######################################################################################################


@click.group()
def defender():
    """Create RegScale issues for each Microsoft Defender 365 Recommendation"""


@defender.command(name="authenticate")
@click.option(
    "--system",
    type=click.Choice(["cloud", "365"], case_sensitive=False),
    help="Pull recommendations from Microsoft Defender 365 or Microsoft Defender for Cloud.",
    prompt="Please choose a system",
    required=True,
)
def authenticate_in_defender(system: str):
    """Obtains an access token using the credentials provided in init.yaml."""
    authenticate(system=system)


@defender.command(name="sync_365_alerts")
@regscale_id(required=False, default=None, prompt=False)
@regscale_module(required=False, default=None, prompt=False)
def sync_365_alerts(regscale_id: Optional[int] = None, regscale_module: Optional[str] = None):
    """
    Get Microsoft Defender 365 alerts and create RegScale
    issues with the information from Microsoft Defender 365.
    """
    sync_defender_and_regscale(
        regscale_id=regscale_id, regscale_module=regscale_module, system="365", defender_object="alerts"
    )


@defender.command(name="sync_365_recommendations")
@regscale_id(required=False, default=None, prompt=False)
@regscale_module(required=False, default=None, prompt=False)
def sync_365_recommendations(regscale_id: Optional[int] = None, regscale_module: Optional[str] = None):
    """
    Get Microsoft Defender 365 recommendations and create RegScale
    issues with the information from Microsoft Defender 365.
    """
    sync_defender_and_regscale(
        regscale_id=regscale_id, regscale_module=regscale_module, system="365", defender_object="recommendations"
    )


@defender.command(name="sync_cloud_alerts")
@regscale_id(required=False, default=None, prompt=False)
@regscale_module(required=False, default=None, prompt=False)
def sync_cloud_alerts(regscale_id: Optional[int] = None, regscale_module: Optional[str] = None):
    """
    Get Microsoft Defender for Cloud alerts and create RegScale
    issues with the information from Microsoft Defender for Cloud.
    """
    sync_defender_and_regscale(
        regscale_id=regscale_id, regscale_module=regscale_module, system="cloud", defender_object="alerts"
    )


@defender.command(name="import_alerts")
@FlatFileImporter.common_scanner_options(
    message="File path to the folder containing Defender .csv files to process to RegScale.",
    prompt="File path to Defender files",
)
def import_alerts(folder_path: PathLike[str], regscale_ssp_id: int, scan_date: datetime):
    """
    Import Microsoft Defender alerts from a CSV file
    """
    app = Application()
    if not validate_regscale_object(regscale_ssp_id, "securityplans"):
        app.logger.warning("SSP #%i is not a valid RegScale Security Plan.", regscale_ssp_id)
        return
    if not scan_date or not FlatFileImporter.check_date_format(scan_date):
        scan_date = datetime.now()
    if len(list(Path(folder_path).glob("*.csv"))) == 0:
        app.logger.warning("No Defender(csv) files found in the specified folder.")
        return
    for file in Path(folder_path).glob("*.csv"):
        Defender(
            name="Defender",
            file_path=file,
            parent_id=regscale_ssp_id,
            parent_module="securityplans",
            scan_date=scan_date,
        )


def authenticate(system: str) -> None:
    """
    Obtains an access token using the credentials provided in init.yaml

    :param str system:
    :rtype: None
    """
    app = check_license()
    api = Api()
    if system == "365":
        url = "https://api.securitycenter.microsoft.com/api/alerts"
    elif system == "cloud":
        url = (
            f'https://management.azure.com/subscriptions/{app.config["azureCloudSubscriptionId"]}/'
            + "providers/Microsoft.Security/alerts?api-version=2022-01-01"
        )
    else:
        error_and_exit("Please enter 365 or cloud for the system.")
    check_token(api=api, system=system, url=url)


def sync_defender_and_regscale(
    regscale_id: Optional[int] = None,
    regscale_module: Optional[str] = None,
    system: Literal["365", "cloud"] = "365",
    defender_object: Literal["alerts", "recommendations"] = "recommendations",
) -> None:
    """
    Sync Microsoft Defender data with RegScale

    :param Optional[int] regscale_id: The RegScale ID to sync the alerts to, defaults to None
    :param Optional[str] regscale_module: The RegScale module to sync the alerts to, defaults to None
    :param Literal["365", "cloud"] system: The system to sync the alerts from, defaults to "365"
    :param Literal["alerts", "recommendations"] defender_object: The type of data to sync, defaults to "recommendations"
    :rtype: None
    """
    app = check_license()
    api = Api()
    # check if RegScale token is valid:
    if not is_valid(app=app):
        error_and_exit(LOGIN_ERROR)

    url_mapping = {
        "365_alerts": "https://api.securitycenter.microsoft.com/api/alerts?$top=10000",
        "365_recommendations": "https://api.securitycenter.microsoft.com/api/recommendations?$top=10000",
        "cloud_alerts": f'https://management.azure.com/subscriptions/{app.config["azureCloudSubscriptionId"]}/'
        + "providers/Microsoft.Security/alerts?api-version=2022-01-01",
    }
    url = url_mapping[f"{system}_{defender_object}"]
    defender_key = "id" if system == "365" else "name"
    mapping_func = {
        "365_alerts": map_365_alert_to_issue,
        "365_recommendations": map_365_recommendation_to_issue,
        "cloud_alerts": map_cloud_alert_to_issue,
    }

    # check the azure token, get a new one if needed
    token = check_token(api=api, system=system, url=url)

    # set headers for the data
    headers = {"Content-Type": "application/json", "Authorization": token}

    if defender_objects := get_items_from_azure(
        api=api,
        headers=headers,
        url=url,
    ):
        defender_data = [
            DefenderData(id=data[defender_key], data=data, system=system, object=defender_object)
            for data in defender_objects
        ]
        integration_field = defender_data[0].integration_field
        logger.info(f"Found {len(defender_data)} Microsoft Defender {system} {defender_object[:-1]}(s).")
    else:
        defender_data = []
        integration_field = DefenderData.get_integration_field(system=system, object=defender_object)
        logger.info(f"No Microsoft Defender {system} {defender_object} found.")

    # get all issues from RegScale where the defenderId field is populated
    # if regscale_id and regscale_module aren't provided
    if not regscale_id and not regscale_module:
        app.logger.warning(
            f"No ID or module provided, retrieving all issues with {integration_field} populated in RegScale..."
        )
        issues = Issue.get_all_by_integration_field(field=integration_field)
    else:
        app.logger.info(f"Retrieving issues from RegScale for {regscale_module} #{regscale_id}...")
        issues = Issue.get_all_by_parent(parent_id=regscale_id, parent_module=regscale_module)
        # sort the issues that have the integration field populated
        issues = [issue for issue in issues if getattr(issue, integration_field, None)]
    logger.info(f"Retrieved {len(issues)} issue(s) from RegScale.")

    regscale_issues = [
        DefenderData(
            id=getattr(issue, integration_field, ""), data=issue.model_dump(), system=system, object=defender_object
        )
        for issue in issues
    ]
    # create progress bars for each threaded task
    with job_progress:
        # see if there are any issues with defender id populated
        if regscale_issues:
            logger.info(f"{len(regscale_issues)} RegScale issue(s) will be analyzed.")
            # create progress bar and analyze the RegScale issues
            analyze_regscale_issues = job_progress.add_task(
                f"[#f8b737]Analyzing {len(regscale_issues)} RegScale issue(s)...", total=len(regscale_issues)
            )
            # evaluate open issues in RegScale
            app.thread_manager.submit_tasks_from_list(
                evaluate_open_issues,
                regscale_issues,
                (
                    api,
                    defender_data,
                    analyze_regscale_issues,
                ),
            )
            _ = app.thread_manager.execute_and_verify()
        else:
            logger.info("No issues from RegScale need to be analyzed.")
        # compare defender 365 recommendations and RegScale issues
        # while removing duplicates, updating existing RegScale Issues,
        # and adding new unique recommendations to unique_recs global variable
        if defender_data:
            logger.info(
                f"Comparing {len(defender_data)} Microsoft Defender {system} {defender_object[:-1]}(s) "
                f"and {len(regscale_issues)} RegScale issue(s).",
            )
            compare_task = job_progress.add_task(
                f"[#ef5d23]Comparing {len(defender_data)} Microsoft Defender {system} {defender_object[:-1]}(s) and "
                + f"{len(regscale_issues)} RegScale issue(s)...",
                total=len(defender_data),
            )
            app.thread_manager.submit_tasks_from_list(
                compare_defender_and_regscale,
                defender_data,
                (
                    api,
                    regscale_issues,
                    defender_key,
                    compare_task,
                ),
            )
            _ = app.thread_manager.execute_and_verify()
        # start threads and progress bar for # of issues that need to be created
        if len(unique_recs) > 0:
            logger.warning("Creating %s issue(s) in RegScale.", len(unique_recs))
            create_issues = job_progress.add_task(
                f"[#21a5bb]Creating {len(unique_recs)} issue(s) in RegScale...",
                total=len(unique_recs),
            )
            app.thread_manager.submit_tasks_from_list(
                create_issue_from_denfeder_data,
                unique_recs,
                (
                    mapping_func[f"{system}_{defender_object}"],
                    api.config,
                    defender_key,
                    regscale_id,
                    regscale_module,
                    create_issues,
                ),
            )
            _ = app.thread_manager.execute_and_verify()
            logger.info(
                "%s/%s issue(s) created in RegScale.",
                len(unique_recs),
                len(new_issues),
            )
    # check if issues needed to be created, updated or closed and print the appropriate message
    if (len(unique_recs) + len(updated) + len(closed)) == 0:
        logger.info("[green]No changes required for existing RegScale issue(s)!")
    else:
        logger.info(
            f"{len(new_issues)} issue(s) created, {len(updated)} issue(s)"
            + f" updated and {len(closed)} issue(s) were closed in RegScale."
        )


def check_token(api: Api, system: str, url: str) -> str:
    """
    Function to check if current Azure token from init.yaml is valid, if not replace it

    :param Api api: API object
    :param str system: Which system to check JWT for, either Defender 365 or Defender for Cloud
    :param str url: The URL to use for authentication
    :return: returns JWT for Microsoft 365 Defender or Microsoft Defender for Cloud depending on system provided
    :rtype: str
    """
    # set up variables for the provided system
    if system == "cloud":
        key = "azureCloudAccessToken"
        params = {"api-version": "2022-01-01"}
    elif system.lower() == "365":
        key = "azure365AccessToken"
        params = None
    else:
        error_and_exit(
            f"{system.title()} is not supported, only Microsoft 365 Defender and Microsoft Defender for Cloud."
        )
    current_token = api.config[key]
    # check the token if it isn't blank
    if current_token is not None:
        # set the headers
        header = {"Content-Type": "application/json", "Authorization": current_token}
        # test current token by getting recommendations
        token_pass = api.get(url=url, headers=header, params=params).status_code
        # check the status code
        if token_pass == 200:
            # token still valid, return it
            token = api.config[key]
            logger.info(
                "Current token for %s is still valid and will be used for future requests.",
                system.title(),
            )
        elif token_pass in [403]:
            # token doesn't have permissions, notify user and exit
            error_and_exit("Incorrect permissions set for application. Cannot retrieve recommendations.")
        else:
            # token is no longer valid, get a new one
            token = get_token(api=api, system=system)
    # token is empty, get a new token
    else:
        token = get_token(api=api, system=system)
    return token


def get_token(api: Api, system: str) -> str:
    """
    Function to get a token from Microsoft Azure and saves it to init.yaml

    :param Api api: API object
    :param str system: Which platform to authenticate for Microsoft Defender, cloud or 365
    :return: JWT from Azure
    :rtype: str
    """
    # set the url and body for request
    if system.lower() == "365":
        url = f'https://login.windows.net/{api.config["azure365TenantId"]}/oauth2/token'
        client_id = api.config["azure365ClientId"]
        client_secret = api.config["azure365Secret"]
        resource = "https://api.securitycenter.windows.com"
        key = "azure365AccessToken"
    elif system.lower() == "cloud":
        url = f'https://login.microsoftonline.com/{api.config["azureCloudTenantId"]}/oauth2/token'
        client_id = api.config["azureCloudClientId"]
        client_secret = api.config["azureCloudSecret"]
        resource = "https://management.azure.com"
        key = "azureCloudAccessToken"
    else:
        error_and_exit(
            f"{system.title()} is not supported, only Microsoft 365 Defender and Microsoft Defender for Cloud."
        )
    data = {
        "resource": resource,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    # get the data
    response = api.post(
        url=url,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
    )
    try:
        return parse_and_save_token(response, api, key, system)
    except KeyError as ex:
        # notify user we weren't able to get a token and exit
        error_and_exit(f"Didn't receive token from Azure.\n{ex}\n{response.text}")
    except JSONDecodeError as ex:
        # notify user we weren't able to get a token and exit
        error_and_exit(f"Unable to authenticate with Azure.\n{ex}\n{response.text}")


def parse_and_save_token(response: requests.Response, api: Api, key: str, system: str) -> str:
    """
    Function to parse the token from the response and save it to init.yaml

    :param requests.Response response: Response from API call
    :param Api api: API object
    :param str key: Key to use for init.yaml token update
    :param str system: Which system to check JWT for, either Defender 365 or Defender for Cloud
    :return: JWT from Azure for the provided system
    :rtype: str
    """
    # try to read the response and parse the token
    res = response.json()
    token = res["access_token"]

    # add the token to init.yaml
    api.config[key] = f"Bearer {token}"

    # write the changes back to file
    api.app.save_config(api.config)

    # notify the user we were successful
    logger.info(f"Azure {system.title()} Login Successful! Init.yaml file was updated with the new access token.")
    # return the token string
    return api.config[key]


def get_items_from_azure(api: Api, headers: dict, url: str) -> list:
    """
    Function to get data from Microsoft Defender returns the data as a list while handling pagination

    :param Api api: API object
    :param dict headers: Headers used for API call
    :param str url: URL to use for the API call
    :return: list of recommendations
    :rtype: list
    """
    # get the data via api call
    response = api.get(url=url, headers=headers)
    try:
        response_data = response.json()
        # try to get the values from the api response
        defender_data = response_data["value"]
    except JSONDecodeError:
        # notify user if there was a json decode error from API response and exit
        error_and_exit("JSON Decode error")
    except KeyError:
        # notify user there was no data from API response and exit
        error_and_exit(
            f"Received unexpected response from Microsoft Defender.\n{response.status_code}: {response.text}"
        )
    # check if pagination is required to fetch all data from Microsoft Defender
    next_link = response_data.get("nextLink")
    if response.status_code == 200 and next_link:
        # get the rest of the data
        defender_data.extend(get_items_from_azure(api=api, headers=headers, url=next_link))
    # return the defender recommendations
    return defender_data


def get_due_date(score: Union[str, int], config: dict, key: str) -> str:
    """
    Function to return due date based on the severity score of
    the Microsoft Defender recommendation; the values are in the init.yaml
    and if not, use the industry standards

    :param Union[str, int] score: Severity score from Microsoft Defender
    :param dict config: Application config
    :param str key: The key to use for init.yaml
    :return: Due date for the issue
    :rtype: str
    """
    # check severity score and assign it to the appropriate due date
    # using the init.yaml specified days
    today = datetime.now().strftime("%m/%d/%y")

    # check if the score is a string, if so convert it to an int & determine due date
    if isinstance(score, str):
        if score.lower() == "low":
            score = 3
        elif score.lower() == "medium":
            score = 5
        elif score.lower() == "high":
            score = 9
        else:
            score = 0
    if score >= 7:
        days = config["issues"][key]["high"]
    elif 4 <= score < 7:
        days = config["issues"][key]["moderate"]
    else:
        days = config["issues"][key]["low"]
    due_date = datetime.strptime(today, "%m/%d/%y") + timedelta(days=days)
    return due_date.strftime(DATE_FORMAT)


def format_description(defender_data: dict, tenant_id: str) -> str:
    """
    Function to format the provided dictionary into an HTML table

    :param dict defender_data: Microsoft Defender data as a dictionary
    :param str tenant_id: The Microsoft Defender tenant ID
    :return: HTML table as a string
    :rtype: str
    """
    url = get_defender_url(defender_data, tenant_id)
    defender_data = flatten_dict(data=defender_data)
    payload = create_payload(defender_data)
    description = create_html_table(payload, url)
    return description


def get_defender_url(rec: dict, tenant_id: str) -> str:
    """
    Function to get the URL for the Microsoft Defender data

    :param dict rec: Microsoft Defender data as a dictionary
    :param str tenant_id: The Microsoft Defender tenant ID
    :return: URL as a string
    :rtype: str
    """
    try:
        url = rec["properties"]["alertUri"]
    except KeyError:
        url = f"https://security.microsoft.com/security-recommendations?tid={tenant_id}"
    return f'<a href="{url}">{url}</a>'


def create_payload(rec: dict) -> dict:
    """
    Function to create a payload for the Microsoft Defender data

    :param dict rec: Microsoft Defender data as a dictionary
    :return: Payload as a dictionary
    :rtype: dict
    """
    payload = {}
    skip_keys = ["associatedthreats", "alerturi", "investigation steps"]
    for key, value in rec.items():
        key = key.replace("propertiesExtendedProperties", "").replace("properties", "")
        if isinstance(value, list) and len(value) > 0 and key.lower() not in skip_keys:
            payload[uncamel_case(key)] = process_list_value(value)
        elif key.lower() not in skip_keys and "entities" not in key.lower():
            if not isinstance(value, list):
                payload[uncamel_case(key)] = value
    return payload


def process_list_value(value: list) -> str:
    """
    Function to process the list value for the Microsoft Defender data

    :param list value: List of values
    :return: Processed list value as a string
    :rtype: str
    """
    if isinstance(value[0], dict):
        return "".join(f"</br>{k}: {v}" for item in value for k, v in item.items())
    elif isinstance(value[0], list):
        return "".join("</br>".join(item) for item in value)
    else:
        return "</br>".join(value)


def create_html_table(payload: dict, url: str) -> str:
    """
    Function to create an HTML table for the Microsoft Defender data

    :param dict payload: Payload for the Microsoft Defender data
    :param str url: URL for the Microsoft Defender data
    :return: HTML table as a string
    :rtype: str
    """
    description = '<table style="border: 1px solid;">'
    for key, value in payload.items():
        if value:
            if "time" in key.lower():
                value = reformat_str_date(value, dt_format="%b %d, %Y")
            description += (
                f'<tr><td style="border: 1px solid;"><b>{key}</b></td>'
                f'<td style="border: 1px solid;">{value}</td></tr>'
            )
    description += (
        '<tr><td style="border: 1px solid;"><b>View in Defender</b></td>'
        f'<td style="border: 1px solid;">{url}</td></tr>'
    )
    description += "</table>"
    return description


def compare_defender_and_regscale(def_data: DefenderData, args: Tuple) -> None:
    """
    Function to check for duplicates between issues in RegScale
    and recommendations/alerts from Microsoft Defender while using threads

    :param DefenderData def_data: Microsoft Defender data
    :param Tuple args: Tuple of args to use during the process
    :rtype: None
    """
    # set local variables with the args that were passed
    api, issues, defender_key, task = args

    # see if recommendation has been analyzed already
    if not def_data.analyzed:
        # change analyzed flag
        def_data.analyzed = True

        # set duplication flag to false
        dupe_check = False

        # iterate through the RegScale issues with defenderId populated
        for issue in issues:
            # check if the RegScale key == Windows Defender ID
            if issue.data.get(issue.integration_field) == def_data.data[defender_key]:
                # change the duplication flag to True
                dupe_check = True
                # check if the RegScale issue is closed or cancelled
                if issue.data["status"].lower() in ["closed", "cancelled"]:
                    # reopen RegScale issue because Microsoft Defender has
                    # recommended it again
                    change_issue_status(
                        api=api,
                        status=api.config["issues"][issue.init_key]["status"],
                        issue=issue.data,
                        rec=def_data,
                        rec_type=issue.init_key,
                    )
        # check if the recommendation is a duplicate
        if dupe_check is False:
            # append unique recommendation to global unique_reqs
            unique_recs.append(def_data)
    job_progress.update(task, advance=1)


def evaluate_open_issues(issue: DefenderData, args: Tuple) -> None:
    """
    function to check for Open RegScale issues against Microsoft
    Defender recommendations and will close the issues that are
    no longer recommended by Microsoft Defender while using threads

    :param DefenderData issue: Microsoft Defender data
    :param Tuple args: Tuple of args to use during the process
    :rtype: None
    """
    # set up local variables from the passed args
    api, defender_data, task = args

    defender_data_dict = {defender_data.id: defender_data for defender_data in defender_data if defender_data.id}

    # check if the issue has already been analyzed
    if not issue.analyzed:
        # set analyzed to true
        issue.analyzed = True

        # check if the RegScale defenderId was recommended by Microsoft Defender
        if issue.data.get(issue.integration_field) not in defender_data_dict and issue.data["status"] not in [
            "Closed",
            "Cancelled",
        ]:
            # the RegScale issue is no longer being recommended and the issue
            # status is not closed or cancelled, we need to close the issue
            change_issue_status(
                api=api,
                status="Closed",
                issue=issue.data,
                rec=defender_data_dict.get(issue.data.get(issue.integration_field)),
                rec_type=issue.init_key,
            )
    job_progress.update(task, advance=1)


def change_issue_status(
    api: Api,
    status: str,
    issue: dict,
    rec: Optional[DefenderData] = None,
    rec_type: str = None,
) -> None:
    """
    Function to change a RegScale issue to the provided status

    :param Api api: API object
    :param str status: Status to change the provided issue to
    :param dict issue: RegScale issue
    :param dict rec: Microsoft Defender recommendation, defaults to None
    :param str rec_type: The platform of Microsoft Defender (cloud or 365), defaults to None
    :rtype: None
    """
    # update issue last updated time, set user to current user and change status
    # to the status that was passed
    issue["lastUpdatedById"] = api.config["userId"]
    issue["dateLastUpdated"] = get_current_datetime(DATE_FORMAT)
    issue["status"] = status

    if not rec:
        return
    rec = rec.data

    # check if rec dictionary was passed, if not create it
    if rec_type == "defender365":
        issue["title"] = rec["recommendationName"]
        issue["description"] = format_description(defender_data=rec, tenant_id=api.config["azure365TenantId"])
        issue["severityLevel"] = Issue.assign_severity(rec["severityScore"])
        issue["issueOwnerId"] = api.config["userId"]
        issue["dueDate"] = get_due_date(score=rec["severityScore"], config=api.config, key="defender365")
    elif rec_type == "defenderCloud":
        issue["title"] = (f'{rec["properties"]["productName"]} Alert - {rec["properties"]["compromisedEntity"]}',)
        issue["description"] = format_description(defender_data=rec, tenant_id=api.config["azureCloudTenantId"])
        issue["severityLevel"] = (Issue.assign_severity(rec["properties"]["severity"]),)
        issue["issueOwnerId"] = api.config["userId"]
        issue["dueDate"] = get_due_date(
            score=rec["properties"]["severity"],
            config=api.config,
            key="defenderCloud",
        )

    # if we are closing the issue, update the date completed
    if status.lower() == "closed":
        if rec_type == "defender365":
            message = "via Microsoft 365 Defender"
        elif rec_type == "defenderCloud":
            message = "via Microsoft Defender for Cloud"
        else:
            message = "via Microsoft Defender"
        issue["dateCompleted"] = get_current_datetime(DATE_FORMAT)
        issue["description"] += f'<p>No longer reported {message} as of {get_current_datetime("%b %d,%Y")}</p>'
        closed.append(issue)
    else:
        issue["dateCompleted"] = ""
        updated.append(issue)

    # use the api to change the status of the given issue
    Issue(**issue).save()


def create_issue_from_denfeder_data(def_data: DefenderData, args: Tuple) -> None:
    """
    Function to utilize threading and create an issues in RegScale for the assigned thread

    :param DefenderData def_data: Microsoft Defender data to create an issue for
    :param Tuple args: Tuple of args to use during the process
    :rtype: None
    """
    # set up local variables from args passed
    mapping_func, config, defender_key, parent_id, parent_module, task = args

    # set the recommendation for the thread for later use in the function
    description = format_description(defender_data=def_data.data, tenant_id=config["azure365TenantId"])

    # check if the recommendation was already created as a RegScale issue
    if not def_data.created:
        # set created flag to true
        def_data.created = True

        # set up the data payload for RegScale API
        issue = mapping_func(data=def_data, config=config, description=description)
        issue.__setattr__(def_data.integration_field, def_data.data[defender_key])
        if parent_id and parent_module:
            issue.parentId = parent_id
            issue.parentModule = parent_module
        # create issue in RegScale via api
        if new_issue := issue.create():
            # add new issue to global list of new_issues
            new_issues.append(new_issue)
    job_progress.update(task, advance=1)


def map_365_alert_to_issue(data: DefenderData, config: dict, description: str) -> Issue:
    """
    Function to map a Microsoft 365 Defender alert to a RegScale issue

    :param DefenderData data: Microsoft Defender recommendation
    :param dict config: Application config
    :param str description: Description of the alert
    :return: RegScale issue
    :rtype: Issue
    """
    return Issue(
        title=f'{data.data["title"]}',
        dateCreated=get_current_datetime(DATE_FORMAT),
        description=description,
        severityLevel=Issue.assign_severity(data.data["severity"]),
        issueOwnerId=config["userId"],
        dueDate=get_due_date(score=data.data["severity"], config=config, key=data.init_key),
        identification=IDENTIFICATION_TYPE,
        status=config["issues"][data.init_key]["status"],
        createdById=config["userId"],
        lastUpdatedById=config["userId"],
        dateLastUpdated=get_current_datetime(DATE_FORMAT),
    )


def map_365_recommendation_to_issue(data: DefenderData, config: dict, description: str) -> Issue:
    """
    Function to map a Microsoft 365 Defender recommendation to a RegScale issue

    :param DefenderData data: Microsoft Defender recommendation
    :param dict config: Application config
    :param str description: Description of the recommendation
    :return: RegScale issue
    :rtype: Issue
    """
    return Issue(
        title=f'{data.data["recommendationName"]}',
        dateCreated=get_current_datetime(DATE_FORMAT),
        description=description,
        severityLevel=Issue.assign_severity(data.data["severityScore"]),
        issueOwnerId=config["userId"],
        dueDate=get_due_date(score=data.data["severityScore"], config=config, key=data.init_key),
        identification=IDENTIFICATION_TYPE,
        status=config["issues"][data.init_key]["status"],
        vendorName=data.data["vendor"],
        createdById=config["userId"],
        lastUpdatedById=config["userId"],
        dateLastUpdated=get_current_datetime(DATE_FORMAT),
    )


def map_cloud_alert_to_issue(data: DefenderData, config: dict, description: str) -> Issue:
    """
    Function to map a Microsoft Defender for Cloud alert to a RegScale issue

    :param DefenderData data: Microsoft Defender for Cloud alert
    :param dict config: Application config
    :param str description: Description of the alert
    :return: RegScale issue
    :rtype: Issue
    """
    return Issue(
        title=f'{data.data["properties"]["productName"]} Alert - {data.data["properties"]["compromisedEntity"]}',
        dateCreated=get_current_datetime(DATE_FORMAT),
        description=description,
        severityLevel=Issue.assign_severity(data.data["properties"]["severity"]),
        issueOwnerId=config["userId"],
        dueDate=get_due_date(
            score=data.data["properties"]["severity"],
            config=config,
            key="defenderCloud",
        ),
        identification=IDENTIFICATION_TYPE,
        status=config["issues"]["defenderCloud"]["status"],
        vendorName=data.data["properties"]["vendorName"],
        createdById=config["userId"],
        lastUpdatedById=config["userId"],
        dateLastUpdated=get_current_datetime(DATE_FORMAT),
    )
