"""Connector Types Enum"""

from enum import Enum


class ConnectorType(str, Enum):
    """Different ConnectorTypes"""

    Assets = "Assets"
    Edr = "Edr"
    Hooks = "Hooks"
    Identity = "Identity"
    Notifications = "Notifications"
    Siem = "SIEM"
    Sink = "Sink"
    Storage = "Storage"
    Ticketing = "Ticketing"
    Vulnerabilities = "Vulnerabilities"

    def __str__(self):
        """Return the value of the Enum"""
        return self.value
