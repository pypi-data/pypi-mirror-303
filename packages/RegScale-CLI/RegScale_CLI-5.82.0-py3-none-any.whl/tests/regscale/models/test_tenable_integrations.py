import json
from random import randint
from unittest.mock import patch

import pytest
from lxml import etree

from regscale.core.app.utils.nessus_utils import cpe_xml_to_dict, get_cpe_file, lookup_cpe_item_by_name, lookup_kev
from regscale.integrations.public.cisa import pull_cisa_kev
from regscale.models.integration_models.tenable_models.models import TenableIOAsset


@pytest.fixture
def cpe_items():
    cpe_root = etree.parse(get_cpe_file())
    dat = cpe_xml_to_dict(cpe_root)
    return dat


@pytest.fixture
def new_assets():
    with open("./tests/test_data/ten_assets.json", "r") as f:
        dat = json.load(f)
    assets = [TenableIOAsset(**a) for a in dat]
    return assets


@patch("regscale.core.app.application.Application")
@patch("regscale.models.integration_models.tenable.TenableIOAsset.sync_to_regscale")
def test_fetch_assets(mock_app, new_assets):
    # Call the fetch_assets function
    assets = new_assets
    app = mock_app
    with patch.object(TenableIOAsset, "sync_to_regscale") as mock_sync:
        mock_sync(app=app, assets=assets, ssp_id=2)

        # Check that the sync_to_regscale method was called with the correct arguments
        mock_sync.assert_called_once_with(app=app, assets=assets, ssp_id=2)


def test_kev_lookup():
    cve = "CVE-1234-3456"
    data = pull_cisa_kev()
    avail = [dat["cveID"] for dat in data["vulnerabilities"]]
    index = randint(0, len(avail))
    assert lookup_kev(cve, data)[0] is None
    assert lookup_kev(avail[index], data)[0]


def test_cpe_lookup(cpe_items):
    name = "cpe:/a:gobalsky:vega:0.49.4"
    lookup_cpe_item_by_name(name, cpe_items)


def test_sync_vulns_data(sync_vuln_result):
    vulns = sync_vuln_result
    assert vulns
