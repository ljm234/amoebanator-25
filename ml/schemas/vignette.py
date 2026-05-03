"""Pydantic v2 vignette schema for 9-class meningitis/encephalitis differential
diagnosis (Amoebanator V1.0).

Schema version: 2.0
Date frozen: 2026-05-02
Target: 270-vignette corpus for Phase 1 sprint, UPCH-aligned, bilingual ES/EN.

Every numeric range and every enum is justified by at least one peer-reviewed
citation in the field docstring. Cross-field validators enforce class-conditional
requirements (e.g., PAM always-flag rule per CDC 2017 case definition).

Citations summary:
    Bacterial meningitis: IDSA Tunkel 2004 (doi:10.1086/425368)
    Encephalitis: IDSA Tunkel 2008 (doi:10.1086/589747)
    PAM: CDC PAM 2017 case definition; MMWR 2025 (PMID 40146665)
    TB meningitis: Marais Lancet ID 2010; Ye TM&IH 2023 (doi:10.1111/tmi.13849)
    Cryptococcal: Ford CID 2018 (PMC5850628); NIH OI guidelines
    GAE/Balamuthia: Bravo PMC8760460; Gotuzzo OFID 2026 (doi:10.1093/ofid/ofaf695.345)
    NCC: Del Brutto 2017 (PMID 28017213); Allen Pathogens 2023
    Inter-rater: Cohen 1960; Landis & Koch 1977; McHugh 2012 (PMC3900052)
"""
from __future__ import annotations
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from ml.schemas.labels import ClassLabel


# ============================================================================
# Demographics sub-model
# ============================================================================
class Demographics(BaseModel):
    """Demographic context for vignette.

    Citations:
        - PAM bimodal age: Gharpure et al. CID 2021 (PMID 32369575)
        - NMDAR sex distribution: Graus Lancet Neurol 2016 (doi:10.1016/S1474-4422(15)00401-9)
        - HACE altitude threshold: Wilderness Medical Society 2024 (PMID 37833187)
        - Peru regional epidemiology: MMWR 2024-2025; Allen Pathogens 2023
    """
    model_config = ConfigDict(extra="forbid")

    age_years: int = Field(
        ..., ge=0, le=110,
        description="Age in years. PAM bimodal (median ~14 y, Gharpure CID 2021); "
                    "HSV-1 bimodal <20 / >50; NCC 20-40 in endemic regions.",
    )
    sex: Literal["male", "female", "intersex"] = Field(
        ...,
        description="Biological sex. PAM ~75% male (recreational water exposure pattern, "
                    "Gharpure 2021); NMDAR ~80% female (Graus 2016).",
    )
    ethnicity: Optional[Literal[
        "hispanic_latino",
        "indigenous_andean",
        "mestizo",
        "afro_peruvian",
        "asian",
        "white_non_hispanic",
        "other",
        "unknown",
    ]] = Field(
        None,
        description="Self-identified ethnicity. Hispanic/mestizo overrepresentation in "
                    "Balamuthia documented in Latin American series (Bravo PMC8760460).",
    )
    geography_region: Literal[
        "peru_lima_coast",
        "peru_loreto_amazon",
        "peru_cusco_altitude",
        "peru_puno_altitude",
        "peru_tumbes",
        "peru_madre_de_dios",
        "us_south",
        "pakistan_karachi",
        "other_latam",
        "other_global",
    ] = Field(
        ...,
        description="Geographic region. Maps to disease epidemiology: Loreto/Madre de Dios "
                    "to arboviral/malaria; Cusco/Puno >3000m to HACE; Tumbes to NCC endemic; "
                    "coastal Peru to Balamuthia; US South to PAM; Karachi to ablution-PAM.",
    )
    altitude_residence_m: Optional[int] = Field(
        None, ge=0, le=5000,
        description="Altitude of residence in meters. HACE risk threshold >2,500 m "
                    "(WMS 2024 PMID 37833187). Cusco 3,399 m; Puno 3,827 m.",
    )


