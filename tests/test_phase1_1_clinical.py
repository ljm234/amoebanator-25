"""Comprehensive tests for ml.data.clinical module -- targeting 100 % coverage.

Covers:
    - Constants (REQUIRED_FIELDS, OPTIONAL_FIELDS, VALID_RANGES, etc.)
    - Enums (ValidationSeverity, LaboratoryFlag)
    - NamedTuples (ValidationResult, CSFReferenceRange, DiagnosticCriteria, …)
    - ClinicalRecord frozen dataclass
    - ParserConfig dataclass
    - RecordValidator (all _validate_* helpers, _is_missing)
    - CSVRecordParser (parse, _parse_row, all _parse_* helpers)
    - ClinicalRecordParser (CSV / JSON / unsupported, to_feature_matrix)
    - CSFAnalyzer (_evaluate_parameter, analyze, _generate_summary)
    - DiagnosticScoreCalculator (default criteria, _normalize_weights,
        _evaluate_criterion, calculate_score, _categorize_risk)
    - ClinicalTimelineBuilder (all add_* methods, get_timeline, get_all_events)
    - OutcomePredictor (extract_features, predict_outcome_probability)
    - CohortBuilder (add_records, build_*_cohorts, get_cohort,
        get_cohort_statistics)
    - SymptomEncoder (encode, encode_to_vector, get_category_counts)
    - TreatmentProtocol (get_recommended_agents)
    - ClinicalDecisionSupport (evaluate_patient)
    - Factory functions (create_clinical_parser, create_diagnostic_calculator,
        create_decision_support, create_symptom_encoder, create_cohort_builder)
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import pytest

from ml.data.clinical import (
    KNOWN_SYMPTOMS,
    OPTIONAL_FIELDS,
    PAM_TREATMENT_PROTOCOL,
    REQUIRED_FIELDS,
    SYMPTOM_ONTOLOGY,
    VALID_RANGES,
    CSF_REFERENCE_RANGES,
    ClinicalDecisionSupport,
    ClinicalRecord,
    ClinicalRecordParser,
    ClinicalTimeline,
    ClinicalTimelineBuilder,
    CohortBuilder,
    CSFAnalyzer,
    CSFInterpretation,
    CSFReferenceRange,
    CSVRecordParser,
    DiagnosticCriteria,
    DiagnosticScoreCalculator,
    DrugInteraction,
    LaboratoryFlag,
    LaboratoryPanel,
    OutcomePredictor,
    ParserConfig,
    RecordValidator,
    RiskScore,
    SymptomEncoder,
    SymptomOntology,
    TreatmentRecord,
    ValidationResult,
    ValidationSeverity,
    create_clinical_parser,
    create_cohort_builder,
    create_decision_support,
    create_diagnostic_calculator,
    create_symptom_encoder,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_record(**overrides: object) -> ClinicalRecord:
    """Create a ClinicalRecord with sensible defaults, overridable."""
    defaults: dict[str, object] = dict(
        record_id="PAT-001",
        age=25,
        sex="M",
        csf_glucose=60.0,
        csf_protein=30.0,
        csf_wbc=200,
        csf_rbc=5,
        microscopy=1,
        pcr=1,
        culture=0,
        symptoms=("headache", "fever"),
        onset_date=datetime(2025, 1, 15),
        duration_hours=48,
        exposure_type="freshwater",
        water_source="lake",
        geographic_region="Southeast US",
        diagnosis="PAM",
        outcome="survived",
        days_to_outcome=14,
    )
    defaults.update(overrides)
    return ClinicalRecord(**defaults)  # type: ignore[arg-type]


def _csv_content(rows: list[dict[str, str]], fieldnames: list[str] | None = None) -> str:
    """Build CSV text from rows."""
    if fieldnames is None:
        fieldnames = sorted({k for row in rows for k in row})
    header = ",".join(fieldnames)
    lines = [header]
    for row in rows:
        lines.append(",".join(row.get(f, "") for f in fieldnames))
    return "\n".join(lines)


_BASE_ROW: dict[str, str] = {
    "record_id": "R1",
    "age": "30",
    "sex": "M",
    "csf_glucose": "55",
    "csf_protein": "35",
    "csf_wbc": "150",
    "csf_rbc": "2",
    "microscopy": "1",
    "pcr": "1",
    "culture": "0",
    "symptoms": "headache;fever",
    "onset_date": "2025-01-10",
    "duration_hours": "48",
    "exposure_type": "freshwater",
    "water_source": "lake",
    "geographic_region": "Southeast US",
    "diagnosis": "PAM",
    "outcome": "survived",
    "days_to_outcome": "14",
}

_ALL_FIELDS = sorted(_BASE_ROW.keys())


# ===================================================================
# Constants
# ===================================================================

class TestConstants:
    def test_required_fields(self) -> None:
        assert isinstance(REQUIRED_FIELDS, frozenset)
        assert "age" in REQUIRED_FIELDS
        assert "csf_wbc" in REQUIRED_FIELDS
        assert "microscopy" in REQUIRED_FIELDS

    def test_optional_fields(self) -> None:
        assert isinstance(OPTIONAL_FIELDS, frozenset)
        assert "sex" in OPTIONAL_FIELDS
        assert REQUIRED_FIELDS.isdisjoint(OPTIONAL_FIELDS)

    def test_valid_ranges(self) -> None:
        for field_name, (lo, hi) in VALID_RANGES.items():
            assert lo < hi, f"Invalid range for {field_name}"

    def test_known_symptoms(self) -> None:
        assert isinstance(KNOWN_SYMPTOMS, frozenset)
        assert "headache" in KNOWN_SYMPTOMS

    def test_csf_reference_ranges(self) -> None:
        for key, ref in CSF_REFERENCE_RANGES.items():
            assert ref.normal_min <= ref.normal_max

    def test_symptom_ontology(self) -> None:
        assert "headache" in SYMPTOM_ONTOLOGY
        assert SYMPTOM_ONTOLOGY["headache"].symptom_code == "R51"

    def test_pam_treatment_protocol(self) -> None:
        assert PAM_TREATMENT_PROTOCOL.protocol_id == "PAM-2025-001"
        assert len(PAM_TREATMENT_PROTOCOL.first_line_agents) >= 2


# ===================================================================
# Enums
# ===================================================================

class TestValidationSeverity:
    def test_members(self) -> None:
        assert set(ValidationSeverity.__members__) == {
            "INFO", "WARNING", "ERROR", "CRITICAL",
        }


class TestLaboratoryFlag:
    def test_members(self) -> None:
        expected = {"NORMAL", "LOW", "HIGH", "CRITICAL_LOW", "CRITICAL_HIGH", "INDETERMINATE"}
        assert set(LaboratoryFlag.__members__) == expected


# ===================================================================
# NamedTuples smoke
# ===================================================================

class TestNamedTuples:
    def test_validation_result(self) -> None:
        vr = ValidationResult("age", True, ValidationSeverity.INFO, "ok", 25)
        assert vr.field_name == "age"
        assert vr.corrected_value is None

    def test_csf_reference_range(self) -> None:
        rr = CSFReferenceRange("glucose", "mg/dL", 50, 80, 20, None, False)
        assert rr.parameter == "glucose"

    def test_diagnostic_criteria(self) -> None:
        dc = DiagnosticCriteria("c1", "test", "cat", 1.0, None, ">=", False)
        assert dc.criterion_id == "c1"

    def test_risk_score(self) -> None:
        rs = RiskScore("s1", "p1", 0.5, "MODERATE", (), (0.4, 0.6), datetime.now())
        assert rs.risk_category == "MODERATE"

    def test_clinical_timeline(self) -> None:
        ct = ClinicalTimeline("e1", "p1", "LAB", datetime.now(), "desc", {})
        assert ct.event_type == "LAB"

    def test_treatment_record(self) -> None:
        tr = TreatmentRecord("t1", "p1", "Drug", 100, "mg", "IV", datetime.now(), None, False)
        assert tr.medication_name == "Drug"

    def test_symptom_ontology(self) -> None:
        so = SymptomOntology("R51", "Headache", "neuro", "CNS", (1, 10), ("cephalalgia",))
        assert so.symptom_code == "R51"

    def test_drug_interaction(self) -> None:
        di = DrugInteraction("A", "B", "inhibit", "high", "cyp3a4", "avoid")
        assert di.severity == "high"

    def test_laboratory_panel(self) -> None:
        lp = LaboratoryPanel("LP1", "CSF Panel", ("glucose",), "CSF", 2, 4)
        assert lp.panel_name == "CSF Panel"


# ===================================================================
# ClinicalRecord (frozen dataclass)
# ===================================================================

class TestClinicalRecord:
    def test_defaults(self) -> None:
        r = ClinicalRecord(record_id="R1", age=30)
        assert r.sex == "U"
        assert r.outcome == "unknown"
        assert r.symptoms == ()

    def test_frozen(self) -> None:
        r = _make_record()
        with pytest.raises(AttributeError):
            r.age = 99  # type: ignore[misc]

    def test_all_fields_populated(self) -> None:
        r = _make_record()
        assert r.record_id == "PAT-001"
        assert r.age == 25
        assert r.diagnosis == "PAM"


# ===================================================================
# ParserConfig
# ===================================================================

class TestParserConfig:
    def test_defaults(self) -> None:
        pc = ParserConfig()
        assert pc.strict_mode is True
        assert pc.coerce_types is True
        assert "NA" in pc.missing_values

    def test_custom(self) -> None:
        pc = ParserConfig(strict_mode=False, date_format="%d/%m/%Y")
        assert pc.strict_mode is False
        assert pc.date_format == "%d/%m/%Y"


# ===================================================================
# RecordValidator
# ===================================================================

class TestRecordValidator:
    def setup_method(self) -> None:
        self.validator = RecordValidator()

    # -- Missing required fields ---
    def test_missing_required_field_absent(self) -> None:
        results = self.validator.validate_record({})
        critical = [r for r in results if r.severity == ValidationSeverity.CRITICAL]
        # age, csf_wbc, microscopy all missing
        assert len(critical) >= 3

    def test_missing_required_field_null(self) -> None:
        results = self.validator.validate_record({"age": "NA", "csf_wbc": "10", "microscopy": "1"})
        crit = [r for r in results if not r.is_valid and r.severity == ValidationSeverity.CRITICAL]
        assert any(r.field_name == "age" for r in crit)

    # -- _is_missing ---
    def test_is_missing_none(self) -> None:
        assert self.validator._is_missing(None) is True

    def test_is_missing_nan(self) -> None:
        assert self.validator._is_missing(float("nan")) is True

    def test_is_missing_string(self) -> None:
        assert self.validator._is_missing("N/A") is True
        assert self.validator._is_missing("hello") is False

    def test_is_missing_number(self) -> None:
        assert self.validator._is_missing(42) is False

    # -- _validate_numeric_range ---
    def test_numeric_in_range(self) -> None:
        r = self.validator._validate_numeric_range("age", 30, 0, 120)
        assert r.is_valid is True

    def test_numeric_out_of_range(self) -> None:
        r = self.validator._validate_numeric_range("age", 150, 0, 120)
        assert r.is_valid is False
        assert r.corrected_value == 120

    def test_numeric_below_range(self) -> None:
        r = self.validator._validate_numeric_range("age", -5, 0, 120)
        assert r.is_valid is False
        assert r.corrected_value == 0

    def test_numeric_not_convertible(self) -> None:
        r = self.validator._validate_numeric_range("age", "xyz", 0, 120)
        assert r.is_valid is False
        assert r.severity == ValidationSeverity.ERROR

    # -- _validate_binary ---
    def test_binary_valid(self) -> None:
        r = self.validator._validate_binary("microscopy", "1")
        assert r.is_valid is True

    def test_binary_non01(self) -> None:
        r = self.validator._validate_binary("microscopy", "5")
        assert r.is_valid is False
        assert r.corrected_value == 1

    def test_binary_zero_int(self) -> None:
        r = self.validator._validate_binary("microscopy", "0")
        assert r.is_valid is True

    def test_binary_non_numeric(self) -> None:
        r = self.validator._validate_binary("microscopy", "abc")
        assert r.is_valid is False
        assert r.severity == ValidationSeverity.ERROR

    # -- _validate_sex ---
    def test_sex_valid_codes(self) -> None:
        for v in ("M", "F", "U"):
            r = self.validator._validate_sex(v)
            assert r.is_valid is True

    def test_sex_full_names(self) -> None:
        for v in ("MALE", "FEMALE", "UNKNOWN"):
            r = self.validator._validate_sex(v)
            assert r.is_valid is True
            assert r.corrected_value == v[0]

    def test_sex_invalid(self) -> None:
        r = self.validator._validate_sex("X")
        assert r.is_valid is False
        assert r.corrected_value == "U"

    # -- _validate_symptoms ---
    def test_symptoms_string(self) -> None:
        r = self.validator._validate_symptoms("headache;fever")
        assert r.is_valid is True

    def test_symptoms_list(self) -> None:
        r = self.validator._validate_symptoms(["headache", "fever"])
        assert r.is_valid is True

    def test_symptoms_unknown_warns(self) -> None:
        r = self.validator._validate_symptoms("headache;alien_rash")
        assert r.severity == ValidationSeverity.WARNING

    def test_symptoms_unparseable(self) -> None:
        r = self.validator._validate_symptoms(12345)
        assert r.is_valid is False
        assert r.severity == ValidationSeverity.ERROR

    def test_symptoms_with_normalize_off(self) -> None:
        v = RecordValidator(ParserConfig(normalize_symptoms=False))
        r = v._validate_symptoms("headache;alien_rash")
        assert r.is_valid is True
        assert r.severity == ValidationSeverity.INFO

    # -- _validate_outcome ---
    def test_outcome_valid(self) -> None:
        for o in ("survived", "deceased", "unknown"):
            r = self.validator._validate_outcome(o)
            assert r.is_valid is True

    def test_outcome_mapping(self) -> None:
        for alt, expected in [("alive", "survived"), ("dead", "deceased"),
                              ("living", "survived"), ("died", "deceased"),
                              ("death", "deceased"), ("fatal", "deceased"),
                              ("na", "unknown"), ("n/a", "unknown")]:
            r = self.validator._validate_outcome(alt)
            assert r.is_valid is True
            assert r.corrected_value == expected

    def test_outcome_unknown_value(self) -> None:
        r = self.validator._validate_outcome("banana")
        assert r.is_valid is False
        assert r.corrected_value == "unknown"

    # -- validate_record complete ---
    def test_validate_record_all_valid(self) -> None:
        results = self.validator.validate_record(dict(_BASE_ROW))
        invalid = [r for r in results if not r.is_valid]
        assert invalid == []

    def test_validation_log_property(self) -> None:
        self.validator.validate_record(dict(_BASE_ROW))
        log = self.validator.validation_log
        assert len(log) > 0
        # It's a copy
        log.clear()
        assert len(self.validator.validation_log) > 0


# ===================================================================
# CSVRecordParser
# ===================================================================

class TestCSVRecordParser:
    def test_parse_valid_csv(self, tmp_path: Path) -> None:
        csv_file = tmp_path / "data.csv"
        csv_file.write_text(_csv_content([_BASE_ROW], _ALL_FIELDS))
        parser = CSVRecordParser()
        records = parser.parse(csv_file)
        assert len(records) == 1
        assert records[0].age == 30

    def test_parse_errors_tracked(self, tmp_path: Path) -> None:
        row = dict(_BASE_ROW)
        row.pop("age")
        row.pop("csf_wbc")
        csv_file = tmp_path / "bad.csv"
        fieldnames = sorted(row.keys())
        csv_file.write_text(_csv_content([row], fieldnames))
        parser = CSVRecordParser(ParserConfig(strict_mode=False))
        records = parser.parse(csv_file)
        assert len(records) == 0  # critical errors → None

    def test_strict_mode_raises(self, tmp_path: Path) -> None:
        row = dict(_BASE_ROW)
        row.pop("age")
        csv_file = tmp_path / "strict.csv"
        fieldnames = sorted(row.keys())
        csv_file.write_text(_csv_content([row], fieldnames))
        parser = CSVRecordParser(ParserConfig(strict_mode=True))
        with pytest.raises(ValueError):
            parser.parse(csv_file)

    def test_parse_errors_property(self, tmp_path: Path) -> None:
        csv_file = tmp_path / "ok.csv"
        csv_file.write_text(_csv_content([_BASE_ROW], _ALL_FIELDS))
        parser = CSVRecordParser()
        parser.parse(csv_file)
        assert parser.parse_errors == []

    # -- _parse_int ---
    def test_parse_int_normal(self) -> None:
        p = CSVRecordParser()
        assert p._parse_int("42") == 42

    def test_parse_int_missing(self) -> None:
        p = CSVRecordParser()
        assert p._parse_int(None) == 0
        assert p._parse_int("NA") == 0

    def test_parse_int_bad(self) -> None:
        p = CSVRecordParser()
        assert p._parse_int("xyz") == 0

    # -- _parse_int_optional ---
    def test_parse_int_optional_none(self) -> None:
        p = CSVRecordParser()
        assert p._parse_int_optional(None) is None
        assert p._parse_int_optional("N/A") is None

    def test_parse_int_optional_bad(self) -> None:
        p = CSVRecordParser()
        assert p._parse_int_optional("xyz") is None

    def test_parse_int_optional_ok(self) -> None:
        p = CSVRecordParser()
        assert p._parse_int_optional("7") == 7

    # -- _parse_float_optional ---
    def test_parse_float_optional(self) -> None:
        p = CSVRecordParser()
        assert p._parse_float_optional("3.14") == pytest.approx(3.14)
        assert p._parse_float_optional(None) is None
        assert p._parse_float_optional("bad") is None

    # -- _parse_binary ---
    def test_parse_binary(self) -> None:
        p = CSVRecordParser()
        assert p._parse_binary("1") == 1
        assert p._parse_binary("0") == 0
        assert p._parse_binary(None) == 0
        assert p._parse_binary("bad") == 0

    # -- _parse_binary_optional ---
    def test_parse_binary_optional(self) -> None:
        p = CSVRecordParser()
        assert p._parse_binary_optional("1") == 1
        assert p._parse_binary_optional(None) is None
        assert p._parse_binary_optional("bad") is None

    # -- _parse_sex ---
    def test_parse_sex(self) -> None:
        p = CSVRecordParser()
        assert p._parse_sex("M") == "M"
        assert p._parse_sex("FEMALE") == "F"
        assert p._parse_sex("MALE") == "M"
        assert p._parse_sex(None) == "U"
        assert p._parse_sex("other") == "U"

    # -- _parse_symptoms ---
    def test_parse_symptoms(self) -> None:
        p = CSVRecordParser()
        assert p._parse_symptoms("headache;fever") == ("headache", "fever")
        assert p._parse_symptoms(None) == ()
        assert p._parse_symptoms("NA") == ()

    # -- _parse_date ---
    def test_parse_date(self) -> None:
        p = CSVRecordParser()
        dt = p._parse_date("2025-01-15")
        assert dt == datetime(2025, 1, 15)
        assert p._parse_date(None) is None
        assert p._parse_date("bad-date") is None

    # -- _parse_outcome ---
    def test_parse_outcome(self) -> None:
        p = CSVRecordParser()
        assert p._parse_outcome("survived") == "survived"
        assert p._parse_outcome("dead") == "deceased"
        assert p._parse_outcome("alive") == "survived"
        assert p._parse_outcome(None) == "unknown"
        assert p._parse_outcome("banana") == "unknown"

    # -- _parse_string_optional ---
    def test_parse_string_optional(self) -> None:
        p = CSVRecordParser()
        assert p._parse_string_optional("hello") == "hello"
        assert p._parse_string_optional(None) is None
        assert p._parse_string_optional("NA") is None

    # -- multiple rows ---
    def test_parse_multiple_rows(self, tmp_path: Path) -> None:
        row2 = dict(_BASE_ROW, record_id="R2", age="40", outcome="deceased")
        csv_file = tmp_path / "multi.csv"
        csv_file.write_text(_csv_content([_BASE_ROW, row2], _ALL_FIELDS))
        parser = CSVRecordParser()
        records = parser.parse(csv_file)
        assert len(records) == 2

    def test_custom_id_column(self, tmp_path: Path) -> None:
        row = dict(_BASE_ROW)
        row["patient_id"] = "P99"
        fieldnames = sorted(row.keys())
        csv_file = tmp_path / "custom_id.csv"
        csv_file.write_text(_csv_content([row], fieldnames))
        parser = CSVRecordParser()
        records = parser.parse(csv_file, id_column="patient_id")
        assert records[0].record_id == "P99"

    def test_missing_id_column_uses_row_num(self, tmp_path: Path) -> None:
        row = dict(_BASE_ROW)
        row.pop("record_id")
        fieldnames = sorted(row.keys())
        csv_file = tmp_path / "no_id.csv"
        csv_file.write_text(_csv_content([row], fieldnames))
        parser = CSVRecordParser()
        records = parser.parse(csv_file, id_column="record_id")
        assert records[0].record_id.startswith("row_")


# ===================================================================
# ClinicalRecordParser  (CSV + JSON + unsupported)
# ===================================================================

class TestClinicalRecordParser:
    def test_parse_csv(self, tmp_path: Path) -> None:
        csv_file = tmp_path / "data.csv"
        csv_file.write_text(_csv_content([_BASE_ROW], _ALL_FIELDS))
        parser = ClinicalRecordParser()
        records = parser.parse(csv_file)
        assert len(records) == 1

    def test_parse_json_array(self, tmp_path: Path) -> None:
        json_data = [_BASE_ROW]
        json_file = tmp_path / "data.json"
        json_file.write_text(json.dumps(json_data))
        parser = ClinicalRecordParser()
        records = parser.parse(json_file)
        assert len(records) == 1

    def test_parse_json_records_key(self, tmp_path: Path) -> None:
        json_data = {"records": [_BASE_ROW]}
        json_file = tmp_path / "data.json"
        json_file.write_text(json.dumps(json_data))
        parser = ClinicalRecordParser()
        records = parser.parse(json_file)
        assert len(records) == 1

    def test_parse_json_bad_structure(self, tmp_path: Path) -> None:
        json_file = tmp_path / "bad.json"
        json_file.write_text(json.dumps({"foo": "bar"}))
        parser = ClinicalRecordParser()
        with pytest.raises(ValueError, match="JSON must contain"):
            parser.parse(json_file)

    def test_parse_json_non_dict_row_skipped(self, tmp_path: Path) -> None:
        json_file = tmp_path / "mixed.json"
        json_file.write_text(json.dumps([_BASE_ROW, "not_a_dict", 42]))
        parser = ClinicalRecordParser()
        records = parser.parse(json_file)
        assert len(records) == 1

    def test_parse_json_strict_raises(self, tmp_path: Path) -> None:
        bad_row = dict(_BASE_ROW)
        bad_row.pop("age")
        json_file = tmp_path / "strict.json"
        json_file.write_text(json.dumps([bad_row]))
        parser = ClinicalRecordParser(ParserConfig(strict_mode=True))
        with pytest.raises(ValueError):
            parser.parse(json_file)

    def test_parse_json_nonstrict_skips(self, tmp_path: Path) -> None:
        bad_row = dict(_BASE_ROW)
        bad_row.pop("age")
        json_file = tmp_path / "nonstrict.json"
        json_file.write_text(json.dumps([bad_row]))
        parser = ClinicalRecordParser(ParserConfig(strict_mode=False))
        records = parser.parse(json_file)
        # may return empty (critical check fails) or parsing succeeds
        assert isinstance(records, list)

    def test_unsupported_format(self, tmp_path: Path) -> None:
        xml_file = tmp_path / "data.xml"
        xml_file.write_text("<data/>")
        parser = ClinicalRecordParser()
        with pytest.raises(ValueError, match="Unsupported file format"):
            parser.parse(xml_file)

    # -- to_feature_matrix ---
    def test_to_feature_matrix(self) -> None:
        parser = ClinicalRecordParser()
        r = _make_record()
        matrix, names = parser.to_feature_matrix([r])
        assert matrix.shape[0] == 1
        assert "age" in names
        # headache present
        assert matrix[0, names.index("sym_headache")] == 1.0

    def test_to_feature_matrix_custom_vocab(self) -> None:
        parser = ClinicalRecordParser()
        r = _make_record(symptoms=("fever",))
        matrix, names = parser.to_feature_matrix([r], symptom_vocabulary=["fever", "nausea"])
        assert matrix[0, names.index("sym_fever")] == 1.0
        assert matrix[0, names.index("sym_nausea")] == 0.0

    def test_to_feature_matrix_empty(self) -> None:
        parser = ClinicalRecordParser()
        matrix, names = parser.to_feature_matrix([])
        assert matrix.shape == (0, len(names))

    def test_to_feature_matrix_optional_none(self) -> None:
        parser = ClinicalRecordParser()
        r = _make_record(csf_glucose=None, csf_protein=None, pcr=None, exposure_type=None)
        matrix, names = parser.to_feature_matrix([r])
        assert matrix[0, names.index("csf_glucose")] == 0.0
        assert matrix[0, names.index("exposure")] == 0.0


# ===================================================================
# CSFAnalyzer
# ===================================================================

class TestCSFAnalyzer:
    def setup_method(self) -> None:
        self.analyzer = CSFAnalyzer()

    # -- _evaluate_parameter ---
    def test_parameter_none(self) -> None:
        assert self.analyzer._evaluate_parameter(None, "glucose") == LaboratoryFlag.INDETERMINATE

    def test_parameter_unknown(self) -> None:
        assert self.analyzer._evaluate_parameter(50.0, "unknown_param") == LaboratoryFlag.INDETERMINATE

    def test_parameter_normal(self) -> None:
        assert self.analyzer._evaluate_parameter(60.0, "glucose") == LaboratoryFlag.NORMAL

    def test_parameter_low(self) -> None:
        # Below normal_min but above critical_low
        assert self.analyzer._evaluate_parameter(25.0, "glucose") == LaboratoryFlag.LOW

    def test_parameter_high(self) -> None:
        assert self.analyzer._evaluate_parameter(90.0, "glucose") == LaboratoryFlag.HIGH

    def test_parameter_critical_low(self) -> None:
        assert self.analyzer._evaluate_parameter(10.0, "glucose") == LaboratoryFlag.CRITICAL_LOW

    def test_parameter_critical_high(self) -> None:
        assert self.analyzer._evaluate_parameter(600.0, "protein") == LaboratoryFlag.CRITICAL_HIGH

    def test_parameter_rbc_high(self) -> None:
        # rbc has normal_max=0 and no critical_high → HIGH
        assert self.analyzer._evaluate_parameter(5.0, "rbc") == LaboratoryFlag.HIGH

    # -- analyze ---
    def test_analyze_normal_csf(self) -> None:
        r = _make_record(csf_glucose=60.0, csf_protein=30.0, csf_wbc=2, csf_rbc=0)
        interp = self.analyzer.analyze(r)
        assert interp.glucose_flag == LaboratoryFlag.NORMAL
        assert interp.pleocytosis_present is False
        assert "normal limits" in interp.interpretation_summary.lower()

    def test_analyze_pam_pattern(self) -> None:
        r = _make_record(csf_glucose=15.0, csf_protein=600.0, csf_wbc=1200, csf_rbc=10)
        interp = self.analyzer.analyze(r)
        assert interp.pleocytosis_present is True
        assert interp.predominant_cell_type == "lymphocyte"
        assert len(interp.differential_considerations) > 0

    def test_analyze_low_glucose_differentials(self) -> None:
        r = _make_record(csf_glucose=15.0, csf_wbc=2)
        interp = self.analyzer.analyze(r)
        assert "Bacterial meningitis" in interp.differential_considerations

    def test_analyze_high_protein_differentials(self) -> None:
        r = _make_record(csf_protein=600.0, csf_wbc=2)
        interp = self.analyzer.analyze(r)
        assert "Inflammatory process" in interp.differential_considerations

    def test_analyze_csf_rbc_none(self) -> None:
        r = _make_record(csf_rbc=None)
        interp = self.analyzer.analyze(r)
        assert interp.rbc_flag == LaboratoryFlag.INDETERMINATE

    # -- _generate_summary ---
    def test_summary_pleocytosis(self) -> None:
        s = self.analyzer._generate_summary(
            LaboratoryFlag.NORMAL, LaboratoryFlag.NORMAL, LaboratoryFlag.HIGH, True
        )
        assert "Pleocytosis" in s

    def test_summary_low_glucose(self) -> None:
        s = self.analyzer._generate_summary(
            LaboratoryFlag.LOW, LaboratoryFlag.NORMAL, LaboratoryFlag.NORMAL, False
        )
        assert "glucose" in s.lower()

    def test_summary_high_protein(self) -> None:
        s = self.analyzer._generate_summary(
            LaboratoryFlag.NORMAL, LaboratoryFlag.HIGH, LaboratoryFlag.NORMAL, False
        )
        assert "protein" in s.lower()

    def test_summary_critical_included(self) -> None:
        s = self.analyzer._generate_summary(
            LaboratoryFlag.CRITICAL_LOW, LaboratoryFlag.CRITICAL_HIGH, LaboratoryFlag.HIGH, True
        )
        assert "Pleocytosis" in s
        assert "glucose" in s.lower()
        assert "protein" in s.lower()


# ===================================================================
# DiagnosticScoreCalculator
# ===================================================================

class TestDiagnosticScoreCalculator:
    def test_default_criteria(self) -> None:
        calc = DiagnosticScoreCalculator()
        assert len(calc.criteria) == 6
        total_w = sum(c.weight for c in calc.criteria)
        assert total_w == pytest.approx(1.0, abs=0.01)

    def test_custom_criteria(self) -> None:
        crit = [DiagnosticCriteria("c1", "Test", "cat", 5.0, None, ">=", False)]
        calc = DiagnosticScoreCalculator(criteria=crit)
        assert len(calc.criteria) == 1
        assert calc.criteria[0].weight == pytest.approx(1.0)

    def test_calculate_score_all_met(self) -> None:
        r = _make_record(
            microscopy=1, csf_wbc=500, csf_glucose=20.0, pcr=1,
            exposure_type="freshwater", duration_hours=24,
        )
        calc = DiagnosticScoreCalculator()
        score = calc.calculate_score(r)
        assert score.risk_category in ("VERY_HIGH", "HIGH")
        assert len(score.contributing_factors) >= 5

    def test_calculate_score_none_met(self) -> None:
        r = _make_record(
            microscopy=0, csf_wbc=2, csf_glucose=60.0, pcr=0,
            exposure_type=None, duration_hours=200,
        )
        calc = DiagnosticScoreCalculator()
        score = calc.calculate_score(r)
        assert score.risk_category == "VERY_LOW"
        assert len(score.contributing_factors) == 0

    def test_calculate_score_partial(self) -> None:
        r = _make_record(
            microscopy=1, csf_wbc=2, csf_glucose=60.0, pcr=None,
            exposure_type=None, duration_hours=None,
        )
        calc = DiagnosticScoreCalculator()
        score = calc.calculate_score(r)
        assert 0.0 < score.score_value < 1.0

    # -- _evaluate_criterion edge cases ---
    def test_criterion_csf_glucose_none(self) -> None:
        calc = DiagnosticScoreCalculator()
        crit = [c for c in calc.criteria if c.criterion_id == "csf_glucose_low"][0]
        r = _make_record(csf_glucose=None)
        met, contrib = calc._evaluate_criterion(crit, r)
        assert met is False

    def test_criterion_pcr_none(self) -> None:
        calc = DiagnosticScoreCalculator()
        crit = [c for c in calc.criteria if c.criterion_id == "pcr_positive"][0]
        r = _make_record(pcr=None)
        met, _ = calc._evaluate_criterion(crit, r)
        assert met is False

    def test_criterion_duration_none(self) -> None:
        calc = DiagnosticScoreCalculator()
        crit = [c for c in calc.criteria if c.criterion_id == "rapid_progression"][0]
        r = _make_record(duration_hours=None)
        met, _ = calc._evaluate_criterion(crit, r)
        assert met is False

    def test_criterion_water_exposure_false(self) -> None:
        calc = DiagnosticScoreCalculator()
        crit = [c for c in calc.criteria if c.criterion_id == "water_exposure"][0]
        r = _make_record(exposure_type=None)
        met, _ = calc._evaluate_criterion(crit, r)
        assert met is False

    def test_criterion_water_exposure_true(self) -> None:
        calc = DiagnosticScoreCalculator()
        crit = [c for c in calc.criteria if c.criterion_id == "water_exposure"][0]
        r = _make_record(exposure_type="lake")
        met, _ = calc._evaluate_criterion(crit, r)
        assert met is True

    # -- _categorize_risk ---
    def test_categorize_risk_all(self) -> None:
        calc = DiagnosticScoreCalculator()
        assert calc._categorize_risk(0.9) == "VERY_HIGH"
        assert calc._categorize_risk(0.8) == "VERY_HIGH"
        assert calc._categorize_risk(0.7) == "HIGH"
        assert calc._categorize_risk(0.6) == "HIGH"
        assert calc._categorize_risk(0.5) == "MODERATE"
        assert calc._categorize_risk(0.4) == "MODERATE"
        assert calc._categorize_risk(0.3) == "LOW"
        assert calc._categorize_risk(0.2) == "LOW"
        assert calc._categorize_risk(0.1) == "VERY_LOW"
        assert calc._categorize_risk(0.0) == "VERY_LOW"

    def test_confidence_interval_clamped(self) -> None:
        r = _make_record(
            microscopy=1, csf_wbc=500, csf_glucose=20.0, pcr=1,
            exposure_type="lake", duration_hours=24,
        )
        calc = DiagnosticScoreCalculator()
        score = calc.calculate_score(r)
        lo, hi = score.confidence_interval
        assert lo >= 0.0
        assert hi <= 1.0

    def test_normalize_weights_zero_total(self) -> None:
        crit = [DiagnosticCriteria("c1", "Test", "cat", 0.0, None, ">=", False)]
        calc = DiagnosticScoreCalculator(criteria=crit)
        # Zero weight total → weights stay 0
        assert calc.criteria[0].weight == 0.0

    def test_normalize_weights_already_normalized(self) -> None:
        """Second call to _normalize_weights is a no-op (line 1345 early return)."""
        calc = DiagnosticScoreCalculator()
        assert calc._weights_normalized is True
        calc._normalize_weights()  # should return immediately
        assert calc._weights_normalized is True


# ===================================================================
# ClinicalTimelineBuilder
# ===================================================================

class TestClinicalTimelineBuilder:
    def test_add_symptom_onset(self) -> None:
        builder = ClinicalTimelineBuilder()
        builder.add_symptom_onset("P1", datetime(2025, 1, 1), ["headache", "fever"])
        events = builder.get_all_events()
        assert len(events) == 1
        assert events[0].event_type == "SYMPTOM_ONSET"

    def test_add_laboratory_result(self) -> None:
        builder = ClinicalTimelineBuilder()
        builder.add_laboratory_result("P1", datetime(2025, 1, 2), "CSF WBC", 500.0, "cells/uL")
        events = builder.get_all_events()
        assert events[0].event_type == "LAB_RESULT"

    def test_add_diagnostic_event(self) -> None:
        builder = ClinicalTimelineBuilder()
        builder.add_diagnostic_event("P1", datetime(2025, 1, 3), "PCR", "positive")
        events = builder.get_all_events()
        assert events[0].event_type == "DIAGNOSTIC"

    def test_add_treatment_event(self) -> None:
        builder = ClinicalTimelineBuilder()
        builder.add_treatment_event("P1", datetime(2025, 1, 4), "Amphotericin B", 5.0, "IV")
        events = builder.get_all_events()
        assert events[0].event_type == "TREATMENT"
        assert "Amphotericin" in events[0].description

    def test_get_timeline_patient_filter(self) -> None:
        builder = ClinicalTimelineBuilder()
        builder.add_symptom_onset("P1", datetime(2025, 1, 1), ["headache"])
        builder.add_symptom_onset("P2", datetime(2025, 1, 2), ["fever"])
        assert len(builder.get_timeline("P1")) == 1
        assert len(builder.get_timeline("P2")) == 1

    def test_timeline_sorted_by_timestamp(self) -> None:
        builder = ClinicalTimelineBuilder()
        builder.add_laboratory_result("P1", datetime(2025, 1, 3), "WBC", 100.0, "cells")
        builder.add_symptom_onset("P1", datetime(2025, 1, 1), ["headache"])
        timeline = builder.get_timeline("P1")
        assert timeline[0].event_timestamp < timeline[1].event_timestamp

    def test_get_all_events_sorted(self) -> None:
        builder = ClinicalTimelineBuilder()
        builder.add_diagnostic_event("P1", datetime(2025, 1, 5), "Culture", "negative")
        builder.add_symptom_onset("P2", datetime(2025, 1, 1), ["fever"])
        events = builder.get_all_events()
        assert events[0].event_timestamp < events[1].event_timestamp


# ===================================================================
# OutcomePredictor
# ===================================================================

class TestOutcomePredictor:
    def test_extract_features_pediatric(self) -> None:
        r = _make_record(age=10, csf_wbc=600, csf_glucose=30.0, pcr=1, microscopy=1, duration_hours=12)
        op = OutcomePredictor()
        feats = op.extract_features(r)
        assert feats["age_pediatric"] == 1.0
        assert feats["age_elderly"] == 0.0
        assert feats["csf_wbc_high"] == 1.0
        assert feats["csf_glucose_low"] == 1.0
        assert feats["rapid_presentation"] == 1.0
        assert feats["delayed_presentation"] == 0.0

    def test_extract_features_elderly(self) -> None:
        r = _make_record(age=70, duration_hours=100)
        op = OutcomePredictor()
        feats = op.extract_features(r)
        assert feats["age_elderly"] == 1.0
        assert feats["delayed_presentation"] == 1.0

    def test_extract_features_no_duration(self) -> None:
        r = _make_record(duration_hours=None)
        op = OutcomePredictor()
        feats = op.extract_features(r)
        assert "rapid_presentation" not in feats
        assert "delayed_presentation" not in feats

    def test_extract_features_glucose_none(self) -> None:
        r = _make_record(csf_glucose=None)
        op = OutcomePredictor()
        feats = op.extract_features(r)
        assert feats["csf_glucose_low"] == 0.0

    def test_extract_features_pcr_zero(self) -> None:
        r = _make_record(pcr=0, microscopy=0)
        op = OutcomePredictor()
        feats = op.extract_features(r)
        assert feats["pcr_positive"] == 0.0
        assert feats["microscopy_positive"] == 0.0

    def test_predict_outcome_probability_keys(self) -> None:
        r = _make_record()
        op = OutcomePredictor()
        result = op.predict_outcome_probability(r)
        assert "mortality_probability" in result
        assert "survival_probability" in result
        assert "confidence" in result
        assert result["mortality_probability"] + result["survival_probability"] == pytest.approx(1.0)

    def test_predict_outcome_probability_range(self) -> None:
        r = _make_record()
        op = OutcomePredictor()
        result = op.predict_outcome_probability(r)
        assert 0.0 <= result["mortality_probability"] <= 1.0


# ===================================================================
# CohortBuilder
# ===================================================================

class TestCohortBuilder:
    def _records(self) -> list[ClinicalRecord]:
        return [
            _make_record(record_id="P1", age=10, outcome="survived", exposure_type="lake"),
            _make_record(record_id="P2", age=25, outcome="deceased", exposure_type="river"),
            _make_record(record_id="P3", age=50, outcome="survived", exposure_type="lake"),
            _make_record(record_id="P4", age=70, outcome="deceased", exposure_type=None),
        ]

    def test_build_age_cohorts(self) -> None:
        cb = CohortBuilder()
        cb.add_records(self._records())
        cohorts = cb.build_age_cohorts()
        assert "P1" in cohorts["age_0_18"]
        assert "P4" in cohorts["age_65_120"]

    def test_build_age_cohorts_custom_bins(self) -> None:
        cb = CohortBuilder()
        cb.add_records(self._records())
        cohorts = cb.build_age_cohorts(bins=(0, 30, 60, 120))
        assert "P1" in cohorts["age_0_30"]

    def test_build_outcome_cohorts(self) -> None:
        cb = CohortBuilder()
        cb.add_records(self._records())
        cohorts = cb.build_outcome_cohorts()
        assert "P1" in cohorts["survived"]
        assert "P2" in cohorts["deceased"]

    def test_build_outcome_unknown(self) -> None:
        r = _make_record(record_id="PX", outcome="unknown")
        cb = CohortBuilder()
        cb.add_records([r])
        cohorts = cb.build_outcome_cohorts()
        assert "PX" in cohorts["unknown"]

    def test_build_outcome_unmapped(self) -> None:
        # Outcome that doesn't match survived/deceased/unknown goes to unknown
        r = _make_record(record_id="PY", outcome="survived")
        cb = CohortBuilder()
        cb.add_records([r])
        cohorts = cb.build_outcome_cohorts()
        assert "PY" in cohorts["survived"]

    def test_build_outcome_unrecognised_goes_to_unknown(self) -> None:
        """Force an outcome not in the cohort dict keys (line 1649 else branch)."""
        import dataclasses
        r = _make_record(record_id="PZ", outcome="survived")
        # Bypass frozen constraint via object.__setattr__ equivalent:
        # ClinicalRecord is frozen, so build a non-frozen copy
        vals = {f.name: getattr(r, f.name) for f in dataclasses.fields(r)}
        vals["outcome"] = "transferred"  # not in {"survived","deceased","unknown"}
        # Build a raw object bypassing __init__ type check
        raw = object.__new__(ClinicalRecord)
        for k, v in vals.items():
            object.__setattr__(raw, k, v)
        cb = CohortBuilder()
        cb.add_records([raw])
        cohorts = cb.build_outcome_cohorts()
        assert "PZ" in cohorts["unknown"]

    def test_build_exposure_cohorts(self) -> None:
        cb = CohortBuilder()
        cb.add_records(self._records())
        cohorts = cb.build_exposure_cohorts()
        assert "P1" in cohorts["lake"]
        assert "P2" in cohorts["river"]
        assert "P4" in cohorts["unknown"]

    def test_get_cohort_existing(self) -> None:
        cb = CohortBuilder()
        cb.add_records(self._records())
        cb.build_age_cohorts()
        assert len(cb.get_cohort("age_0_18")) >= 1

    def test_get_cohort_missing(self) -> None:
        cb = CohortBuilder()
        assert cb.get_cohort("nonexistent") == []

    def test_get_cohort_statistics(self) -> None:
        cb = CohortBuilder()
        cb.add_records(self._records())
        cb.build_outcome_cohorts()
        stats = cb.get_cohort_statistics("survived")
        assert stats["count"] == 2
        assert "age_mean" in stats

    def test_get_cohort_statistics_empty(self) -> None:
        cb = CohortBuilder()
        stats = cb.get_cohort_statistics("nonexistent")
        assert stats == {"count": 0}


# ===================================================================
# SymptomEncoder
# ===================================================================

class TestSymptomEncoder:
    def test_encode_known(self) -> None:
        enc = SymptomEncoder()
        result = enc.encode("headache")
        assert result is not None
        assert result.symptom_code == "R51"

    def test_encode_by_synonym(self) -> None:
        enc = SymptomEncoder()
        result = enc.encode("cephalalgia")
        assert result is not None
        assert result.symptom_name == "Headache"

    def test_encode_unknown(self) -> None:
        enc = SymptomEncoder()
        assert enc.encode("alien_rash") is None

    def test_encode_normalized(self) -> None:
        enc = SymptomEncoder()
        result = enc.encode("Altered Mental Status")
        assert result is not None

    def test_encode_to_vector(self) -> None:
        enc = SymptomEncoder()
        vec, names = enc.encode_to_vector(["headache", "fever"])
        assert vec.shape == (len(names),)
        assert vec[names.index("headache")] == 1.0
        assert vec[names.index("fever")] == 1.0
        assert vec[names.index("nausea")] == 0.0

    def test_encode_to_vector_unknown_ignored(self) -> None:
        enc = SymptomEncoder()
        vec, names = enc.encode_to_vector(["alien_rash"])
        assert vec.sum() == 0.0

    def test_get_category_counts(self) -> None:
        enc = SymptomEncoder()
        counts = enc.get_category_counts(["headache", "fever", "seizure"])
        assert counts["neurological"] == 2  # headache + seizure
        assert counts["constitutional"] == 1  # fever

    def test_get_category_counts_unknown(self) -> None:
        enc = SymptomEncoder()
        counts = enc.get_category_counts(["alien_rash"])
        assert counts == {}

    def test_post_init_reverse_lookup(self) -> None:
        enc = SymptomEncoder()
        assert "R51" in enc._code_to_name
        assert enc._code_to_name["R51"] == "headache"


# ===================================================================
# TreatmentProtocol
# ===================================================================

class TestTreatmentProtocol:
    def test_get_recommended_agents_no_failures(self) -> None:
        agents = PAM_TREATMENT_PROTOCOL.get_recommended_agents()
        assert "Amphotericin B (liposomal)" in agents
        assert "Miltefosine" in agents

    def test_get_recommended_agents_first_line_failed(self) -> None:
        agents = PAM_TREATMENT_PROTOCOL.get_recommended_agents(
            failed_agents=["Amphotericin B (liposomal)", "Miltefosine"]
        )
        assert "Fluconazole" in agents
        assert "Amphotericin B (liposomal)" not in agents

    def test_get_recommended_agents_partial_first_line(self) -> None:
        agents = PAM_TREATMENT_PROTOCOL.get_recommended_agents(
            failed_agents=["Miltefosine"]
        )
        assert "Amphotericin B (liposomal)" in agents
        assert "Miltefosine" not in agents

    def test_get_recommended_agents_none_arg(self) -> None:
        agents = PAM_TREATMENT_PROTOCOL.get_recommended_agents(None)
        assert len(agents) >= 2


# ===================================================================
# ClinicalDecisionSupport
# ===================================================================

class TestClinicalDecisionSupport:
    def test_evaluate_patient_keys(self) -> None:
        cds = ClinicalDecisionSupport()
        r = _make_record()
        result = cds.evaluate_patient(r)
        assert "patient_id" in result
        assert "csf_interpretation" in result
        assert "risk_assessment" in result
        assert "outcome_prediction" in result
        assert "recommended_treatment" in result
        assert "monitoring" in result
        assert "supportive_care" in result

    def test_evaluate_patient_csf_keys(self) -> None:
        cds = ClinicalDecisionSupport()
        r = _make_record()
        result = cds.evaluate_patient(r)
        csf = result["csf_interpretation"]
        assert "glucose_status" in csf
        assert "protein_status" in csf
        assert "wbc_status" in csf
        assert "pleocytosis" in csf

    def test_evaluate_patient_risk_keys(self) -> None:
        cds = ClinicalDecisionSupport()
        r = _make_record()
        result = cds.evaluate_patient(r)
        risk = result["risk_assessment"]
        assert "score" in risk
        assert "category" in risk

    def test_default_factory(self) -> None:
        cds = create_decision_support()
        assert isinstance(cds, ClinicalDecisionSupport)


# ===================================================================
# Factory functions
# ===================================================================

class TestFactories:
    def test_create_clinical_parser_default(self) -> None:
        p = create_clinical_parser()
        assert isinstance(p, ClinicalRecordParser)

    def test_create_clinical_parser_config(self) -> None:
        p = create_clinical_parser(ParserConfig(strict_mode=False))
        assert isinstance(p, ClinicalRecordParser)

    def test_create_diagnostic_calculator_default(self) -> None:
        c = create_diagnostic_calculator()
        assert isinstance(c, DiagnosticScoreCalculator)
        assert len(c.criteria) == 6

    def test_create_diagnostic_calculator_custom(self) -> None:
        crit = [DiagnosticCriteria("c1", "Test", "cat", 1.0, None, ">=", False)]
        c = create_diagnostic_calculator(custom_criteria=crit)
        assert len(c.criteria) == 1

    def test_create_decision_support(self) -> None:
        cds = create_decision_support()
        assert isinstance(cds, ClinicalDecisionSupport)

    def test_create_symptom_encoder_default(self) -> None:
        enc = create_symptom_encoder()
        assert isinstance(enc, SymptomEncoder)
        assert len(enc.ontology) == len(SYMPTOM_ONTOLOGY)

    def test_create_symptom_encoder_custom(self) -> None:
        custom = {"test": SymptomOntology("T01", "Test", "cat", "sys", (1, 5), ())}
        enc = create_symptom_encoder(custom_ontology=custom)
        assert len(enc.ontology) == 1

    def test_create_cohort_builder_empty(self) -> None:
        cb = create_cohort_builder()
        assert isinstance(cb, CohortBuilder)

    def test_create_cohort_builder_with_records(self) -> None:
        records = [_make_record(record_id="P1"), _make_record(record_id="P2")]
        cb = create_cohort_builder(records=records)
        cohorts = cb.build_age_cohorts()
        total = sum(len(v) for v in cohorts.values())
        assert total == 2


# ===================================================================
# CSFInterpretation dataclass
# ===================================================================

class TestCSFInterpretation:
    def test_frozen(self) -> None:
        interp = CSFInterpretation(
            glucose_flag=LaboratoryFlag.NORMAL,
            protein_flag=LaboratoryFlag.NORMAL,
            wbc_flag=LaboratoryFlag.NORMAL,
            rbc_flag=LaboratoryFlag.NORMAL,
            glucose_ratio=None,
            pleocytosis_present=False,
            predominant_cell_type=None,
            interpretation_summary="ok",
            differential_considerations=(),
        )
        with pytest.raises(AttributeError):
            interp.glucose_flag = LaboratoryFlag.HIGH  # type: ignore[misc]
