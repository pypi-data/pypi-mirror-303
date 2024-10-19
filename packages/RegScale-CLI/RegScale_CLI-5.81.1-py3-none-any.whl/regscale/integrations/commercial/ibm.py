#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IBM AppScan RegScale integration"""
from datetime import datetime
from os import PathLike
from pathlib import Path

import click
from rich.console import Console

from regscale.core.app.application import Application
from regscale.models.integration_models.flat_file_importer import FlatFileImporter
from regscale.models.integration_models.ibm import AppScan
from regscale.validation.record import validate_regscale_object


@click.group()
def ibm():
    """Performs actions on IBM AppScan files."""


@ibm.command(name="show_mapping")
def show_mapping():
    """Show the default mapping for IBM AppScan."""
    import json

    mapping = AppScan.default_mapping().mapping
    console = Console()
    # convert dict to json string
    dat = json.dumps(mapping, indent=4)
    console.print(dat)


@ibm.command(name="import_appscan")
@FlatFileImporter.common_scanner_options(
    message="File path to the folder containing IBM AppScan .csv files to process to RegScale.",
    prompt="File path for IBM AppScan files:",
)
def import_appscan(folder_path: PathLike[str], regscale_ssp_id: int, scan_date: datetime) -> None:
    """
    Import IBM AppScan scans, vulnerabilities and assets to RegScale from IBM AppScan files
    """
    app = Application()
    if not validate_regscale_object(regscale_ssp_id, "securityplans"):
        app.logger.warning("SSP #%i is not a valid RegScale Security Plan.", regscale_ssp_id)
        return
    if not scan_date or not FlatFileImporter.check_date_format(scan_date):
        scan_date = datetime.now()
    if len(list(Path(folder_path).glob("*.csv"))) == 0:
        app.logger.warning("No IBM AppScan(csv) files found in the specified folder.")
        return
    for file in Path(folder_path).glob("*.csv"):
        AppScan(name="IBM AppScan", file_path=str(file), plan_id=regscale_ssp_id, scan_date=scan_date)
