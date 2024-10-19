#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Scanner Variables """

from regscale.core.app.utils.variables import RsVariablesMeta, RsVariableType


class ScannerVariables(metaclass=RsVariablesMeta):
    """
    Scanner Variables class to define class-level attributes with type annotations and examples
    """

    # Define class-level attributes with type annotations and examples
    issueCreation: RsVariableType(str, "PerAsset|Consolidated", required=True)  # type: ignore # noqa: F722,F821
    vulnerabilityCreation: RsVariableType(str, "NoIssue|IssueCreation|PoamCreation", required=True)  # type: ignore  # noqa: F722,F821
    userId: RsVariableType(str, "00000000-0000-0000-0000-000000000000")  # type: ignore # noqa: F722,F821
    poamTitleType: RsVariableType(str, "Cve|PluginId", default="Cve", required=False)  # type: ignore # noqa: F722,F821
    tenableGroupByPlugin: RsVariableType(bool, "true|false", default=False, required=False)  # type: ignore # noqa: F722,F821
    threadMaxWorkers: RsVariableType(int, "1-8", default=4, required=False)  # type: ignore # noqa: F722,F821