# ============================================================================
# History sub-model
# ============================================================================
class History(BaseModel):
    """History of present illness.

    Citations:
        - PAM time course: MMWR 2025 (PMID 40146665) - 1-12 days, median 5
        - TB time course: Huynh Lancet Neurol 2022
        - Cryptococcal subacute: NIH OI cryptococcosis
    """
    model_config = ConfigDict(extra="forbid")

    symptom_onset_to_presentation_days: float = Field(
        ..., ge=0, le=180,
        description="Days from symptom onset to presentation. PAM 1-12 d; bacterial 1-3 d; "
                    "viral days-week; TB 14-56 d; cryptococcal 7-84 d (subacute).",
    )
    chief_complaint: Literal[
        "headache",
        "fever_with_headache",
        "altered_mental_status",
        "seizure",
        "focal_deficit",
        "neck_stiffness",
        "vomiting",
        "behavioral_change",
        "thunderclap_headache",
        "gait_ataxia",
    ] = Field(
        ...,
        description="Primary chief complaint. Thunderclap to SAH/RCVS; gait ataxia + altitude "
                    "to HACE; behavioral change + dyskinesia to NMDAR (Graus 2016).",
    )
    prodrome_description: Optional[str] = Field(
        None, max_length=500,
        description="Free-text prodrome description (e.g., genital lesions before HSV-2 "
                    "meningitis, AMS prodrome before HACE, viral URI before enteroviral).",
    )
    red_flags_present: List[Literal[
        "immunocompromise",
        "recent_neurosurgery",
        "fresh_water_exposure_14d",
        "high_altitude_ascent_7d",
        "pregnancy_postpartum",
        "sah_thunderclap_history",
        "animal_bite",
        "taenia_household_contact",
    ]] = Field(
        default_factory=list,
        description="Clinical red flags requiring specific diagnostic consideration "
                    "per IDSA/CDC guidance.",
    )


# ============================================================================
# ExposureHistory sub-model
# ============================================================================
class ExposureHistory(BaseModel):
    """Exposure history including PAM always-flag fields.

    Citations:
        - CDC PAM 2017 case definition (ndc.services.cdc.gov)
        - MMWR 2025 splash pad (PMID 40146665)
        - Karachi ablution-PAM: PMC10620794
        - WMS 2024 HACE (PMID 37833187)
        - Del Brutto 2017 NCC criteria (PMID 28017213)
        - Ford CID 2018 cryptococcal CD4 threshold (PMC5850628)
    """
    model_config = ConfigDict(extra="forbid")

    freshwater_exposure_within_14d: bool = Field(
        ...,
        description="CRITICAL FIELD for PAM always-flag rule (CDC 2017 case definition). "
                    "True if patient had recreational freshwater exposure or nasal "
                    "irrigation/ablution within 14 days before symptom onset.",
    )
    freshwater_exposure_type: Optional[Literal[
        "lake",
        "river",
        "hot_spring",
        "splash_pad",
        "swimming_pool_unchlorinated",
        "neti_pot_tap_water",
        "ritual_ablution_wudu",
        "none",
    ]] = Field(
        None,
        description="Type of freshwater exposure. Splash pad documented in MMWR 2025 "
                    "(Arkansas case PMID 40146665). Ablution dominant in Karachi.",
    )
    altitude_exposure_within_7d_m: Optional[int] = Field(
        None, ge=0, le=6000,
        description="Maximum altitude reached in past 7 days, in meters. HACE risk "
                    "begins ~2,500 m; serious risk >3,500 m (WMS 2024 PMID 37833187).",
    )
    pork_consumption_or_taenia_contact: Optional[bool] = Field(
        None,
        description="Pork consumption or household Taenia contact. Minor epidemiologic "
                    "criterion in Del Brutto 2017 NCC. Tumbes Peru cohort 38% NCC.",
    )
    mosquito_endemic_area_exposure: Optional[bool] = Field(
        None,
        description="Mosquito-endemic area exposure (Aedes for dengue, Anopheles for "
                    "P. falciparum). Loreto/Madre de Dios documented hot zones.",
    )
    immunocompromise_status: Literal[
        "none",
        "hiv_cd4_under100",
        "hiv_cd4_100_200",
        "hiv_cd4_over200",
        "transplant_solid_organ",
        "transplant_hsct",
        "malignancy_active",
        "immunosuppressive_drugs",
        "diabetes",
        "unknown",
    ] = Field(
        ...,
        description="Immunocompromise status. CD4<100 to cryptococcal screening threshold "
                    "(Ford CID 2018 PMC5850628). HSCT to highest Acanthamoeba GAE risk.",
    )
    hiv_status: Literal[
        "positive_on_art",
        "positive_not_on_art",
        "negative",
        "unknown",
    ] = Field(
        ...,
        description="HIV status. Independent of CD4 absolute count for class-conditional "
                    "validation (NIH OI guidelines).",
    )
    cd4_count_cells_per_uL: Optional[int] = Field(
        None, ge=0, le=2000,
        description="CD4 count cells/uL. Required when HIV+ for cryptococcal disease "
                    "diagnosis (Ford CID 2018; <100 = high CrAg risk).",
    )

    @model_validator(mode="after")
    def _freshwater_type_requires_exposure(self):
        """If freshwater_exposure_within_14d=True, freshwater_exposure_type must be set
        per CDC PAM 2017 case definition."""
        if self.freshwater_exposure_within_14d and self.freshwater_exposure_type is None:
            raise ValueError(
                "freshwater_exposure_type required when "
                "freshwater_exposure_within_14d is True (CDC PAM 2017 case definition)."
            )
        return self


