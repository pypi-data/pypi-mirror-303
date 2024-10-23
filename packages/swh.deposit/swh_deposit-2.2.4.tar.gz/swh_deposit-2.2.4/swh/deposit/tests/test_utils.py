# Copyright (C) 2018-2022  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from xml.etree import ElementTree

import pytest

from swh.deposit import utils
from swh.model.exceptions import ValidationError
from swh.model.swhids import CoreSWHID, QualifiedSWHID


@pytest.fixture
def xml_with_origin_reference():
    xml_data = """<?xml version="1.0"?>
  <entry xmlns="http://www.w3.org/2005/Atom"
           xmlns:codemeta="https://doi.org/10.5063/SCHEMA/CODEMETA-2.0"
           xmlns:swh="https://www.softwareheritage.org/schema/2018/deposit">
      <swh:deposit>
        <swh:reference>
          <swh:origin url="{url}"/>
        </swh:reference>
      </swh:deposit>
  </entry>
    """
    return xml_data.strip()


def test_normalize_date_0():
    """When date is a list, choose the first date and normalize it"""
    actual_date = utils.normalize_date(["2017-10-12", "date1"])

    assert actual_date == {
        "timestamp": {"microseconds": 0, "seconds": 1507766400},
        "offset": 0,
    }


def test_normalize_date_1():
    """Providing a date in a reasonable format, everything is fine"""
    actual_date = utils.normalize_date("2018-06-11 17:02:02")

    assert actual_date == {
        "timestamp": {"microseconds": 0, "seconds": 1528736522},
        "offset": 0,
    }


def test_normalize_date_doing_irrelevant_stuff():
    """Providing a date with only the year results in a reasonable date"""
    actual_date = utils.normalize_date("2017")

    assert actual_date == {
        "timestamp": {"seconds": 1483228800, "microseconds": 0},
        "offset": 0,
    }


@pytest.mark.parametrize(
    "swhid,expected_metadata_context",
    [
        (
            "swh:1:cnt:51b5c8cc985d190b5a7ef4878128ebfdc2358f49",
            {"origin": None},
        ),
        (
            "swh:1:snp:51b5c8cc985d190b5a7ef4878128ebfdc2358f49;origin=http://blah",
            {"origin": "http://blah", "path": None},
        ),
        (
            "swh:1:dir:51b5c8cc985d190b5a7ef4878128ebfdc2358f49;path=/path",
            {"origin": None, "path": b"/path"},
        ),
        (
            "swh:1:rev:51b5c8cc985d190b5a7ef4878128ebfdc2358f49;visit=swh:1:snp:41b5c8cc985d190b5a7ef4878128ebfdc2358f49",  # noqa
            {
                "origin": None,
                "path": None,
                "snapshot": CoreSWHID.from_string(
                    "swh:1:snp:41b5c8cc985d190b5a7ef4878128ebfdc2358f49"
                ),
            },
        ),
        (
            "swh:1:rel:51b5c8cc985d190b5a7ef4878128ebfdc2358f49;anchor=swh:1:dir:41b5c8cc985d190b5a7ef4878128ebfdc2358f49",  # noqa
            {
                "origin": None,
                "path": None,
                "directory": CoreSWHID.from_string(
                    "swh:1:dir:41b5c8cc985d190b5a7ef4878128ebfdc2358f49"
                ),
            },
        ),
    ],
)
def test_compute_metadata_context(swhid: str, expected_metadata_context):
    assert expected_metadata_context == utils.compute_metadata_context(
        QualifiedSWHID.from_string(swhid)
    )


def test_parse_swh_reference_origin(xml_with_origin_reference):
    url = "https://url"
    xml_data = xml_with_origin_reference.format(url=url)
    metadata = ElementTree.fromstring(xml_data)

    actual_origin = utils.parse_swh_reference(metadata)
    assert actual_origin == url


@pytest.fixture
def xml_swh_deposit_template():
    xml_data = """<?xml version="1.0"?>
  <entry xmlns:swh="https://www.softwareheritage.org/schema/2018/deposit"
         xmlns:schema="http://schema.org/">
      <swh:deposit>
        {swh_deposit}
      </swh:deposit>
  </entry>
    """
    return xml_data.strip()


@pytest.mark.parametrize(
    "xml_ref",
    [
        "",
        "<swh:reference></swh:reference>",
        "<swh:reference><swh:object /></swh:reference>",
        """<swh:reference><swh:object swhid="" /></swh:reference>""",
    ],
)
def test_parse_swh_reference_empty(xml_swh_deposit_template, xml_ref):
    xml_body = xml_swh_deposit_template.format(swh_deposit=xml_ref)
    metadata = ElementTree.fromstring(xml_body)

    assert utils.parse_swh_reference(metadata) is None


