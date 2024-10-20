import csv
import logging
import os

from singleton_decorator import singleton
from typing import List, Optional

from . import constants
from .file_utils import check_infile_status
from .record import Record

DEFAULT_OUTDIR = os.path.join(
    constants.DEFAULT_OUTDIR_BASE,
    os.path.splitext(os.path.basename(__file__))[0],
    constants.DEFAULT_TIMESTAMP
)

@singleton
class Parser:
    """Class for parsing tab-delimited review file."""

    def __init__(self, **kwargs):
        """Constructor for class Parser"""
        self.config = kwargs.get("config", None)
        self.config_file = kwargs.get("config_file", None)
        self.infile = kwargs.get("infile", None)
        self.logfile = kwargs.get("logfile", None)
        self.outdir = kwargs.get("outdir", DEFAULT_OUTDIR)
        self.verbose = kwargs.get("verbose", constants.DEFAULT_VERBOSE)

        self._is_parsed = False
        self._records = []

        logging.info(f"Instantiated Parser in {os.path.abspath(__file__)}")

    def get_records(self, infile: Optional[str]) -> List[Record]:
        """Get the records.

        Args:
            infile (Optional[str]): The path to the file.

        Returns:
            List[Record]: List of records.
        """
        if not self._is_parsed:
            self._parse_file(infile)
        return self._records

    def _parse_file(self, infile: Optional[str]) -> None:
        """Parse the tab-delimited review file.

        Args:
            infile (Optional[str]): The path to the file.
        """
        if infile is None:
            infile = self.infile

        check_infile_status(infile)

        logging.info(f"Will parse the tab-delimited review file '{infile}'")

        with open(infile, mode='r') as f:

            reader = csv.reader(f)

            line_ctr = 0

            for row in reader:

                line_ctr += 1

                if line_ctr == 1:
                    continue

                record = Record(
                    lab_number=row[constants.DEFAULT_LAB_NUMBER_IDX],
                    overall_call=row[constants.DEFAULT_OVERALL_CALL_IDX],
                    gene=row[constants.DEFAULT_GENE_IDX],
                    zygosity=row[constants.DEFAULT_ZYGOSITY_IDX],
                    mutation=row[constants.DEFAULT_MUTATION_IDX],
                    variant_phen=row[constants.DEFAULT_VARIANT_PHEN_IDX],
                    disease=row[constants.DEFAULT_DISEASE_IDX],
                    internal_comment=row[constants.DEFAULT_INTERNAL_COMMENT_IDX],
                    is_on_report=row[constants.DEFAULT_IS_ON_REPORT_IDX],
                    sanger=row[constants.DEFAULT_SANGER_IDX],
                    score=row[constants.DEFAULT_SCORE_IDX],
                    link=row[constants.DEFAULT_LINK_IDX],
                    quality=row[constants.DEFAULT_QUALITY_IDX],
                    format=row[constants.DEFAULT_FORMAT_IDX],
                    mrna=row[constants.DEFAULT_MRNA_IDX],
                    clinical_category=row[constants.DEFAULT_CLINICAL_CATEGORY_IDX],
                    clinical_genetics_supporting=row[constants.DEFAULT_CLINICAL_GENETICS_SUPPORTING_IDX],
                    clinical_genetics_disprove=row[constants.DEFAULT_CLINICAL_GENETICS_DISPROVE_IDX],
                    clinical_genetics_intermediate=row[constants.DEFAULT_CLINICAL_GENETICS_DISPROVE_IDX],
                    population_genetics_supporting=row[constants.DEFAULT_POPULATION_GENETICS_SUPPORTING_IDX],
                    population_genetics_disprove=row[constants.DEFAULT_POPULATION_GENETICS_DISPROVE_IDX],
                    population_genetics_intermediate=row[constants.DEFAULT_POPULATION_GENETICS_INTERMEDIATE_IDX],
                    functional_assay=row[constants.DEFAULT_FUNCTIONAL_ASSAY_IDX],
                    experimental_supporting=row[constants.DEFAULT_EXPERIMENTAL_SUPPORTING_IDX],
                    experimental_disprove=row[constants.DEFAULT_EXPERIMENTAL_DISPROVE_IDX],
                    experimental_intermediate=row[constants.DEFAULT_EXPERIMENTAL_INTERMEDIATE_IDX],
                    theoretical_supporting=row[constants.DEFAULT_THEORETICAL_SUPPORTING_IDX],
                    theoretical_disprove=row[constants.DEFAULT_THEORETICAL_DISPROVE_IDX],
                    theoretical_intermediate=row[constants.DEFAULT_THEORETICAL_INTERMEDIATE_IDX],
                    unnamed_1=row[constants.DEFAULT_UNNAMED_1_IDX],
                    unnamed_2=row[constants.DEFAULT_UNNAMED_2_IDX],
                    unnamed_3=row[constants.DEFAULT_UNNAMED_3_IDX],
                    unnamed_4=row[constants.DEFAULT_UNNAMED_4_IDX],
                    gnomad_het_ac=row[constants.DEFAULT_GNOMAD_HET_AC_IDX],
                    gnomad_homo_ac=row[constants.DEFAULT_GNOMAD_HOMO_AC_IDX],
                    gnomad_popmax_af=row[constants.DEFAULT_GNOMAD_POPMAX_AF_IDX],
                    gnomad_overall_af=row[constants.DEFAULT_GNOMAD_OVERALL_AF_IDX],
                    clinvar_id=row[constants.DEFAULT_CLINVAR_ID_IDX],
                    clinvar_significance=row[constants.DEFAULT_CLINVAR_SIGNIFICANCE_IDX],
                    clinvar_ambry=row[constants.DEFAULT_CLINVAR_AMBRY_IDX],
                    clinvar_invitae=row[constants.DEFAULT_CLINVAR_INVITAE_IDX],
                    clinvar_counsyl=row[constants.DEFAULT_CLINVAR_COUNSYL_IDX],
                    clinvar_iglcoa=row[constants.DEFAULT_CLINVAR_IGLCOA_IDX],
                    clinvar_genedx=row[constants.DEFAULT_CLINVAR_GENEDX_IDX],
                    clinvar_natera=row[constants.DEFAULT_CLINVAR_NATERA_IDX],
                    cadd_phred_score=row[constants.DEFAULT_CADD_PHRED_SCORE_IDX],
                    spliceai_score=row[constants.DEFAULT_SPLICEAI_SCORE_IDX],
                    exon_number=row[constants.DEFAULT_EXON_NUMBER_IDX],
                    fs_value=row[constants.DEFAULT_FS_VALUE_IDX],
                    hgmd_class=row[constants.DEFAULT_HGMD_CLASS_IDX],
                    hgmd_id=row[constants.DEFAULT_HGMD_ID_IDX],
                    hgmd_phen=row[constants.DEFAULT_HGMD_PHEN_IDX],
                    hgmd_pmid=row[constants.DEFAULT_HGMD_PMID_IDX],
                    mut_type=row[constants.DEFAULT_MUT_TYPE_IDX],
                    bam_link=row[constants.DEFAULT_BAM_LINK_IDX],
                    igv_link=row[constants.DEFAULT_IGV_LINK_IDX],
                    proximal=row[constants.DEFAULT_PROXIMAL_IDX],
                )

                self._records.append(record)

            logging.info(f"Processed '{line_ctr}' lines in the file '{infile}'")