# ============================================================================
# VitalSigns sub-model
# ============================================================================
class VitalSigns(BaseModel):
    """Vital signs at presentation.

    Citations:
        - GCS: Teasdale & Jennett Lancet 1974
        - Sepsis-3 criteria: Singer JAMA 2016
        - WHO cerebral malaria GCS<11: WHO 2023 Malaria Guidelines
        - PRES BP: Hinchey NEJM 1996
    """
    model_config = ConfigDict(extra="forbid")

    temperature_celsius: float = Field(
        ..., ge=34.0, le=42.5,
        description="Body temperature in Celsius. Fever >38C supports infection. "
                    "Afebrile coma possible in cerebral malaria.",
    )
    heart_rate_bpm: int = Field(
        ..., ge=30, le=220,
        description="Heart rate in beats per minute. Tachycardia plus hypotension "
                    "supports septic shock (Sepsis-3, Singer JAMA 2016).",
    )
    systolic_bp_mmHg: int = Field(
        ..., ge=50, le=260,
        description="Systolic blood pressure mmHg. Severe HTN >180 supports PRES "
                    "(Hinchey NEJM 1996); SBP<90 with shock supports meningococcal "
                    "Waterhouse-Friderichsen.",
    )
    diastolic_bp_mmHg: int = Field(
        ..., ge=30, le=160,
        description="Diastolic blood pressure mmHg.",
    )
    glasgow_coma_scale: int = Field(
        ..., ge=3, le=15,
        description="Glasgow Coma Scale 3-15. Severe <=8; cerebral malaria <11 per WHO. "
                    "Teasdale & Jennett Lancet 1974.",
    )
    oxygen_saturation_pct: Optional[int] = Field(
        None, ge=50, le=100,
        description="SpO2 percent. HAPE coexistent with HACE if SpO2<85% at altitude.",
    )
    respiratory_rate_breaths_per_min: int = Field(
        ..., ge=6, le=60,
        description="Respiratory rate breaths/min. RR>30 plus altered MS in WHO severe "
                    "malaria criteria.",
    )


# ============================================================================
# PhysicalExam sub-model
# ============================================================================
class PhysicalExam(BaseModel):
    """Physical examination findings.

    Citations:
        - IDSA bacterial meningitis 2004 (van de Beek triad)
        - IDSA encephalitis 2008
        - Bravo PMC8760460 (centrofacial Balamuthia 73%)
        - StatPearls Meningococcal NBK549849 (petechiae 62-81%)
        - Lancet Neurol Huynh 2022 (CN VI in TB ~30%)
    """
    model_config = ConfigDict(extra="forbid")

    mental_status_grade: Literal[
        "alert",
        "confused",
        "somnolent",
        "stuporous",
        "comatose",
    ] = Field(
        ...,
        description="Categorical mental status. Required for IDSA encephalitis case "
                    "definition (Tunkel 2008): altered MS, behavioral change, seizure, focal.",
    )
    neck_stiffness: bool = Field(
        ...,
        description="Neck stiffness (meningismus). Triad sensitivity 44% in bacterial "
                    "meningitis (van de Beek NEJM 2004).",
    )
    kernig_or_brudzinski_positive: Optional[bool] = Field(
        None,
        description="Kernig and/or Brudzinski sign. Low sensitivity (~5% individually) "
                    "but high specificity for meningeal irritation (Thomas CID 2002).",
    )
    focal_neurological_deficit: bool = Field(
        ...,
        description="Focal neurological deficit. Raises probability of HSV-1, TB "
                    "(CN palsy 30%), NCC, GAE, SAH; rare in pure aseptic meningitis.",
    )
    cranial_nerve_palsy: Literal[
        "none",
        "CN_VI",
        "CN_III",
        "CN_VII",
        "multiple",
        "other",
    ] = Field(
        "none",
        description="Cranial nerve palsy. CN VI palsy in ~30% of TB meningitis "
                    "(basilar exudate, Lancet Neurol Huynh 2022).",
    )
    skin_lesion_centrofacial_chronic: Optional[bool] = Field(
        None,
        description="Centrofacial skin lesion preceding CNS by months. 73% of Peruvian "
                    "Balamuthia cases (Bravo PMC8760460); median 15 months pre-CNS.",
    )
    petechial_or_purpuric_rash: bool = Field(
        ...,
        description="Petechial or purpuric rash. 62-81% in meningococcal meningitis "
                    "(van de Beek 2008); rapidly evolving suggests purpura fulminans.",
    )
    papilledema_on_fundoscopy: Optional[bool] = Field(
        None,
        description="Papilledema. Suggests elevated ICP: cryptococcal (60-80% with "
                    "OP>=25), TB hydrocephalus, PRES, SAH, severe NCC.",
    )


