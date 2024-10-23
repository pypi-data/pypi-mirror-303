"""Class to handle mapping RegScale models to OCSF models for Synqly integration"""

from datetime import datetime
from typing import Any, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from regscale.integrations.commercial.synqly.connectors.ticketing import Ticketing

from synqly import engine
from synqly.engine import CreateTicketRequest
from synqly.engine.resources.ticketing.types.priority import Priority

from regscale.core.app.utils.app_utils import (
    error_and_exit,
    convert_datetime_to_regscale_string,
)
from synqly.engine.resources.ticketing.types.ticket import Ticket
from regscale.models.regscale_models import Issue


class Mapper:
    """Mapping class to handle RegScale models to OCSF models for Synqly integration"""

    def to_oscf(self, regscale_object: Any, **kwargs: dict) -> Any:
        """
        Convert RegScale object to OCSF object

        :param Any regscale_object: RegScale object to convert to an OCSF object
        :param dict **kwargs: Keyword Arguments
        :return: The comparable OCSF object
        :rtype: Any
        """
        if isinstance(regscale_object, Issue):
            return self._regscale_issue_to_ticket(regscale_object, **kwargs)
        else:
            error_and_exit(f"Unsupported object type {type(regscale_object)}")

    def to_regscale(self, connector: Union["Ticketing"], oscf_object: Any, **kwargs: dict) -> Any:
        """
        Convert OCSF object to RegScale object

        :param Union["Ticketing"] connector: Connector class object
        :param Any oscf_object: OCSF object to convert to a RegScale object
        :param dict **kwargs: Keyword Arguments
        :return: The comparable RegScale object
        :rtype: Any
        """
        if isinstance(oscf_object, Ticket):
            return self._ticket_to_regscale(connector, oscf_object, **kwargs)
        else:
            error_and_exit(f"Unsupported object type {type(oscf_object)}")

    @staticmethod
    def _ticket_to_regscale(connector: Union["Ticketing"], ticket: Ticket, **kwargs) -> Issue:
        """
        Convert OCSF Ticket to RegScale Issue

        :param Union["Ticketing"] connector: Connector class object
        :param Ticket ticket: OCSF Ticket to convert to a RegScale Issue
        :param dict **kwargs: Keyword Arguments
        :return: The comparable RegScale Issue
        :rtype: Issue
        """
        due_date = convert_datetime_to_regscale_string(ticket.due_date)
        ticket_dict = ticket.dict()
        key_val_desc = "All fields:\n"
        for k, v in ticket_dict.items():
            key_val_desc += f"{k.replace('_', ' ').title()}: {str(v) or 'NULL'}\n"
        regscale_issue = Issue(
            title=ticket.summary,
            severityLevel=Issue.assign_severity(ticket.priority),
            dueDate=due_date,
            description=f"Description {ticket.description}\n{key_val_desc}",
            status=("Closed" if ticket.status.lower() == "done" else "Draft"),
            dateCompleted=(
                convert_datetime_to_regscale_string(ticket.completion_date) if ticket.status.lower() == "done" else None
            ),
            **kwargs,
        )
        # update the correct integration field names or manual detection fields
        if connector.has_integration_field:
            setattr(regscale_issue, connector.integration_id_field, ticket.id)
        else:
            regscale_issue.manualDetectionSource = connector.integration
            regscale_issue.manualDetectionId = ticket.id
        return regscale_issue

    @staticmethod
    def _map_ticket_priority(severity: str) -> Priority:
        """
        Map RegScale severity to OCSF priority

        :param str severity: RegScale severity
        :return: OCSF priority
        :rtype: Priority
        """
        if "high" in severity.lower():
            return Priority.HIGH
        elif "moderate" in severity.lower():
            return Priority.MEDIUM
        else:
            return Priority.LOW

    def _regscale_issue_to_ticket(self, regscale_issue: Issue, **kwargs: dict) -> CreateTicketRequest:
        """
        Maps a RegScale issue to a JIRA issue

        :param Issue regscale_issue: RegScale issue object
        :param dict kwargs: Additional keyword arguments
        :return: Synqly CreateTicketRequest object
        :rtype: CreateTicketRequest
        """
        # TODO: there is a bug in synqly code that due_data and priority are mandatory even if they aren't applicable
        return engine.CreateTicketRequest(
            name=regscale_issue.title,
            summary=f"RegScale Issue #{regscale_issue.id}: {regscale_issue.description}",
            creator=kwargs.get("creator", "RegScale CLI"),
            priority=self._map_ticket_priority(regscale_issue.severityLevel),
            status=regscale_issue.status,
            due_date=datetime.strptime(regscale_issue.dueDate, "%Y-%m-%dT%H:%M:%S"),  # convert string to datetime
            **kwargs,
        )
