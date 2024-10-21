from cocotb_coverage.coverage import merge_coverage, coverage_db
from .dyutools import find_all_match
import logging
import xml.etree.ElementTree as ET
import click
from pathlib import Path


@click.command()
@click.option('--path', prompt="The path from where to search")
@click.option('--pattern', prompt="The pattern forcoverage xml file")
def fcov_merge(path='./', pattern='.*coverage.xml'):
    log = logging.getLogger("merge coverage")
    all_files = find_all_match(pattern, path)
    log.info(f"Coverage files found {all_files}")
    if Path("functional_coverage.xml").exists():
        Path("functional_coverage.xml").rename("old_functional_coverage.xml")
    merge_coverage(log.info, "functional_coverage.xml", *all_files)
    root = ET.parse("functional_coverage.xml")
    top = root.getroot()
    section = ET.Element("section")
    field = ET.SubElement(section, "field")
    field.set("name", top.attrib['abs_name'])
    field.set("value", top.attrib['cover_percentage'])
    for e in root.findall(".//*[@coverage]"):
        field = ET.SubElement(section, "field")
        field.set("name", e.attrib['abs_name'])
        field.set("value", e.attrib['cover_percentage'])
    ET.ElementTree(element=section).write('fcov_report.xml')

    coverage_db.report_coverage(log.info)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fcov_merge()