# ============================================================================
# Labs sub-model
# ============================================================================
class Labs(BaseModel):
    """Peripheral lab values.

    Citations:
        - IDSA Tunkel 2004 (bacterial WBC patterns)
        - WHO Dengue Guidelines 2023 (platelet thresholds)
        - Sormunen Pediatrics 1999 (CRP>40 favors bacterial)
        - Vikse 2015 meta-analysis (procalcitonin)
        - AAFP Hyponatremia 2015 (Na<125 severe)
        - Marais Lancet ID 2010 (TB SIADH)
    """
    model_config = ConfigDict(extra="forbid")

    wbc_blood_per_uL: int = Field(
        ..., ge=100, le=80000,
        description="Peripheral WBC count cells/uL. Leukocytosis supports bacterial "
                    "sepsis; lymphopenia in severe dengue/malaria.",
    )
    platelets_per_uL: int = Field(
        ..., ge=5000, le=800000,
        description="Platelet count cells/uL. <100k strongly supports dengue/severe "
                    "malaria; DIC in meningococcal.",
    )
    alt_ast_U_per_L: Optional[int] = Field(
        None, ge=5, le=10000,
        description="ALT/AST U/L. Elevation in dengue (>1000 = severe dengue criterion), "
                    "Plasmodium hepatic involvement.",
    )
    crp_mg_per_L: Optional[float] = Field(
        None, ge=0, le=500,
        description="C-reactive protein mg/L. >40 mg/L favors bacterial over viral "
                    "(Sormunen Pediatrics 1999).",
    )
    procalcitonin_ng_per_mL: Optional[float] = Field(
        None, ge=0, le=200,
        description="Procalcitonin ng/mL. >0.5 ng/mL favors bacterial (Vikse 2015 meta).",
    )
    serum_sodium_mEq_per_L: int = Field(
        ..., ge=100, le=170,
        description="Serum sodium mEq/L. <125 = severe symptomatic hyponatremia "
                    "(non-infectious mimic class); SIADH common in TB meningitis.",
    )


