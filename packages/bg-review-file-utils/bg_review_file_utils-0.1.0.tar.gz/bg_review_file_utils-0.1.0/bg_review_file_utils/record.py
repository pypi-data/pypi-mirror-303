from pydantic import BaseModel, Field, field_validator
from enum import Enum

from typing import Optional, Union

DEFAULT_HGMD_PHEN_MIN_LENGTH = 10
DEFAULT_HGMD_PHEN_MAX_LENGTH = 100

DEFAULT_HGMD_PMID_MIN_LENGTH = 10
DEFAULT_HGMD_PMID_MAX_LENGTH = 100

DEFAULT_MIN_GENE_NAME_LENGTH = 3
DEFAULT_MAX_GENE_NAME_LENGTH = 10

DEFAULT_MIN_MUTATION_LENGTH = 5
DEFAULT_MAX_MUTATION_LENGTH = 25

DEFAULT_MIN_DISEASE_LENGTH = 5
DEFAULT_MAX_DISEASE_LENGTH = 70

DEFAULT_INTERPRETATION_MIN_LENGTH = 5
DEFAULT_INTERPRETATION_MAX_LENGTH = 100


DEFAULT_SOURCE_MIN_LENGTH = 5
DEFAULT_SOURCE_MAX_LENGTH = 100


DEFAULT_LINK_PREFIX = '=HYPERLINK("https://gnomad.broadinstitute.org/variant/'
DEFAULT_LINK_SUFFIX = '","gnomAD")'

DEFAULT_CLINVAR_ID_PREFIX = '=HYPERLINK("https://www.ncbi.nlm.nim.gov/clinvar/variation/'

DEFAULT_BAM_LINK_PREFIX = '=HYPERLINK("https://localhost:60151/load?file=\\'

DEFAULT_IGV_LINK_PREFIX = '=HYPERLINK("https://localhost:60151/goto?locus='


class MutationTypeEnum(str, Enum):
    MT1 = "frameshift"
    MT2 = "HGVS_ERROR"
    MT3 = "intergenic"
    MT4 = "intronic"
    MT5 = "na"
    MT6 = "ncRNA"
    MT7 = "nonframeshift_deletion"
    MT8 = "nonframeshift_insertion"
    MT9 = "nonsynonymous_SNV"
    MT10 = "nonsynonymous_SNV_exonic_splice_region"
    MT11 = "splice_Acceptor_Site"
    MT12 = "splice_Donor_Site"
    MT13 = "splice_Region"
    MT14 = "start_Codon"
    MT15 = "stopgain_SNV"
    MT16 = "stoploss_SNV"
    MT17 = "synonymous_SNV"
    MT18 = "synonymous_SNV_exonic_splice_region"
    MT19 = "UTR3"
    MT20 = "UTR5"


class HGMDClassEnum(str, Enum):
    DFP = "DFP"
    DM = "DM"
    DMQ = "DM?"
    DP = "DP"
    FP = "FP"
    NA = "na"



class ClinvarSignificanceEnum(str, Enum):
    CS1 = "Benign|other"
    CS2 = "ClinVar_Significance"
    CS3 = "Conflicting_interpretations_of_pathogenicity"
    CS4 = "Conflicting_interpretations_of_pathogenicity|drug_response"
    CS5 = "Conflicting_interpretations_of_pathogenicity|other"
    CS6 = "Conflicting_interpretations_of_pathogenicity|other|risk_factor"
    CS6 = "Conflicting_interpretations_of_pathogenicity|risk_factor"
    CS7 = "drug_response"
    CS8 = "Likely_benign"
    CS9 = "Likely_pathogenic"
    CS10 = "na"
    CS11 = "not_provided"
    CS12 = "Pathogenic"
    CS13 = "Pathogenic/Likely_pathogenic"
    CS14 = "Pathogenic/Likely_pathogenic|risk_factor"
    CS15 = "Pathogenic|risk_factor"
    CS16 = "Uncertain_significance"
    CS17 = "Pathogenic,_low_penetrance"
    CS18 = "other"
    CS19 = "likely_benign"
    CS20 = "pathogenic"
    CS21 = "uncertain"


