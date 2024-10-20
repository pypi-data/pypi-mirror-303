import csv
import logging
import os
from datetime import datetime

from singleton_decorator import singleton
from typing import List, Optional

from . import constants
from .record import Record


@singleton
class Writer:
    """Class for writing comma-separated samplesheet file."""

    def __init__(self, **kwargs):
        """Constructor for class Writer."""
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", None)
        self.outfile = kwargs.get("outfile", None)
        self.logfile = kwargs.get("logfile", None)
        self.outdir = kwargs.get("outdir", constants.DEFAULT_OUTDIR)
        self.verbose = kwargs.get("verbose", constants.DEFAULT_VERBOSE)

        logging.info(f"Instantiated Writer in {os.path.abspath(__file__)}")

    def write_file(self, records: List[Record], outfile: Optional[str]) -> None:
        """Write the records to the output comma-separated file.

        Args:
            records: List of records.
            outfile (Optional[str]): The path to the output file.
        """
        with open(outfile, 'w') as of:
            of.write(f"## method-created: {os.path.abspath(__file__)}\n")
            of.write(f"## date-created: {str(datetime.today().strftime('%Y-%m-%d-%H%M%S'))}\n")
            of.write(f"## created-by: {os.environ.get('USER')}\n")
            of.write(f"## logfile: {self.logfile}\n")

            header_line = "\t".join(self.config.get("column_headers"))

            of.write(f"{header_line}\n")

            for record in records:
                line = record.lab_number + "\t" + \
                    record.overall_call + "\t" + \
                    record.gene + "\t" + \
                    record.zygosity + "\t" + \
                    record.mutation + "\t" + \
                    record.variant_phen + "\t" + \
                    record.disease + "\t" + \
                    record.internal_comment + "\t" + \
                    record.is_on_report + "\t" + \
                    record.sanger + "\t" + \
                    record.score + "\t" + \
                    record.vcf + "\t" + \
                    record.interpretation + "\t" + \
                    record.source + "\t" + \
                    record.link + "\t" + \
                    record.quality + "\t" + \
                    record.format + "\t" + \
                    record.mrna + "\t" + \
                    record.clinical_category + "\t" + \
                    record.clinical_genetics_supporting + "\t" + \
                    record.clinical_genetics_disprove + "\t" + \
                    record.clinical_genetics_intermediate + "\t" + \
                    record.functional_assay + "\t" + \
                    record.experimental_supporting + "\t" + \
                    record.experimental_disprove + "\t" + \
                    record.experimental_intermediate + "\t" + \
                    record.theoretical_supporting + "\t" + \
                    record.theoretical_disprove + "\t" + \
                    record.theoretical_intermediate + "\t" + \
                    record.unnamed_1 + "\t" + \
                    record.unnamed_2 + "\t" + \
                    record.unnamed_3 + "\t" + \
                    record.unnamed_4 + "\t" + \
                    record.gnomad_het_ac + "\t" + \
                    record.gnomad_homo_ac + "\t" + \
                    record.gnomad_popmax_af + "\t" + \
                    record.gnomad_overall_af + "\t" + \
                    record.clinvar_id + "\t" + \
                    record.clinvar_significance + "\t" + \
                    record.clinvar_ambry + "\t" + \
                    record.clinvar_invitae + "\t" + \
                    record.clinvar_counsyl + "\t" + \
                    record.clinvar_iglcoa + "\t" + \
                    record.clinvar_genedx + "\t" + \
                    record.clinvar_natera + "\t" + \
                    record.cadd_phred_score + "\t" + \
                    record.spliceai_score + "\t" + \
                    record.exon_number + "\t" + \
                    record.fs_value + "\t" + \
                    record.hgmd_class + "\t" + \
                    record.hgmd_id + "\t" + \
                    record.hgmd_phen + "\t" + \
                    record.hgmd_pmid + "\t" + \
                    record.mut_type + "\t" + \
                    record.bam_link + "\t" + \
                    record.igv_link + "\t" + \
                    record.proximal

                of.write(f"{line}\n")

        logging.info(f"Wrote tab-delimited review file '{outfile}'")

        if self.verbose:
            print(f"Wrote tab-delimited review file '{outfile}'")