# ============================================================================
# CSFProfile sub-model — diagnostic core
# ============================================================================
class CSFProfile(BaseModel):
    """CSF analysis results — the primary diagnostic discriminator across 9 classes.

    Citations:
        - IDSA Tunkel 2004 (bacterial cutoffs from van de Beek 422-pt analysis)
        - Huynh Lancet Neurol 2022 (TB CSF patterns)
        - NIH OI cryptococcosis (OP>=25 in 60-80%)
        - Ye TM&IH 2023 doi:10.1111/tmi.13849 (ADA cutoff 10 U/L)
        - Prasad Cureus 2023 doi:10.7759/cureus.39896 (ADA confirmation)
        - Williams CID 2015 (CrAg LFA near-100% sensitivity)
        - StatPearls NBK535447 (PAM wet mount diagnosis)
        - Perry BMJ 2015 PMID 25739953 (xanthochromia + RBC for SAH)
        - Sakushima J Infect 2011 (lactate>3.5 favors bacterial)
        - Del Brutto 2017 (eosinophilic CSF in racemose NCC)
    """
    model_config = ConfigDict(extra="forbid")

    opening_pressure_cmH2O: float = Field(
        ..., ge=5, le=60,
        description="Opening pressure cmH2O. >=25 cmH2O in 60-80% of HIV-cryptococcal "
                    "(NIH OI guidelines, AMBITION-cm); >=30 = therapeutic LP trigger.",
    )
    csf_wbc_per_mm3: int = Field(
        ..., ge=0, le=50000,
        description="CSF white blood cell count per mm3. PAM 1k-30k neutrophilic; "
                    "bacterial 1k-5k neutrophilic; viral 50-1k lymphocytic; TB 100-500 "
                    "lymphocytic. IDSA Tunkel 2004.",
    )
    csf_neutrophil_pct: int = Field(
        ..., ge=0, le=100,
        description="CSF neutrophil percentage. Bacterial 80-95% neutrophilic; PAM "
                    "neutrophilic; viral/TB/fungal lymphocytic.",
    )
    csf_lymphocyte_pct: int = Field(
        ..., ge=0, le=100,
        description="CSF lymphocyte percentage. Required complement to neutrophil%; "
                    "sum-to-100 validator with eosinophil%.",
    )
    csf_eosinophil_pct: int = Field(
        0, ge=0, le=100,
        description="CSF eosinophil percentage. >10% suggests parasitic - racemose NCC, "
                    "Angiostrongylus, schistosomiasis (Del Brutto 2017).",
    )
    csf_glucose_mg_per_dL: int = Field(
        ..., ge=0, le=200,
        description="CSF glucose mg/dL. <34 mg/dL or CSF:serum <0.23 = >=99% specific "
                    "for bacterial vs viral (IDSA Tunkel 2004).",
    )
    csf_protein_mg_per_dL: int = Field(
        ..., ge=5, le=3000,
        description="CSF protein mg/dL. Bacterial often >220 (>=99% specific cutoff); "
                    "TB typically 100-500; viral <=150.",
    )
    csf_lactate_mmol_per_L: Optional[float] = Field(
        None, ge=0.5, le=20,
        description="CSF lactate mmol/L. >3.5 favors bacterial; <3.5 viral. Confounded "
                    "by post-antibiotic exposure (Sakushima 2011).",
    )
    csf_ada_U_per_L: Optional[float] = Field(
        None, ge=0, le=100,
        description="CSF adenosine deaminase U/L. >=10 U/L = optimal cutoff for TB "
                    "meningitis (Ye TM&IH 2023; Prasad Cureus 2023; AUC 0.94).",
    )
    csf_crag_lfa_result: Optional[Literal[
        "positive",
        "negative",
        "not_done",
    ]] = Field(
        "not_done",
        description="CSF cryptococcal antigen lateral flow assay. Near-100% sensitivity "
                    "in HIV-cryptococcal (Williams CID 2015).",
    )
    csf_wet_mount_motile_amoebae: Optional[Literal[
        "positive",
        "negative",
        "not_done",
    ]] = Field(
        "not_done",
        description="CSF wet mount for motile trophozoites. N. fowleri commonly visible "
                    "(unlike Balamuthia/Acanthamoeba). CDC: Gram stain destroys organism.",
    )
    csf_xanthochromia_present: Optional[bool] = Field(
        None,
        description="CSF xanthochromia. Present ~100% at 12h post-bleed (SAH). "
                    "Perry BMJ 2015 PMID 25739953.",
    )
    csf_rbc_per_mm3: Optional[int] = Field(
        None, ge=0, le=1_000_000,
        description="CSF red blood cell count per mm3. >2000 non-decreasing across "
                    "tubes plus xanthochromia = SAH.",
    )
    csf_rbc_decreasing_across_tubes: Optional[bool] = Field(
        None,
        description="RBC count decreasing tube 1 to 4 = traumatic tap; non-decreasing "
                    "with xanthochromia = SAH.",
    )

    @model_validator(mode="after")
    def _csf_differential_sums_to_100(self):
        """CSF WBC differential percentages must sum to ~100% (allow +/-2 rounding)
        when CSF is cellular (WBC>5/mm3). IDSA Tunkel 2004 reference standard."""
        total = (
            self.csf_neutrophil_pct
            + self.csf_lymphocyte_pct
            + self.csf_eosinophil_pct
        )
        if self.csf_wbc_per_mm3 > 5 and not (98 <= total <= 102):
            raise ValueError(
                f"CSF WBC differential percentages must sum to ~100% when "
                f"WBC>5/mm3 (got neutrophil={self.csf_neutrophil_pct}, "
                f"lymphocyte={self.csf_lymphocyte_pct}, eosinophil="
                f"{self.csf_eosinophil_pct}, total={total}). "
                f"IDSA Tunkel 2004 reference standard."
            )
        return self