@pytest.fixture
def xml_with_swhid(atom_dataset):
    return atom_dataset["entry-data-with-swhid-no-prov"]


@pytest.mark.parametrize(
    "swhid",
    [
        "swh:1:cnt:31b5c8cc985d190b5a7ef4878128ebfdc2358f49;origin=https://hal.archives-ouvertes.fr/hal-01243573;visit=swh:1:snp:4fc1e36fca86b2070204bedd51106014a614f321;anchor=swh:1:rev:9c5de20cfb54682370a398fcc733e829903c8cba;path=/moranegg-AffectationRO-df7f68b/",  # noqa
        "swh:1:dir:31b5c8cc985d190b5a7ef4878128ebfdc2358f49;anchor=swh:1:dir:9c5de20cfb54682370a398fcc733e829903c8cba",  # noqa
        "swh:1:rev:31b5c8cc985d190b5a7ef4878128ebfdc2358f49;anchor=swh:1:rev:9c5de20cfb54682370a398fcc733e829903c8cba",  # noqa
        "swh:1:rel:31b5c8cc985d190b5a7ef4878128ebfdc2358f49;anchor=swh:1:rel:9c5de20cfb54682370a398fcc733e829903c8cba",  # noqa
        "swh:1:snp:31b5c8cc985d190b5a7ef4878128ebfdc2358f49;anchor=swh:1:snp:9c5de20cfb54682370a398fcc733e829903c8cba",  # noqa
        "swh:1:dir:31b5c8cc985d190b5a7ef4878128ebfdc2358f49",
    ],
)
def test_parse_swh_reference_swhid(swhid, xml_with_swhid):
    xml_data = xml_with_swhid.format(
        swhid=swhid,
    )
    metadata = ElementTree.fromstring(xml_data)

    actual_swhid = utils.parse_swh_reference(metadata)
    assert actual_swhid is not None

    expected_swhid = QualifiedSWHID.from_string(swhid)
    assert actual_swhid == expected_swhid


@pytest.mark.parametrize(
    "invalid_swhid",
    [
        # incorrect length
        "swh:1:cnt:31b5c8cc985d190b5a7ef4878128ebfdc235"  # noqa
        # visit qualifier should be a core SWHID with type,
        "swh:1:dir:c4993c872593e960dc84e4430dbbfbc34fd706d0;visit=swh:1:rev:0175049fc45055a3824a1675ac06e3711619a55a",  # noqa
        # anchor qualifier should be a core SWHID with type one of
        "swh:1:rev:c4993c872593e960dc84e4430dbbfbc34fd706d0;anchor=swh:1:cnt:b5f505b005435fa5c4fa4c279792bd7b17167c04;path=/",  # noqa
        "swh:1:rev:c4993c872593e960dc84e4430dbbfbc34fd706d0;visit=swh:1:snp:0175049fc45055a3824a1675ac06e3711619a55a;anchor=swh:1:snp:b5f505b005435fa5c4fa4c279792bd7b17167c04",  # noqa
    ],
)
def test_parse_swh_reference_invalid_swhid(invalid_swhid, xml_with_swhid):
    """Unparsable swhid should raise"""
    xml_invalid_swhid = xml_with_swhid.format(swhid=invalid_swhid)
    metadata = ElementTree.fromstring(xml_invalid_swhid)

    with pytest.raises(ValidationError):
        utils.parse_swh_reference(metadata)


@pytest.mark.parametrize(
    "xml_ref",
    [
        "",
        "<swh:metadata-provenance></swh:metadata-provenance>",
        "<swh:metadata-provenance><schema:url /></swh:metadata-provenance>",
    ],
)
def test_parse_swh_metatada_provenance_empty(xml_swh_deposit_template, xml_ref):
    xml_body = xml_swh_deposit_template.format(swh_deposit=xml_ref)
    metadata = ElementTree.fromstring(xml_body)

    assert utils.parse_swh_metadata_provenance(metadata) is None


@pytest.fixture
def xml_with_metadata_provenance(atom_dataset):
    return atom_dataset["entry-data-with-metadata-provenance"]


def test_parse_swh_metadata_provenance2(xml_with_metadata_provenance):
    xml_data = xml_with_metadata_provenance.format(url="https://url.org/metadata/url")
    metadata = ElementTree.fromstring(xml_data)

    actual_url = utils.parse_swh_metadata_provenance(metadata)

    assert actual_url == "https://url.org/metadata/url"