class ScoreEnum(str, Enum):
    S10 = 10
    S13 = 13
    S14 = 14
    S20 = 20
    S24 = 24
    S28 = 28
    S29 = 29
    S30 = 30
    S34 = 34
    S35 = 35


class InternalCommentEnum(str, Enum):
    LOW_COPY_REPEAT = "Low_copy_repeat"
    LOW_QUALITY = "Low_quality"
    LOW_QUALITY_ZYGOSITY = "Low_quality,Zygosity"
    ZYGOSITY = "Zygosity"


class IsOnReportEnum(str, Enum):
    Y = "Y"
    N = "N"


class SangerEnum(str, Enum):
    P = "P"
    N = "N"


class VariantPhenotypeEnum(str, Enum):
    CL = "CL"
    NA = "na"
    NR = "NR"
    OT = "OT"


class OverallCallEnum(str, Enum):
    HOLD = 'HOLD'
    Positive = 'Positive'
    Negative = 'Negative'


class ZygosityEnum(str, Enum):
    HEMIZYGOUS = 'Hem'
    HETEROZYGOUS = 'Het'
    LIKELY_HEMIZYGOUS = 'Lhm'
    LIKELY_HETEROZYGOUS = 'Lht'
    MOSAIC = 'Mos'


class Record(BaseModel):

    # Field/column number 1
    lab_number: Optional[int] = Field(None, title="Lab Number", min=7, max=7)

    # Field/column number 2
    overall_call: Optional[OverallCallEnum] = Field(None, title="Overall Call")

    # Field/column number 3
    gene: Optional[str] = Field(None, title="Gene")

    # Field/column number 4
    zygosity: Optional[ZygosityEnum] = Field(None, title="Zygosity")

    # Field/column number 5
    mutation: Optional[str] = Field(None, title="Mutation")

    # Field/column number 6
    variant_phen: Optional[VariantPhenotypeEnum] = Field(None, title="Variant Phen")

    # Field/column number 7
    disease: Optional[str] = Field(None, title="Disease")

    # Field/column number 8
    internal_comment: Optional[InternalCommentEnum] = Field(None, title="Internal Comment")

    # Field/column number 9
    is_on_report: Optional[IsOnReportEnum] = Field(None, title="Is On Report")

    # Field/column number 10
    sanger: Optional[SangerEnum] = Field(None, title="Sanger")

    # Field/column number 11
    score: Optional[ScoreEnum] = Field(None, title="Score")

    # Field/column number 12
    vcf: Optional[str] = Field(None, title="VCF")

    # Field/column number 13
    interpretation: Optional[str] = Field(None, title="Interpretation")

    # Field/column number 14
    source: Optional[str] = Field(None, title="Source")

    # Field/column number 15
    link: Optional[str] = Field(None, title="Link")

    # Field/column number 16
    quality: Optional[Union[str, float]] = Field(None, title="Quality")

    # Field/column number 17
    format: Optional[str] = Field(None, title="Format")

    # Field/column number 18
    mrna: Optional[str] = Field(None, title="mRNA")

    # Field/column number 19
    clinical_category: Optional[str] = Field(None, title="Clinical Category")

    # Field/column number 20
    clinical_genetics_supporting: Optional[str] = Field(None, title="Clinical Genetics Supporting")

    # Field/column number 21
    clinical_genetics_disprove: Optional[str] = Field(None, title="Clinical Genetics Disprove")

    # Field/column number 22
    clinical_genetics_intermediate: Optional[str] = Field(None, title="Clinical Genetics Intermediate")

    # Field/column number 23
    population_genetics_supporting: Optional[str] = Field(None, title="Population Genetics Supporting")

    # Field/column number 24
    population_genetics_disprove: Optional[str] = Field(None, title="Population Genetics Disprove")

    # Field/column number 25
    population_genetics_intermediate: Optional[str] = Field(None, title="Population Genetics Intermediate")

    # Field/column number 26
    functional_assay: Optional[str] = Field(None, title="Functional Assay")

    # Field/column number 27
    experimental_supporting: Optional[str] = Field(None, title="Experimental Supporting")

    # Field/column number 28
    experimental_disprove: Optional[str] = Field(None, title="Experimental Disprove")

    # Field/column number 29
    experimental_intermediate: Optional[str] = Field(None, title="Experimental Intermediate")

    # Field/column number 30
    theoretical_supporting: Optional[str] = Field(None, title="Theoretical Supporting")

    # Field/column number 31
    theoretical_disprove: Optional[str] = Field(None, title="Theoretical Disprove")

    # Field/column number 32
    theoretical_intermediate: Optional[str] = Field(None, title="Theoretical Intermediate")

    # Field/column number 33
    unnamed_1: Optional[str] = Field(None, title="Unnamed")

    # Field/column number 34
    unnamed_2: Optional[str] = Field(None, title="Unnamed")

    # Field/column number 35
    unnamed_3: Optional[str] = Field(None, title="Unnamed")

    # Field/column number 36
    unnamed_4: Optional[str] = Field(None, title="Unnamed")

    # Field/column number 37
    gnomad_het_ac: Optional[Union[str, int]] = Field(None, title="GNOMAD Het AC")

    # Field/column number 38
    gnomad_homo_ac: Optional[Union[str, int]] = Field(None, title="GNOMAD Homo AC")

    # Field/column number 39
    gnomad_popmax_af: Optional[Union[str, float]] = Field(None, title="GNOMAD population maximum allele frequency")

    # Field/column number 40
    gnomad_overall_af: Optional[Union[str, float]] = Field(None, title="GNOMAD Overall allele frequency")

    # Field/column number 41
    clinvar_id: Optional[str] = Field(None, title="ClinVar identifier")

    # Field/column number 42
    clinvar_significance: Optional[ClinvarSignificanceEnum] = Field(None, title="ClinVar Significance")

    # Field/column number 43
    clinvar_ambry: Optional[ClinvarSignificanceEnum] = Field(None, title="ClinVar Ambry")

    # Field/column number 44
    clinvar_invitae: Optional[ClinvarSignificanceEnum] = Field(None, title="ClinVar Invitae")

    # Field/column number 45
    clinvar_counsyl: Optional[ClinvarSignificanceEnum] = Field(None, title="ClinVar Counsyl")

    # Field/column number 46
    clinvar_iglcoa: Optional[ClinvarSignificanceEnum] = Field(None, title="ClinVar IGLCoA")

    # Field/column number 47
    clinvar_genedx: Optional[ClinvarSignificanceEnum] = Field(None, title="ClinVar GeneDx")

    # Field/column number 48
    clinvar_natera: Optional[ClinvarSignificanceEnum] = Field(None, title="ClinVar Natera")

    # Field/column number 49
    cadd_phred_score: Optional[Union[str, float]] = Field(None, title="CAAD_phred_score")

    # Field/column number 50
    spliceai_score: Optional[str] = Field(None, title="SpliceAI Score (position, type)")

    # Field/column number 51
    exon_number: Optional[str] = Field(None, title="Exon Number (Total Exons)")

    # Field/column number 52
    fs_value: Optional[str] = Field(None, title="FS Value")

    # Field/column number 53
    hgmd_class: Optional[HGMDClassEnum] = Field(None, title="HGMD Class")

    # Field/column number 54
    hgmd_id: Optional[str] = Field(None, title="HGMD ID")

    # Field/column number 55
    hgmd_phen: Optional[str] = Field(None, title="HGMD Phen")

    # Field/column number 56
    hgmd_pmid: Optional[str] = Field(None, title="HGMD PMID")

    # Field/column number 57
    mut_type: Optional[MutationTypeEnum] = Field(None, title="Mutation Type")

    # Field/column number 58
    bam_link: Optional[str] = Field(None, title="BAM Link")

    # Field/column number 59
    igv_link: Optional[str] = Field(None, title="IGV Link")

    # Field/column number 60
    proximal: Optional[str] = Field(None, title="Proximal")


    @field_validator('lab_number')
    def is_lab_number_valid(cls, v):
        if not (1000000 <= v <= 9999999):
            raise ValueError('lab_number must be a 7-digit integer')
        return v

    @field_validator('gene')
    def is_gene_valid(cls, v):
        if not v.isupper():
            raise ValueError('gene must be uppercase')
        if not len(v) >= DEFAULT_MIN_GENE_NAME_LENGTH:
            raise ValueError('gene must be at least 3 characters long')
        if not len(v) <= DEFAULT_MAX_GENE_NAME_LENGTH:
            raise ValueError('gene must be less than 10 characters long')
        if not v.isalpha():
            raise ValueError('gene must be alphabetic')
        return v

    @field_validator('mutation')
    def is_mutation_valid(cls, v):
        if DEFAULT_MIN_MUTATION_LENGTH < v < DEFAULT_MAX_MUTATION_LENGTH:
            return v
        raise ValueError(f"The mutation string '{v}' must be between {DEFAULT_MIN_MUTATION_LENGTH} and {DEFAULT_MAX_MUTATION_LENGTH} characters long")

    @field_validator('disease')
    def is_disease_valid(cls, v):
        if DEFAULT_MIN_DISEASE_LENGTH < v < DEFAULT_MAX_DISEASE_LENGTH:
            return v
        raise ValueError(f"The disease string '{v}' must be between {DEFAULT_MIN_DISEASE_LENGTH} and {DEFAULT_MAX_DISEASE_LENGTH} characters long")

    @field_validator('vcf')
    def is_vcf_valid(cls, v):
        parts = v.split('_')
        if parts[0] == "X" or 0 < int(parts[0]) < 24:
            pass
        else:
            raise ValueError('vcf must start with X or a number between 1 and 23')

        try:
            int(parts[1])
        except ValueError:
            raise ValueError('vcf must have a second part that is an integer')

        if not parts[2] or not all(c in 'ATCG' for c in parts[2]):
            raise ValueError('vcf must have a third part that is at least one character long and can only contain A, T, C, G')

        if not parts[3] or not all(c in 'ATCG' for c in parts[2]):
            raise ValueError('vcf must have a third part that is at least one character long and can only contain A, T, C, G')

        return v

    @field_validator('interpretation')
    def is_interpretation_valid(cls, v):
        if DEFAULT_INTERPRETATION_MIN_LENGTH < v < DEFAULT_INTERPRETATION_MAX_LENGTH:
            return v
        raise ValueError(f"interpretation string '{v}' must be between {DEFAULT_INTERPRETATION_MIN_LENGTH} and {DEFAULT_INTERPRETATION_MAX_LENGTH} characters long")

    @field_validator('source')
    def is_source_valid(cls, v):
        if DEFAULT_SOURCE_MIN_LENGTH < v < DEFAULT_SOURCE_MAX_LENGTH:
            return v
        raise ValueError(f"source string '{v}' must be between {DEFAULT_SOURCE_MIN_LENGTH} and {DEFAULT_SOURCE_MAX_LENGTH} characters long")


    @field_validator('link')
    def is_link_valid(cls, v):
        if not v.startswith(DEFAULT_LINK_PREFIX):
            raise ValueError(f"link must start with {DEFAULT_LINK_PREFIX}")
        if not v.endswith(DEFAULT_LINK_SUFFIX):
            raise ValueError(f"link must end with {DEFAULT_LINK_SUFFIX}")
        return v

    @field_validator('quality')
    def is_quality_valid(cls, v):
        try:
            return float(v)
        except ValueError:
            if v == "na":
                return v
            raise ValueError('quality must be a float')

    @field_validator('format')
    def is_format_valid(cls, v):
        # TODO: Need to implement validation for this field
        return v

    @field_validator('mRNA')
    def is_mRNA_valid(cls, v):
        if not v.startswith('NM_'):
            raise ValueError('mRNA must start with NM_')
        if not v[-1].isdigit():
            raise ValueError('mRNA must end with an integer value')
        return v

    @field_validator('gnomad_het_ac')
    def is_gnomad_het_ac_valid(cls, v):
        try:
            return int(v)
        except ValueError:
            if v == "na":
                return v
            raise ValueError('gnomad_het_ac must be an integer')

    @field_validator('gnomad_homo_ac')
    def is_gnomad_homo_ac_valid(cls, v):
        try:
            return int(v)
        except ValueError:
            if v == "na":
                return v
            raise ValueError('gnomad_homo_ac must be an integer')

    @field_validator('gnomad_popmax_af')
    def is_gnomad_popmax_af_valid(cls, v):
        try:
            return float(v)
        except ValueError:
            if v == "na":
                return v
            raise ValueError('gnomad_popmax_af must be an float')

    @field_validator('gnomad_overall_af')
    def is_gnomad_overall_af_valid(cls, v):
        try:
            return float(v)
        except ValueError:
            if v == "na":
                return v
            raise ValueError('gnomad_overall_af must be an float')

    @field_validator('clinvar_id')
    def is_clinvar_id_valid(cls, v):
        if not v.startswith(DEFAULT_CLINVAR_ID_PREFIX):
            raise ValueError(f"clinvar_id must start with {DEFAULT_CLINVAR_ID_PREFIX}")
        return v

    @field_validator("spliceai_score")
    def is_spliceai_score_valid(cls, v):
        if v == "na":
            return v
        parts = v.split("(")
        try:
            float(parts[0])
        except ValueError:
            raise ValueError('First part of spliceai_score must be an float')

        position, type = parts[1].split(",")
        if type.endswith(")"):
            type = type[:-1]

        try:
            int(position)
        except ValueError:
            raise ValueError('Second part of spliceai_score must be an integer')

        if type not in ("dg", "al", "ag"):
            raise ValueError(f"type part of spliceai_score must be one of dg, al, ag - not {type}")

        return v

    @field_validator("exon_number")
    def is_exon_number_valid(cls, v):
        if v == "na":
            return v

        if v == ".(.)":
            return v

        parts = v.split("(")

        try:
            int(parts[0])
        except ValueError:
            raise ValueError(f"First part of exon_number must be an integer - not {parts[0]}")

        total_exons = parts[1][:-1]

        try:
            int(total_exons)
        except ValueError:
            raise ValueError(f"Second part of exon_number must be an integer - not {total_exons}")

        return v


    @field_validator("fs_value")
    def is_fs_value_valid(cls, v):
        if v == "na":
            return v

        if v == ".":
            return v

        try:
            return float(v)
        except ValueError:
            raise ValueError('fs_value must be a float')

    @field_validator("hgmd_id")
    def is_hgmd_id_valid(cls, v):
        if v == "na":
            return v

        if v == ".":
            return v

        prefixes = ("CM", "CD", "CI", "CS", "CR", "CG", "CR", "HM")

        for prefix in prefixes:
            if v.startswith(prefix):
                val = v.replace(prefix, "")
                try:
                    int(val)
                    break
                except ValueError:
                    raise ValueError(f"The second portion of hgmd_id that begins with {prefix} must be an integer - not {val}")

        return v

    @field_validator("hgmd_phen")
    def is_hgmd_phen_valid(cls, v):
        if v == ".":
            return v

        if DEFAULT_HGMD_PHEN_MIN_LENGTH < v < DEFAULT_HGMD_PHEN_MAX_LENGTH:
            return v
        raise ValueError(f"The hgmd_phen string '{v}' must be between {DEFAULT_HGMD_PHEN_MIN_LENGTH} and {DEFAULT_HGMD_PHEN_MAX_LENGTH} characters long")

    @field_validator("hgmd_pmid")
    def is_hgmd_pmid_valid(cls, v):
        if v == ".":
            return v

        if v == "na":
            return v

        if DEFAULT_HGMD_PMID_MIN_LENGTH < v < DEFAULT_HGMD_PMID_MAX_LENGTH:
            return v
        raise ValueError(f"The hgmd_pmid string '{v}' must be between {DEFAULT_HGMD_PMID_MIN_LENGTH} and {DEFAULT_HGMD_PMID_MAX_LENGTH} characters long")

    @field_validator('bam_link')
    def is_bam_link_valid(cls, v):
        if not v.startswith(DEFAULT_BAM_LINK_PREFIX):
            raise ValueError(f"bam_link must start with {DEFAULT_BAM_LINK_PREFIX}")
        return v

    @field_validator('igv_link')
    def is_igv_link_valid(cls, v):
        if not v.startswith(DEFAULT_IGV_LINK_PREFIX):
            raise ValueError(f"igv_link must start with {DEFAULT_IGV_LINK_PREFIX}")
        return v