# ============================================================================
# Imaging sub-model
# ============================================================================
class Imaging(BaseModel):
    """Neuroimaging findings.

    Citations:
        - IDSA Tunkel 2008 (MRI preferred for encephalitis)
        - Del Brutto 2017 NCC (scolex within cyst absolute criterion)
        - StatPearls NBK557643 (HSV-1 mesial temporal FLAIR >90% MRI)
        - Lancet Neurol Huynh 2022 (TB basal meningeal enhancement)
        - Hinchey NEJM 1996 (PRES parieto-occipital)
        - Hackett HAH 1998 (HACE microhemorrhages)
    """
    model_config = ConfigDict(extra="forbid")

    imaging_modality: Literal[
        "none",
        "ct_noncontrast",
        "ct_contrast",
        "mri_noncontrast",
        "mri_contrast",
        "mri_with_dwi_flair",
    ] = Field(
        ...,
        description="Imaging modality. MRI with FLAIR/DWI preferred per IDSA 2008 "
                    "encephalitis; CT first-line for SAH (~99% sensitivity <6h).",
    )
    imaging_pattern: Optional[Literal[
        "normal",
        "mesial_temporal_t2_flair_hyperintensity",
        "basal_meningeal_enhancement_with_hydrocephalus",
        "dilated_virchow_robin_with_pseudocysts",
        "multiple_ring_enhancing_lesions",
        "cysticercosis_cysts_with_scolex",
        "calcified_cysts",
        "parenchymal_calcifications_no_cyst",
        "diffuse_cerebral_edema_basilar_meningeal_enhancement",
        "brain_swelling_arboviral",
        "vasogenic_edema_microhemorrhages",
        "basal_cistern_hyperdensity",
        "parieto_occipital_vasogenic_edema",
        "segmental_vasoconstriction",
    ]] = Field(
        None,
        description="Class-discriminative imaging pattern. HSV-1: mesial-temporal FLAIR. "
                    "TB: basal meningeal enhancement + hydrocephalus. Cryptococcal: "
                    "dilated VR spaces. Balamuthia/GAE: multiple ring-enhancing. NCC: "
                    "cysts +/- scolex (Del Brutto 2017). PAM: cerebral edema. HACE: "
                    "vasogenic edema + microhemorrhages. SAH: hyperdense basal cisterns. "
                    "PRES: parieto-occipital edema. RCVS: segmental vasoconstriction.",
    )
    imaging_finding_count: Optional[int] = Field(
        None, ge=0, le=50,
        description="Number/staging of lesions. Supports NCC staging (vesicular/colloidal/"
                    "granular nodular/calcified per Del Brutto) and GAE multifocality.",
    )
    imaging_text_summary: Optional[str] = Field(
        None, max_length=1000,
        description="Free-text radiologist impression for adjudicator context.",
    )


# ============================================================================
# DiagnosticTests sub-model (with nested DxResult)
# ============================================================================
class DxResult(BaseModel):
    """Single diagnostic test result with sensitivity/specificity attribution."""
    model_config = ConfigDict(extra="forbid")

    test_name: str = Field(..., min_length=1, max_length=200)
    result: str = Field(..., min_length=1, max_length=500)
    sensitivity_pct: Optional[float] = Field(None, ge=0, le=100)
    specificity_pct: Optional[float] = Field(None, ge=0, le=100)
    citation_pmid_or_doi: str = Field(..., min_length=1, max_length=200)


class DiagnosticTests(BaseModel):
    """Diagnostic test results array.

    Includes Gram stain, blood/CSF cultures, HSV-1/enterovirus PCR, FilmArray ME panel
    (sensitivity 90% / specificity 97% pooled meta-analysis, PMID 31760115),
    Xpert MTB/RIF (85%/98% Hernandez TM&IH 2021), Xpert Ultra (Cresswell CID 2020),
    EITB cysticercosis (~98% >=2 viable cysts, Tsang 1989), Balamuthia IFA, brain
    biopsy histology, malaria thick/thin smear, dengue NS1, mNGS for free-living amebae.
    """
    model_config = ConfigDict(extra="forbid")

    results: List[DxResult] = Field(default_factory=list)


