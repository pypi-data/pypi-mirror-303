import datetime
import gzip
import io
import os
import re
import subprocess
import sys
import zipfile

from logging import Logger

from ingestion.caris.util.tests import safely_extract_tests_from_json_data
from ingestion.vcf_standardization.standardize import standardize_vcf


# This is done in next step, we are just adding to yaml
def extract_sv(prefix, include_somatic: bool, include_germline: bool):
    vcfs = []

    # Hard-code genome reference for Caris VCFs
    genome_reference = "GRCh38"

    if include_somatic:
        vcfs.append(
            {
                "fileName": f".lifeomic/caris/{prefix}/{prefix}.modified.somatic.nrm.filtered.vcf.gz",
                "sequenceType": "somatic",
                "type": "shortVariant",
                "reference": genome_reference,
            }
        )

    if include_germline:
        vcfs.append(
            {
                "fileName": f".lifeomic/caris/{prefix}/{prefix}.modified.germline.nrm.filtered.vcf.gz",
                "sequenceType": "germline",
                "type": "shortVariant",
                "reference": genome_reference,
            }
        )

    return vcfs


def get_vendsig_dict(json_data, log: Logger):
    # Return a dicitionary of {'chr:star_pos:ref:alt' : 'vendsig'}
    vendsig_dict = {"vendor": "caris"}
    extracted_tests = safely_extract_tests_from_json_data(json_data)

    for test in extracted_tests:
        results = [
            result
            for result in test.get("testResults", {})
            if isinstance(result, dict) and "genomicAlteration" in result.keys()
        ]
        for result in results:
            if "alterationDetails" in result["genomicAlteration"].keys():
                vendsig = map_vendsig(result["genomicAlteration"]["result"])
                sv = result["genomicAlteration"]["alterationDetails"]["transcriptAlterationDetails"]
                vendsig_dict.update(
                    {
                        f'{result["genomicAlteration"]["chromosome"]}:{sv["transcriptStartPosition"]}:{sv["referenceNucleotide"]}:{sv["observedNucleotide"]}': vendsig
                    }
                )

    return vendsig_dict


def map_vendsig(ci: str) -> str:
    if ci in ["Pathogenic Variant", "Pathogenic"]:
        return "Pathogenic"
    elif ci in ["Likely Pathogenic Variant", "Likely Pathogenic"]:
        return "Likely pathogenic"
    elif ci in ["Benign Variant", "Benign"]:
        return "Benign"
    elif ci in ["Likely Benign Variant", "Likely Benign"]:
        return "Likely benign"
    elif ci in ["Variant of Uncertain Significance", "VUS"]:
        return "Uncertain significance"
    else:
        return "Unknown"


def process_caris_vcf(infile, json_data, outpath, file_name, log: Logger):
    line_count = 0
    vendsig_dict = {"vendor": "caris"}

    if "germline.vcf" in infile:
        outfile = f"{file_name}.modified.germline.vcf"
        sample_name = "germline_" + file_name

    else:
        outfile = f"{file_name}.modified.somatic.vcf"
        sample_name = file_name
        # Read in a dictionary of variants with VENDSIG from the JSON file for somatic only
        vendsig_dict = get_vendsig_dict(json_data, log)

    line_count = standardize_vcf(
        infile=infile,
        outfile=outfile,
        out_path=outpath,
        case_id=sample_name,
        log=log,
        vendsig_dict=vendsig_dict,
        compression=True,
    )

    return line_count
