#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aqua RegScale integration"""
from datetime import datetime
from os import PathLike
from pathlib import Path

import click

from regscale.core.app.application import Application
from regscale.models.integration_models.aqua import Aqua
from regscale.models.integration_models.flat_file_importer import FlatFileImporter
from regscale.validation.record import validate_regscale_object


@click.group()
def aqua():
    """Performs actions on Aqua Scanner artifacts."""


@aqua.command(name="import_aqua")
@FlatFileImporter.common_scanner_options(
    message="File path to the folder containing Aqua .csv files to process to RegScale.",
    prompt="File path for Aqua files:",
)
def import_aqua(folder_path: PathLike[str], regscale_ssp_id: int, scan_date: datetime):
    """
    Import Aqua scan data to RegScale
    """
    import_aqua_scan(folder_path, regscale_ssp_id, scan_date)


def import_aqua_scan(folder_path: PathLike[str], regscale_ssp_id: int, scan_date: datetime) -> None:
    """
    Import Aqua scan data to RegScale

    :param PathLike[str] folder_path: File path to the folder containing Aqua .csv files to process to RegScale
    :param int regscale_ssp_id: The RegScale SSP ID
    :param datetime scan_date: The date of the scan
    :rtype: None
    """
    """
        Import Aqua scans, vulnerabilities and assets to RegScale from Aqua files
        """
    app = Application()
    if not validate_regscale_object(regscale_ssp_id, "securityplans"):
        app.logger.warning("SSP #%i is not a valid RegScale Security Plan.", regscale_ssp_id)
        return
    if not scan_date or not FlatFileImporter.check_date_format(scan_date):
        scan_date = datetime.now()
    files = list(Path(folder_path).glob("*.csv")) + list(Path(folder_path).glob("*.xlsx"))
    if len(files) == 0:
        app.logger.warning("No Aqua(csv/xlsx) files found in the specified folder.")
        return
    for file in files:
        Aqua(name="Aqua", file_path=str(file), regscale_ssp_id=regscale_ssp_id, scan_date=scan_date)