# ============================================================================
# AdjudicationMetadata sub-model
# ============================================================================
class AdjudicationMetadata(BaseModel):
    """Physician adjudication metadata for vignette inclusion in corpus.

    Citations:
        - Cohen 1960 (original kappa coefficient)
        - Landis & Koch 1977 (substantial agreement >=0.61 threshold)
        - McHugh 2012 PMC3900052 (>=0.7 preferred for clinical/high-stakes)
        - Cochrane handbook for systematic reviews (disagreement resolution)
    """
    model_config = ConfigDict(extra="forbid")

    adjudicator_ids: List[str] = Field(
        ..., min_length=2,
        description="Adjudicator unique identifiers. Minimum 2 required for inter-rater "
                    "reliability calculation per Cohen 1960; McHugh 2012 PMC3900052.",
    )
    cohen_kappa: float = Field(
        ..., ge=0.0, le=1.0,
        description="Cohen's kappa coefficient. Inclusion threshold >=0.61 (Landis & Koch "
                    "1977 'substantial'); >=0.7 preferred for clinical (McHugh 2012).",
    )
    disagreement_resolution: Optional[Literal[
        "consensus_discussion",
        "third_adjudicator",
        "excluded",
    ]] = Field(
        None,
        description="Pre-registered disagreement resolution protocol per Cochrane handbook "
                    "for systematic reviews adapted to vignette QA.",
    )
    anchoring_documentation: str = Field(
        ..., min_length=1, max_length=2000,
        description="Free text linking vignette to source paper(s) used as clinical anchor.",
    )
    inclusion_decision: Literal[
        "include",
        "exclude",
        "hold_for_revision",
    ] = Field(
        ...,
        description="Final inclusion decision after adjudication.",
    )


# ============================================================================
# LiteratureAnchor sub-model
# ============================================================================
class LiteratureAnchor(BaseModel):
    """Peer-reviewed literature anchor for vignette clinical fidelity.

    Citations:
        - PMID format spec (NLM PubMed)
        - DOI format spec (ISO 26324:2022)
    """
    model_config = ConfigDict(extra="forbid")

    anchor_type: Literal[
        "case_report",
        "guideline",
        "review",
        "surveillance",
        "meta_analysis",
        "cohort",
        "rct",
        "prospective_observational",
    ] = Field(
        ...,
        description="Type of literature anchor. Used by adjudicators to weight clinical "
                    "fidelity (case_report < cohort < meta_analysis < rct).",
    )
    pmid: Optional[str] = Field(
        None, pattern=r"^\d{7,9}$",
        description="PubMed ID (7-9 digits). At least one of pmid or doi required.",
    )
    doi: Optional[str] = Field(
        None, pattern=r"^10\.\d{4,9}/.+$",
        description="Digital Object Identifier. At least one of pmid or doi required.",
    )

    @model_validator(mode="after")
    def _at_least_one_id(self):
        """At least one of pmid or doi must be non-None for citation traceability."""
        if self.pmid is None and self.doi is None:
            raise ValueError(
                "LiteratureAnchor requires at least one of pmid or doi for citation "
                "traceability (cannot have both as None)."
            )
        return self


# ============================================================================
# Provenance sub-model
# ============================================================================
class Provenance(BaseModel):
    """Vignette generation provenance for audit trail and reproducibility.

    Citations:
        - Mitchell et al. 2019 (Model Cards framework, doi:10.1145/3287560.3287596)
        - FAIR data principles 2016
        - SHA-256 spec (NIST FIPS 180-4)
    """
    model_config = ConfigDict(extra="forbid")

    generation_timestamp_utc: datetime = Field(
        ...,
        description="ISO-8601 UTC timestamp of vignette generation. Required for "
                    "reproducibility audit per FAIR principles.",
    )
    generator_model_identifier: str = Field(
        ..., min_length=1, max_length=200,
        description="Model identifier string used for generation (e.g., "
                    "'claude-sonnet-4.5/2026-04-15' or 'manual-fixture-2026-05-02').",
    )
    prompt_hash_sha256: str = Field(
        ..., pattern=r"^[a-f0-9]{64}$",
        description="SHA-256 hash of generation prompt. NIST FIPS 180-4 spec; "
                    "64 lowercase hex characters.",
    )
    schema_version: Literal["2.0"] = Field(
        ...,
        description="Schema version for migration management. Locked to '2.0'.",
    )
    inclusion_decision_rationale: str = Field(
        ..., max_length=1000,
        description="Free-text rationale for inclusion decision; readable by adjudicators.",
    )


# ============================================================================
# VignetteSchema — top-level container with class-conditional validators
# ============================================================================
class VignetteSchema(BaseModel):
    """Top-level vignette container for 9-class meningitis/encephalitis differential.

    All sub-models are required except where Optional is annotated. Cross-field
    validators enforce class-conditional clinical rules:

    1. PAM always-flag rule (CDC PAM 2017 case definition):
       If ground_truth_class == ClassLabel.PAM, then
       exposure.freshwater_exposure_within_14d MUST be True.

    2. Cryptococcal CD4 consistency (Ford CID 2018 PMC5850628):
       If ground_truth_class == ClassLabel.CRYPTOCOCCAL_FUNGAL and HIV+,
       then cd4_count_cells_per_uL MUST be set.

    3. Schema version lock: schema_version is Literal['2.0'] at top level
       (mirrors provenance.schema_version for redundant safety).
    """
    model_config = ConfigDict(extra="forbid")

    schema_version: Literal["2.0"] = Field(
        "2.0",
        description="Schema version locked to '2.0'. Top-level lock mirrors "
                    "provenance.schema_version for migration safety.",
    )
    case_id: str = Field(
        ..., min_length=1, max_length=200,
        description="Unique case identifier within corpus. Convention: "
                    "'<CLASS>-<NNN>-<ANCHOR-PMID>' (e.g., 'PAM-001-MMWR-2025-Arkansas').",
    )
    ground_truth_class: ClassLabel = Field(
        ...,
        description="Ground-truth diagnostic class (1-9) per ClassLabel IntEnum.",
    )
    demographics: Demographics
    history: History
    exposure: ExposureHistory
    vitals: VitalSigns
    exam: PhysicalExam
    labs: Labs
    csf: CSFProfile
    imaging: Imaging
    diagnostic_tests: DiagnosticTests
    adjudication: AdjudicationMetadata
    literature_anchors: List[LiteratureAnchor] = Field(
        ..., min_length=1,
        description="At least one peer-reviewed literature anchor required.",
    )
    provenance: Provenance
    narrative_es: Optional[str] = Field(
        None, max_length=4000,
        description="Spanish-language clinical narrative for bilingual deployment "
                    "(UPCH/Peru target).",
    )
    narrative_en: Optional[str] = Field(
        None, max_length=4000,
        description="English-language clinical narrative for bilingual deployment.",
    )

    @model_validator(mode="after")
    def _pam_always_flag_rule(self):
        """CDC PAM 2017 case definition + MMWR 2025: PAM class requires freshwater
        exposure within 14 days (or nasal irrigation/ablution)."""
        if self.ground_truth_class == ClassLabel.PAM:
            if not self.exposure.freshwater_exposure_within_14d:
                raise ValueError(
                    "PAM ground_truth_class requires "
                    "exposure.freshwater_exposure_within_14d=True per CDC 2017 "
                    "case definition (always-flag rule)."
                )
        return self

    @model_validator(mode="after")
    def _cryptococcal_cd4_required_when_hiv(self):
        """Ford CID 2018 PMC5850628: cryptococcal class with HIV+ requires CD4 count
        for cryptococcal antigen screening threshold determination."""
        if self.ground_truth_class == ClassLabel.CRYPTOCOCCAL_FUNGAL:
            hiv_pos = self.exposure.hiv_status in (
                "positive_on_art",
                "positive_not_on_art",
            )
            if hiv_pos and self.exposure.cd4_count_cells_per_uL is None:
                raise ValueError(
                    "Cryptococcal class with HIV-positive status requires "
                    "exposure.cd4_count_cells_per_uL (Ford CID 2018 PMC5850628; "
                    "WHO Advanced HIV 2022)."
                )
        return self


__all__ = [
    "ClassLabel",
    "Demographics",
    "History",
    "ExposureHistory",
    "VitalSigns",
    "PhysicalExam",
    "Labs",
    "CSFProfile",
    "Imaging",
    "DxResult",
    "DiagnosticTests",
    "AdjudicationMetadata",
    "LiteratureAnchor",
    "Provenance",
    "VignetteSchema",
]
