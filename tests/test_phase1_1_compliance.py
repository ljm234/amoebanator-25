"""
Phase 1.1 Compliance Module — Comprehensive Test Suite.

Tests cover:
  - ORCID validation (format, checksum, ISO 7064 Mod 11-2)
  - Researcher identity construction and validation
  - CITI training completeness and expiration checks
  - IRB application state machine (all valid and invalid transitions)
  - CDC Form 0.1310 field validation
  - Security attestation signing, verification, and expiration
  - Compliance gate evaluation (all 4 stages)
  - Factory functions
  - Serialisation round-trips
"""

from __future__ import annotations

import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from ml.data.compliance import (
    ALL_SAFEGUARDS,
    AttestationStatus,
    CDCDataRequestForm,
    CDCFormStatus,
    CITICompletion,
    ComplianceGate,
    ComplianceGateResult,
    ConsentRecord,
    ConsentRegistry,
    ConsentStatus,
    ConsentType,
    IRBApplication,
    IRBStatus,
    IRBTransition,
    ResearcherIdentity,
    ResearcherValidator,
    SafeguardCategory,
    SecurityAttestation,
    ValidationIssue,
    _validate_orcid_checksum,
    create_compliance_gate,
    create_irb_application,
    create_researcher_identity,
)


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════


def _make_citi_completions(
    expired: bool = False,
    low_score: bool = False,
    missing: frozenset[str] | None = None,
) -> tuple[CITICompletion, ...]:
    """Build a set of CITI completions for testing."""
    from ml.data.compliance import CITI_REQUIRED_MODULES

    now = datetime.now(tz=timezone.utc)
    modules = CITI_REQUIRED_MODULES - (missing or frozenset())
    comps = []
    for mod_id in sorted(modules):
        exp_date = now - timedelta(days=30) if expired else now + timedelta(days=365)
        score = 65.0 if low_score else 95.0
        comps.append(
            CITICompletion(
                module_id=mod_id,
                module_name=mod_id.replace("_", " ").title(),
                completion_date=now - timedelta(days=60),
                expiration_date=exp_date,
                score=score,
                certificate_id=f"CERT-{mod_id[:4].upper()}",
            )
        )
    return tuple(comps)


def _make_valid_identity() -> ResearcherIdentity:
    """Create a fully valid researcher identity."""
    return ResearcherIdentity(
        orcid="0000-0002-1825-0097",
        full_name="Jordan Montenegro",
        email="jmontenegro@weber.edu",
        institution="Weber State University",
        department="Computer Science",
        role="Independent Researcher",
        citi_completions=_make_citi_completions(),
        verified_at=datetime.now(tz=timezone.utc),
    )


def _make_approved_irb(identity: ResearcherIdentity | None = None) -> IRBApplication:
    """Create an IRB application in APPROVED state with future expiration."""
    identity = identity or _make_valid_identity()
    irb = IRBApplication(
        protocol_title="PAM Diagnostic ML Pipeline",
        protocol_number="IRB-2026-001",
        pi_identity=identity,
    )
    irb.transition_to(IRBStatus.SUBMITTED, actor="PI")
    irb.transition_to(IRBStatus.UNDER_REVIEW, actor="IRB Chair")
    irb.transition_to(IRBStatus.APPROVED, actor="IRB Committee")
    return irb


def _make_submitted_cdc_form() -> CDCDataRequestForm:
    """Create a CDC form that has passed validation and been submitted."""
    form = CDCDataRequestForm()
    form.fields = {
        "investigator_name": "Jordan Montenegro",
        "institution": "Weber State University",
        "project_title": "PAM Diagnostic Pipeline",
        "data_description": "De-identified PAM surveillance records 2015-2025",
        "justification": "Machine learning model for rapid PAM screening",
        "irb_protocol_number": "IRB-2026-001",
        "irb_approval_date": datetime.now(tz=timezone.utc).isoformat(),
        "data_security_plan": (
            "All data will be encrypted using AES-256-GCM at rest and TLS 1.3 "
            "in transit. Access is restricted via role-based access control with "
            "multi-factor authentication. Physical safeguards include locked "
            "server rooms with biometric access. Annual HIPAA training is mandatory "
            "for all personnel with data access. Audit logs are maintained with "
            "cryptographic tamper detection."
        ),
        "destruction_plan": (
            "Data destruction follows NIST SP 800-88 Rev. 1 media sanitization "
            "guidelines. All electronic media containing PHI will undergo "
            "cryptographic erasure followed by physical destruction and shredding."
        ),
        "signature_date": datetime.now(tz=timezone.utc).isoformat(),
    }
    issues = form.validate()
    assert not any(i.severity == "error" for i in issues)
    form.mark_submitted(receipt_id="CDC-REC-2026-0001")
    return form


def _make_signed_attestation(identity: ResearcherIdentity | None = None) -> tuple[SecurityAttestation, bytes]:
    """Create a signed security attestation with all safeguards compliant."""
    att = SecurityAttestation(researcher=identity or _make_valid_identity())
    for sg in ALL_SAFEGUARDS:
        att.respond(sg.check_id, compliant=True)
    key = b"test-signing-key-32-bytes-long!!"
    att.sign(key)
    return att, key


# ═══════════════════════════════════════════════════════════════════════════
# ORCID Validation Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestORCIDValidation:
    """ORCID identifier format and checksum tests."""

    def test_valid_orcid_checksum(self) -> None:
        assert _validate_orcid_checksum("0000000218250097") is True

    def test_invalid_orcid_checksum(self) -> None:
        assert _validate_orcid_checksum("0000000218250098") is False

    def test_orcid_with_x_check_digit(self) -> None:
        assert _validate_orcid_checksum("000000012281955X") is True

    def test_validator_rejects_bad_format(self) -> None:
        validator = ResearcherValidator()
        issues = validator._validate_orcid("not-an-orcid")
        assert len(issues) == 1
        assert issues[0].severity == "error"
        assert "XXXX-XXXX-XXXX-XXXX" in issues[0].message

    def test_validator_rejects_bad_checksum(self) -> None:
        validator = ResearcherValidator()
        issues = validator._validate_orcid("0000-0002-1825-0098")
        assert len(issues) == 1
        assert "checksum" in issues[0].message.lower()

    def test_validator_accepts_valid_orcid(self) -> None:
        validator = ResearcherValidator()
        issues = validator._validate_orcid("0000-0002-1825-0097")
        assert issues == []


# ═══════════════════════════════════════════════════════════════════════════
# Researcher Identity & Validator Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestResearcherIdentity:
    """Researcher identity construction and frozen dataclass behaviour."""

    def test_identity_is_frozen(self) -> None:
        identity = _make_valid_identity()
        with pytest.raises(AttributeError):
            identity.full_name = "Modified"  # type: ignore[misc]

    def test_identity_fields(self) -> None:
        identity = _make_valid_identity()
        assert identity.orcid == "0000-0002-1825-0097"
        assert identity.institution == "Weber State University"
        assert len(identity.citi_completions) > 0

    def test_factory_creates_verified_identity(self) -> None:
        identity = create_researcher_identity(
            orcid="0000-0002-1825-0097",
            full_name="Test User",
            email="test@example.edu",
            institution="Test University",
            department="CS",
        )
        assert identity.verified_at is not None


class TestResearcherValidator:
    """Comprehensive researcher validation tests."""

    def test_valid_researcher_passes(self) -> None:
        identity = _make_valid_identity()
        validator = ResearcherValidator()
        issues = validator.validate(identity)
        errors = [i for i in issues if i.severity == "error"]
        assert errors == []

    def test_invalid_email_format(self) -> None:
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="not-valid-email",
            institution="Test",
            department="CS",
            citi_completions=_make_citi_completions(),
        )
        validator = ResearcherValidator()
        issues = validator.validate(identity)
        email_issues = [i for i in issues if i.field_name == "email"]
        assert any(i.severity == "error" for i in email_issues)

    def test_non_institutional_email_warning(self) -> None:
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="user@gmail.com",
            institution="Test",
            department="CS",
            citi_completions=_make_citi_completions(),
        )
        validator = ResearcherValidator()
        issues = validator.validate(identity)
        email_warns = [i for i in issues if i.field_name == "email" and i.severity == "warning"]
        assert len(email_warns) == 1
        assert "non-institutional" in email_warns[0].message.lower()

    def test_expired_citi_module(self) -> None:
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=_make_citi_completions(expired=True),
        )
        validator = ResearcherValidator()
        issues = validator.validate(identity)
        expired_issues = [
            i for i in issues
            if "expired" in i.message.lower()
        ]
        assert len(expired_issues) > 0

    def test_low_citi_score_warning(self) -> None:
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=_make_citi_completions(low_score=True),
        )
        validator = ResearcherValidator()
        issues = validator.validate(identity)
        score_warns = [
            i for i in issues
            if "80%" in i.message
        ]
        assert len(score_warns) > 0

    def test_missing_citi_modules(self) -> None:
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=_make_citi_completions(
                missing=frozenset({"hipaa_privacy", "data_security"})
            ),
        )
        validator = ResearcherValidator()
        issues = validator.validate(identity)
        missing_issues = [
            i for i in issues
            if "not completed" in i.message.lower()
        ]
        assert len(missing_issues) == 2

    def test_custom_required_modules(self) -> None:
        validator = ResearcherValidator(
            required_modules=frozenset({"custom_module"}),
        )
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=(),
        )
        issues = validator.validate(identity)
        missing = [i for i in issues if "custom_module" in i.message]
        assert len(missing) == 1

    def test_edu_domain_accepted(self) -> None:
        validator = ResearcherValidator()
        issues = validator._validate_email("user@stanford.edu")
        assert issues == []

    def test_gov_domain_accepted(self) -> None:
        validator = ResearcherValidator()
        issues = validator._validate_email("user@cdc.gov")
        assert issues == []

    def test_ac_domain_accepted(self) -> None:
        validator = ResearcherValidator()
        issues = validator._validate_email("user@oxford.ac.uk")
        assert issues == []


# ═══════════════════════════════════════════════════════════════════════════
# IRB Application Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestIRBApplication:
    """IRB state machine, transitions, and lifecycle checks."""

    def test_initial_state_is_draft(self) -> None:
        irb = IRBApplication()
        assert irb.status == IRBStatus.DRAFT

    def test_valid_transition_draft_to_submitted(self) -> None:
        irb = IRBApplication()
        irb.transition_to(IRBStatus.SUBMITTED, actor="PI")
        assert irb.status == IRBStatus.SUBMITTED
        assert irb.submitted_date is not None

    def test_valid_full_approval_path(self) -> None:
        irb = _make_approved_irb()
        assert irb.status == IRBStatus.APPROVED
        assert irb.approval_date is not None
        assert irb.expiration_date is not None

    def test_transition_records_history(self) -> None:
        irb = IRBApplication()
        irb.transition_to(IRBStatus.SUBMITTED, actor="PI", notes="Initial submission")
        assert len(irb.transitions) == 1
        t = irb.transitions[0]
        assert t.from_status == IRBStatus.DRAFT
        assert t.to_status == IRBStatus.SUBMITTED
        assert t.actor == "PI"
        assert t.notes == "Initial submission"

    def test_invalid_transition_raises(self) -> None:
        irb = IRBApplication()
        with pytest.raises(ValueError, match="Invalid transition"):
            irb.transition_to(IRBStatus.APPROVED)

    def test_terminated_has_no_valid_transitions(self) -> None:
        irb = IRBApplication()
        irb.transition_to(IRBStatus.SUBMITTED)
        irb.transition_to(IRBStatus.UNDER_REVIEW)
        irb.transition_to(IRBStatus.TERMINATED)
        with pytest.raises(ValueError):
            irb.transition_to(IRBStatus.APPROVED)

    def test_revisions_requested_loops_to_submitted(self) -> None:
        irb = IRBApplication()
        irb.transition_to(IRBStatus.SUBMITTED)
        irb.transition_to(IRBStatus.REVISIONS_REQUESTED)
        irb.transition_to(IRBStatus.SUBMITTED)
        assert irb.status == IRBStatus.SUBMITTED
        assert len(irb.transitions) == 3

    def test_conditional_approval_to_approved(self) -> None:
        irb = IRBApplication()
        irb.transition_to(IRBStatus.SUBMITTED)
        irb.transition_to(IRBStatus.UNDER_REVIEW)
        irb.transition_to(IRBStatus.CONDITIONALLY_APPROVED)
        irb.transition_to(IRBStatus.APPROVED)
        assert irb.status == IRBStatus.APPROVED

    def test_is_current_when_approved(self) -> None:
        irb = _make_approved_irb()
        assert irb.is_current() is True

    def test_is_current_false_when_not_approved(self) -> None:
        irb = IRBApplication()
        assert irb.is_current() is False

    def test_days_until_expiration(self) -> None:
        irb = _make_approved_irb()
        days = irb.days_until_expiration()
        assert days is not None
        assert days > 1000  # 3 years ≈ 1095 days

    def test_days_until_expiration_none_when_no_expiry(self) -> None:
        irb = IRBApplication()
        assert irb.days_until_expiration() is None

    def test_compute_protocol_hash(self) -> None:
        irb = IRBApplication()
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            f.write(b"test protocol content for hashing")
            f.flush()
            h = irb.compute_protocol_hash(Path(f.name))
        assert len(h) == 64  # SHA-256 hex digest
        assert irb.protocol_hash == h

    def test_to_dict_serialisation(self) -> None:
        irb = _make_approved_irb()
        d = irb.to_dict()
        assert d["status"] == "approved"
        assert d["approval_date"] is not None
        assert d["expiration_date"] is not None
        assert d["transitions_count"] == 3

    def test_factory_creates_draft(self) -> None:
        identity = _make_valid_identity()
        irb = create_irb_application(
            protocol_title="Test",
            protocol_number="TP-001",
            pi_identity=identity,
        )
        assert irb.status == IRBStatus.DRAFT
        assert irb.pi_identity == identity

    def test_expired_to_draft_resubmission(self) -> None:
        irb = _make_approved_irb()
        irb.transition_to(IRBStatus.EXPIRED)
        irb.transition_to(IRBStatus.DRAFT)
        assert irb.status == IRBStatus.DRAFT

    def test_suspended_to_approved(self) -> None:
        irb = _make_approved_irb()
        irb.transition_to(IRBStatus.SUSPENDED)
        irb.transition_to(IRBStatus.APPROVED)
        assert irb.status == IRBStatus.APPROVED

    def test_suspended_to_terminated(self) -> None:
        irb = _make_approved_irb()
        irb.transition_to(IRBStatus.SUSPENDED)
        irb.transition_to(IRBStatus.TERMINATED)
        assert irb.status == IRBStatus.TERMINATED

    def test_renewal_pending_to_approved(self) -> None:
        irb = _make_approved_irb()
        irb.transition_to(IRBStatus.RENEWAL_PENDING)
        irb.transition_to(IRBStatus.APPROVED)
        assert irb.status == IRBStatus.APPROVED

    def test_renewal_pending_to_expired(self) -> None:
        irb = _make_approved_irb()
        irb.transition_to(IRBStatus.RENEWAL_PENDING)
        irb.transition_to(IRBStatus.EXPIRED)
        assert irb.status == IRBStatus.EXPIRED


# ═══════════════════════════════════════════════════════════════════════════
# CDC Form 0.1310 Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestCDCDataRequestForm:
    """CDC Form 0.1310 field validation and lifecycle tests."""

    def test_initial_status_not_started(self) -> None:
        form = CDCDataRequestForm()
        assert form.status == CDCFormStatus.NOT_STARTED

    def test_set_field_moves_to_in_progress(self) -> None:
        form = CDCDataRequestForm()
        form.set_field("investigator_name", "Test")
        assert form.status == CDCFormStatus.IN_PROGRESS

    def test_empty_form_fails_validation(self) -> None:
        form = CDCDataRequestForm()
        issues = form.validate()
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) >= 10  # at least 10 required fields missing
        assert form.status == CDCFormStatus.VALIDATION_FAILED

    def test_complete_form_passes(self) -> None:
        form = _make_submitted_cdc_form()
        assert form.status == CDCFormStatus.SUBMITTED

    def test_irb_date_too_old_warning(self) -> None:
        form = CDCDataRequestForm()
        form.fields = {
            "investigator_name": "Test",
            "institution": "Test U",
            "project_title": "Test Project",
            "data_description": "Test data",
            "justification": "Test justification",
            "irb_protocol_number": "IRB-001",
            "irb_approval_date": (
                datetime.now(tz=timezone.utc) - timedelta(days=400)
            ).isoformat(),
            "data_security_plan": " ".join(["word"] * 60),
            "destruction_plan": "NIST SP 800-88 sanitization and shredding",
            "signature_date": datetime.now(tz=timezone.utc).isoformat(),
        }
        issues = form.validate()
        date_warns = [
            i for i in issues
            if i.field_name == "irb_approval_date" and i.severity == "warning"
        ]
        assert len(date_warns) == 1

    def test_irb_date_invalid_format(self) -> None:
        form = CDCDataRequestForm()
        form.fields = {"irb_approval_date": "not-a-date"}
        form.validate()
        date_errs = [
            i for i in form.validation_issues
            if i.field_name == "irb_approval_date" and i.severity == "error"
        ]
        assert any("ISO 8601" in e.message for e in date_errs)

    def test_security_plan_too_short(self) -> None:
        form = CDCDataRequestForm()
        form.fields = {"data_security_plan": "Use encryption"}
        form.validate()
        plan_warns = [
            i for i in form.validation_issues
            if i.field_name == "data_security_plan" and i.severity == "warning"
        ]
        assert len(plan_warns) == 1

    def test_destruction_plan_missing_nist(self) -> None:
        form = CDCDataRequestForm()
        form.fields = {"destruction_plan": "We will delete the files"}
        form.validate()
        dest_infos = [
            i for i in form.validation_issues
            if i.field_name == "destruction_plan" and i.severity == "info"
        ]
        assert len(dest_infos) == 1
        assert dest_infos[0].suggestion is not None
        assert "NIST" in dest_infos[0].suggestion

    def test_destruction_plan_with_nist_passes(self) -> None:
        form = CDCDataRequestForm()
        form.fields = {"destruction_plan": "Follow NIST SP 800-88 guidelines"}
        form.validate()
        dest_infos = [
            i for i in form.validation_issues
            if i.field_name == "destruction_plan" and i.severity == "info"
        ]
        assert len(dest_infos) == 0

    def test_mark_submitted(self) -> None:
        form = _make_submitted_cdc_form()
        assert form.submission_receipt == "CDC-REC-2026-0001"
        assert form.submitted_at is not None

    def test_to_dict(self) -> None:
        form = _make_submitted_cdc_form()
        d = form.to_dict()
        assert d["form_version"] == "0.1310-2024"
        assert d["status"] == "submitted"
        assert d["submission_receipt"] is not None

    def test_ready_to_submit_status(self) -> None:
        form = CDCDataRequestForm()
        form.fields = {
            "investigator_name": "Test",
            "institution": "Test U",
            "project_title": "Test",
            "data_description": "Test",
            "justification": "Test",
            "irb_protocol_number": "IRB-001",
            "irb_approval_date": datetime.now(tz=timezone.utc).isoformat(),
            "data_security_plan": " ".join(["security"] * 60),
            "destruction_plan": "NIST 800-88 sanitization and destruction",
            "signature_date": datetime.now(tz=timezone.utc).isoformat(),
        }
        form.validate()
        assert form.status == CDCFormStatus.READY_TO_SUBMIT


# ═══════════════════════════════════════════════════════════════════════════
# Security Attestation Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestSecurityAttestation:
    """Security attestation signing, verification, and safeguard checks."""

    def test_initial_status_pending(self) -> None:
        att = SecurityAttestation()
        assert att.status == AttestationStatus.PENDING

    def test_respond_records_compliance(self) -> None:
        att = SecurityAttestation()
        att.respond("PHY-001", compliant=True)
        assert att.safeguard_responses["PHY-001"] is True

    def test_respond_invalid_check_raises(self) -> None:
        att = SecurityAttestation()
        with pytest.raises(ValueError, match="Unknown safeguard"):
            att.respond("INVALID-001", compliant=True)

    def test_all_checks_completed_false(self) -> None:
        att = SecurityAttestation()
        att.respond("PHY-001", compliant=True)
        assert att.all_checks_completed() is False

    def test_all_checks_completed_true(self) -> None:
        att = SecurityAttestation()
        for sg in ALL_SAFEGUARDS:
            att.respond(sg.check_id, compliant=True)
        assert att.all_checks_completed() is True

    def test_all_compliant(self) -> None:
        att = SecurityAttestation()
        for sg in ALL_SAFEGUARDS:
            att.respond(sg.check_id, compliant=True)
        assert att.all_compliant() is True

    def test_all_compliant_false_with_non_compliant(self) -> None:
        att = SecurityAttestation()
        for sg in ALL_SAFEGUARDS:
            att.respond(sg.check_id, compliant=True)
        att.respond("PHY-001", compliant=False)
        assert att.all_compliant() is False

    def test_sign_succeeds(self) -> None:
        att, key = _make_signed_attestation()
        assert att.status == AttestationStatus.SIGNED
        assert att.signed_at is not None
        assert att.expires_at is not None
        assert len(att.signature) == 64  # HMAC-SHA256 hex digest

    def test_sign_fails_incomplete(self) -> None:
        att = SecurityAttestation()
        att.respond("PHY-001", compliant=True)
        with pytest.raises(ValueError, match="not all safeguard checks"):
            att.sign(b"key")

    def test_sign_fails_non_compliant(self) -> None:
        att = SecurityAttestation()
        for sg in ALL_SAFEGUARDS:
            att.respond(sg.check_id, compliant=(sg.check_id != "PHY-001"))
        with pytest.raises(ValueError, match="not all safeguards are compliant"):
            att.sign(b"key")

    def test_verify_signature(self) -> None:
        att, key = _make_signed_attestation()
        assert att.verify_signature(key) is True

    def test_verify_signature_wrong_key(self) -> None:
        att, _ = _make_signed_attestation()
        assert att.verify_signature(b"wrong-key") is False

    def test_verify_signature_unsigned(self) -> None:
        att = SecurityAttestation()
        assert att.verify_signature(b"key") is False

    def test_is_current(self) -> None:
        att, _ = _make_signed_attestation()
        assert att.is_current() is True

    def test_is_current_false_when_pending(self) -> None:
        att = SecurityAttestation()
        assert att.is_current() is False

    def test_non_compliant_checks(self) -> None:
        att = SecurityAttestation()
        for sg in ALL_SAFEGUARDS:
            att.respond(sg.check_id, compliant=(sg.check_id != "TEC-003"))
        nc = att.non_compliant_checks()
        assert any(sg.check_id == "TEC-003" for sg in nc)

    def test_non_compliant_checks_includes_unanswered(self) -> None:
        att = SecurityAttestation()
        nc = att.non_compliant_checks()
        assert len(nc) == len(ALL_SAFEGUARDS)

    def test_to_dict(self) -> None:
        att, _ = _make_signed_attestation()
        d = att.to_dict()
        assert d["status"] == "signed"
        assert d["total_checks"] == len(ALL_SAFEGUARDS)
        assert d["compliant_checks"] == len(ALL_SAFEGUARDS)
        assert d["signature_present"] is True


# ═══════════════════════════════════════════════════════════════════════════
# Safeguard Constants Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestSafeguardConstants:
    """Validate safeguard definitions and categories."""

    def test_all_safeguards_count(self) -> None:
        assert len(ALL_SAFEGUARDS) == 12  # 3 physical + 5 technical + 4 admin

    def test_physical_safeguards_category(self) -> None:
        from ml.data.compliance import PHYSICAL_SAFEGUARDS
        for sg in PHYSICAL_SAFEGUARDS:
            assert sg.category == SafeguardCategory.PHYSICAL

    def test_technical_safeguards_category(self) -> None:
        from ml.data.compliance import TECHNICAL_SAFEGUARDS
        for sg in TECHNICAL_SAFEGUARDS:
            assert sg.category == SafeguardCategory.TECHNICAL

    def test_administrative_safeguards_category(self) -> None:
        from ml.data.compliance import ADMINISTRATIVE_SAFEGUARDS
        for sg in ADMINISTRATIVE_SAFEGUARDS:
            assert sg.category == SafeguardCategory.ADMINISTRATIVE

    def test_all_have_nist_control(self) -> None:
        for sg in ALL_SAFEGUARDS:
            assert sg.nist_control, f"{sg.check_id} missing NIST control"

    def test_all_have_hipaa_reference(self) -> None:
        for sg in ALL_SAFEGUARDS:
            assert sg.hipaa_reference, f"{sg.check_id} missing HIPAA reference"


# ═══════════════════════════════════════════════════════════════════════════
# Compliance Gate Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestComplianceGate:
    """Full compliance gate evaluation tests."""

    def test_empty_gate_fails(self) -> None:
        gate = ComplianceGate()
        result, blockers = gate.evaluate()
        assert result == ComplianceGateResult.FAILED
        assert len(blockers) == 4

    def test_full_gate_passes(self) -> None:
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        form = _make_submitted_cdc_form()
        att, _ = _make_signed_attestation(identity)

        gate = create_compliance_gate(
            researcher=identity,
            irb=irb,
            cdc_form=form,
            attestation=att,
        )
        result, blockers = gate.evaluate()
        assert result == ComplianceGateResult.PASSED
        assert blockers == []

    def test_missing_irb_fails(self) -> None:
        identity = _make_valid_identity()
        form = _make_submitted_cdc_form()
        att, _ = _make_signed_attestation(identity)

        gate = ComplianceGate(
            researcher_identity=identity,
            cdc_form=form,
            security_attestation=att,
        )
        result, blockers = gate.evaluate()
        assert result == ComplianceGateResult.FAILED
        assert any("IRB" in b for b in blockers)

    def test_draft_irb_fails(self) -> None:
        identity = _make_valid_identity()
        irb = IRBApplication(pi_identity=identity)  # DRAFT
        form = _make_submitted_cdc_form()
        att, _ = _make_signed_attestation(identity)

        gate = ComplianceGate(
            researcher_identity=identity,
            irb_application=irb,
            cdc_form=form,
            security_attestation=att,
        )
        result, blockers = gate.evaluate()
        assert result == ComplianceGateResult.FAILED

    def test_cdc_form_not_submitted_fails(self) -> None:
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        form = CDCDataRequestForm()  # NOT_STARTED
        att, _ = _make_signed_attestation(identity)

        gate = ComplianceGate(
            researcher_identity=identity,
            irb_application=irb,
            cdc_form=form,
            security_attestation=att,
        )
        result, blockers = gate.evaluate()
        assert result == ComplianceGateResult.FAILED
        assert any("CDC form" in b.lower() or "cdc" in b.lower() for b in blockers)

    def test_unsigned_attestation_fails(self) -> None:
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        form = _make_submitted_cdc_form()
        att = SecurityAttestation()  # PENDING

        gate = ComplianceGate(
            researcher_identity=identity,
            irb_application=irb,
            cdc_form=form,
            security_attestation=att,
        )
        result, blockers = gate.evaluate()
        assert result == ComplianceGateResult.FAILED

    def test_generate_report(self) -> None:
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        form = _make_submitted_cdc_form()
        att, _ = _make_signed_attestation(identity)

        gate = create_compliance_gate(
            researcher=identity, irb=irb, cdc_form=form, attestation=att,
        )
        report = gate.generate_report()
        assert report["gate_result"] == "passed"
        assert "stages" in report
        assert "researcher_identity" in report["stages"]
        assert "irb_application" in report["stages"]
        assert "cdc_form" in report["stages"]
        assert "security_attestation" in report["stages"]

    def test_generate_report_empty_gate(self) -> None:
        gate = ComplianceGate()
        report = gate.generate_report()
        assert report["gate_result"] == "failed"
        assert report["stages"]["researcher_identity"]["status"] == "not_provided"


# ═══════════════════════════════════════════════════════════════════════════
# Value Object Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestValueObjects:
    """NamedTuple and enum tests."""

    def test_irb_status_values(self) -> None:
        assert IRBStatus.DRAFT.value == "draft"
        assert IRBStatus.APPROVED.value == "approved"
        assert len(IRBStatus) == 10

    def test_cdc_form_status_values(self) -> None:
        assert CDCFormStatus.NOT_STARTED.value == "not_started"
        assert len(CDCFormStatus) == 9

    def test_attestation_status_values(self) -> None:
        assert AttestationStatus.PENDING.value == "pending"
        assert len(AttestationStatus) == 5

    def test_compliance_gate_result_values(self) -> None:
        assert ComplianceGateResult.PASSED.value == "passed"
        assert len(ComplianceGateResult) == 4

    def test_citi_completion_namedtuple(self) -> None:
        comp = CITICompletion(
            module_id="test",
            module_name="Test Module",
            completion_date=datetime.now(tz=timezone.utc),
            expiration_date=datetime.now(tz=timezone.utc),
            score=95.0,
            certificate_id="CERT-001",
        )
        assert comp.score == 95.0

    def test_irb_transition_namedtuple(self) -> None:
        t = IRBTransition(
            from_status=IRBStatus.DRAFT,
            to_status=IRBStatus.SUBMITTED,
            timestamp=datetime.now(tz=timezone.utc),
            actor="PI",
            notes="",
        )
        assert t.from_status == IRBStatus.DRAFT

    def test_validation_issue_namedtuple(self) -> None:
        vi = ValidationIssue(
            field_name="test",
            severity="error",
            message="test error",
            suggestion=None,
        )
        assert vi.suggestion is None


# ═══════════════════════════════════════════════════════════════════════════
# Coverage Gap Tests — previously uncovered lines
# ═══════════════════════════════════════════════════════════════════════════


class TestCoverageGaps:
    """Tests targeting previously uncovered code paths."""

    def test_orcid_checksum_with_dash(self) -> None:
        """Line 201: skip '-' char in ORCID checksum calculation."""
        result = _validate_orcid_checksum("0000-0002-1825-0097")
        assert result is True

    def test_citi_tz_naive_expiration(self) -> None:
        """Line 338: CITI expiration_date without tzinfo."""
        from ml.data.compliance import CITI_REQUIRED_MODULES
        now_naive = datetime.now()  # tz-naive
        comps = tuple(
            CITICompletion(
                module_id=m,
                module_name=m.replace("_", " ").title(),
                completion_date=now_naive - timedelta(days=30),
                expiration_date=now_naive - timedelta(days=1),  # expired, tz-naive
                score=95.0,
                certificate_id=f"C-{m[:4].upper()}",
            )
            for m in sorted(CITI_REQUIRED_MODULES)
        )
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=comps,
        )
        validator = ResearcherValidator()
        issues = validator.validate(identity)
        # Should have expired module errors without crashing on tz-naive
        expired_issues = [i for i in issues if "expired" in i.message.lower()]
        assert len(expired_issues) > 0

    def test_irb_is_current_tz_naive_expiration(self) -> None:
        """Lines 537, 541: IRB.is_current with tz-naive expiration_date."""
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        # Replace expiration_date with a tz-naive datetime (future)
        irb.expiration_date = datetime.now() + timedelta(days=365)
        assert irb.is_current() is True

    def test_irb_days_until_expiration_tz_naive(self) -> None:
        """Line 551: days_until_expiration with tz-naive expiration_date."""
        irb = _make_approved_irb()
        irb.expiration_date = datetime.now() + timedelta(days=100)
        days = irb.days_until_expiration()
        assert days is not None
        assert 99 <= days <= 100

    def test_cdc_irb_date_tz_naive(self) -> None:
        """Line 694: CDC form IRB date parsing with tz-naive datetime."""
        form = CDCDataRequestForm()
        # Use a tz-naive date string (no +00:00 suffix)
        naive_date = datetime.now().isoformat()
        form.fields = {
            "investigator_name": "Test",
            "institution": "Test U",
            "project_title": "Test",
            "data_description": "Test",
            "justification": "Test",
            "irb_protocol_number": "IRB-001",
            "irb_approval_date": naive_date,
            "data_security_plan": " ".join(["security"] * 60),
            "destruction_plan": "NIST SP 800-88 sanitization",
            "signature_date": naive_date,
        }
        form.validate()
        # Should not crash on tz-naive date
        assert form.status in (CDCFormStatus.READY_TO_SUBMIT, CDCFormStatus.VALIDATION_FAILED)

    def test_attestation_is_current_tz_naive_expiry(self) -> None:
        """Lines 1037, 1041: attestation.is_current with tz-naive expires_at."""
        att, key = _make_signed_attestation()
        # Replace expires_at with tz-naive datetime (future)
        att.expires_at = datetime.now() + timedelta(days=365)
        assert att.is_current() is True

    def test_gate_identity_errors_appended(self) -> None:
        """Lines 1120-1121: gate evaluation appends identity error messages."""
        bad_identity = ResearcherIdentity(
            orcid="0000-0000-0000-0000",  # bad checksum
            full_name="Test",
            email="bad-email",
            institution="Test",
            department="CS",
            citi_completions=(),
        )
        gate = ComplianceGate(researcher_identity=bad_identity)
        result, blockers = gate.evaluate()
        assert result == ComplianceGateResult.FAILED
        identity_blockers = [b for b in blockers if b.startswith("Identity:")]
        assert len(identity_blockers) >= 1


# ═══════════════════════════════════════════════════════════════════════════
# Multi-Jurisdiction Compliance Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestJurisdictionCompliance:
    """JurisdictionCompliance single-jurisdiction tracking tests."""

    def test_mark_completed_valid_requirement(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.USA_HIPAA)
        jc.mark_completed("irb_approval")
        assert "irb_approval" in jc.completed_requirements

    def test_mark_completed_unknown_requirement_raises(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.USA_HIPAA)
        with pytest.raises(ValueError, match="not a recognised requirement"):
            jc.mark_completed("nonexistent_req")

    def test_waive_requirement(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.EU_GDPR)
        jc.waive("dpo_notification", "Already established via parent org DPO")
        assert "dpo_notification" in jc.waived_requirements
        assert jc.waivers["dpo_notification"] == "Already established via parent org DPO"

    def test_waived_requirement_can_be_completed(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.USA_HIPAA)
        jc.waive("breach_notification_plan", "Covered by institutional plan")
        jc.mark_completed("breach_notification_plan")
        assert "breach_notification_plan" in jc.completed_requirements

    def test_is_compliant_all_completed(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance, _JURISDICTION_REQUIREMENTS
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.USA_COMMON_RULE)
        for req in _JURISDICTION_REQUIREMENTS[Jurisdiction.USA_COMMON_RULE]:
            jc.mark_completed(req)
        assert jc.is_compliant() is True

    def test_is_compliant_with_waivers(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance, _JURISDICTION_REQUIREMENTS
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.BRAZIL_LGPD)
        reqs = list(_JURISDICTION_REQUIREMENTS[Jurisdiction.BRAZIL_LGPD])
        for req in reqs[:-1]:
            jc.mark_completed(req)
        jc.waive(reqs[-1], "Institutional waiver")
        assert jc.is_compliant() is True

    def test_not_compliant_incomplete(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.USA_HIPAA)
        jc.mark_completed("irb_approval")
        assert jc.is_compliant() is False

    def test_outstanding_requirements(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance, _JURISDICTION_REQUIREMENTS
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.MEXICO_LFPDPPP)
        jc.mark_completed("inai_registration")
        outstanding = jc.outstanding_requirements()
        expected = _JURISDICTION_REQUIREMENTS[Jurisdiction.MEXICO_LFPDPPP] - {"inai_registration"}
        assert outstanding == expected

    def test_compliance_score(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance, _JURISDICTION_REQUIREMENTS
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.USA_HIPAA)
        total = len(_JURISDICTION_REQUIREMENTS[Jurisdiction.USA_HIPAA])
        jc.mark_completed("irb_approval")
        assert jc.compliance_score() == pytest.approx(1.0 / total)

    def test_compliance_score_full(self) -> None:
        from ml.data.compliance import Jurisdiction, JurisdictionCompliance, _JURISDICTION_REQUIREMENTS
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.EU_GDPR)
        for req in _JURISDICTION_REQUIREMENTS[Jurisdiction.EU_GDPR]:
            jc.mark_completed(req)
        assert jc.compliance_score() == pytest.approx(1.0)


class TestMultiJurisdictionRegistry:
    """MultiJurisdictionRegistry cross-jurisdiction tests."""

    def test_add_jurisdiction(self) -> None:
        from ml.data.compliance import Jurisdiction, MultiJurisdictionRegistry
        registry = MultiJurisdictionRegistry()
        registry.add_jurisdiction(Jurisdiction.USA_HIPAA)
        assert Jurisdiction.USA_HIPAA in registry.jurisdictions

    def test_add_duplicate_no_op(self) -> None:
        from ml.data.compliance import Jurisdiction, MultiJurisdictionRegistry
        registry = MultiJurisdictionRegistry()
        registry.add_jurisdiction(Jurisdiction.EU_GDPR)
        registry.add_jurisdiction(Jurisdiction.EU_GDPR)
        assert len(registry.jurisdictions) == 1

    def test_empty_registry_not_globally_compliant(self) -> None:
        from ml.data.compliance import MultiJurisdictionRegistry
        registry = MultiJurisdictionRegistry()
        assert registry.is_globally_compliant() is False

    def test_global_score_empty(self) -> None:
        from ml.data.compliance import MultiJurisdictionRegistry
        registry = MultiJurisdictionRegistry()
        assert registry.global_score() == 0.0

    def test_globally_compliant_all_met(self) -> None:
        from ml.data.compliance import (
            Jurisdiction, MultiJurisdictionRegistry, _JURISDICTION_REQUIREMENTS,
        )
        registry = MultiJurisdictionRegistry()
        for j in (Jurisdiction.USA_HIPAA, Jurisdiction.EU_GDPR):
            registry.add_jurisdiction(j)
            for req in _JURISDICTION_REQUIREMENTS[j]:
                registry.jurisdictions[j].mark_completed(req)
        assert registry.is_globally_compliant() is True
        assert registry.global_score() == pytest.approx(1.0)

    def test_globally_compliant_partial(self) -> None:
        from ml.data.compliance import (
            Jurisdiction, MultiJurisdictionRegistry, _JURISDICTION_REQUIREMENTS,
        )
        registry = MultiJurisdictionRegistry()
        registry.add_jurisdiction(Jurisdiction.USA_HIPAA)
        for req in _JURISDICTION_REQUIREMENTS[Jurisdiction.USA_HIPAA]:
            registry.jurisdictions[Jurisdiction.USA_HIPAA].mark_completed(req)
        registry.add_jurisdiction(Jurisdiction.BRAZIL_LGPD)  # no completions
        assert registry.is_globally_compliant() is False

    def test_summary_structure(self) -> None:
        from ml.data.compliance import Jurisdiction, MultiJurisdictionRegistry
        registry = MultiJurisdictionRegistry()
        registry.add_jurisdiction(Jurisdiction.USA_HIPAA)
        registry.add_jurisdiction(Jurisdiction.MEXICO_LFPDPPP)
        summary = registry.summary()
        assert summary["jurisdictions_tracked"] == 2
        assert "per_jurisdiction" in summary
        assert "usa_hipaa" in summary["per_jurisdiction"]
        assert "mexico_lfpdppp" in summary["per_jurisdiction"]


# ═══════════════════════════════════════════════════════════════════════════
# Renewal Alert Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestRenewalAlerts:
    """Tests for generate_renewal_alerts function."""

    def test_no_alerts_when_everything_fresh(self) -> None:
        from ml.data.compliance import generate_renewal_alerts, create_compliance_gate
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        form = _make_submitted_cdc_form()
        att, _ = _make_signed_attestation(identity)
        gate = create_compliance_gate(
            researcher=identity, irb=irb, cdc_form=form, attestation=att,
        )
        alerts = generate_renewal_alerts(gate)
        # New IRB and attestation should yield only INFO alerts (far from expiry)
        critical = [a for a in alerts if a.severity == "critical"]
        assert len(critical) == 0

    def test_irb_critical_alert(self) -> None:
        from ml.data.compliance import generate_renewal_alerts
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        # Set expiration to 10 days from now (critical)
        irb.expiration_date = datetime.now(tz=timezone.utc) + timedelta(days=10)
        gate = ComplianceGate(irb_application=irb)
        alerts = generate_renewal_alerts(gate, critical_days=30)
        critical = [a for a in alerts if a.severity == "critical"]
        assert len(critical) >= 1
        assert any("IRB" in a.component for a in critical)

    def test_irb_warning_alert(self) -> None:
        from ml.data.compliance import generate_renewal_alerts
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        irb.expiration_date = datetime.now(tz=timezone.utc) + timedelta(days=60)
        gate = ComplianceGate(irb_application=irb)
        alerts = generate_renewal_alerts(gate, warning_days=90, critical_days=30)
        warning = [a for a in alerts if a.severity == "warning"]
        assert len(warning) >= 1

    def test_attestation_alert(self) -> None:
        from ml.data.compliance import generate_renewal_alerts
        att, _ = _make_signed_attestation()
        att.expires_at = datetime.now(tz=timezone.utc) + timedelta(days=5)
        gate = ComplianceGate(security_attestation=att)
        alerts = generate_renewal_alerts(gate, critical_days=30)
        att_alerts = [a for a in alerts if "Attestation" in a.component]
        assert len(att_alerts) >= 1

    def test_citi_expiring_alert(self) -> None:
        from ml.data.compliance import generate_renewal_alerts, CITI_REQUIRED_MODULES
        now = datetime.now(tz=timezone.utc)
        comps = tuple(
            CITICompletion(
                module_id=m,
                module_name=m.replace("_", " ").title(),
                completion_date=now - timedelta(days=300),
                expiration_date=now + timedelta(days=15),  # expiring soon
                score=95.0,
                certificate_id=f"C-{m[:4].upper()}",
            )
            for m in sorted(CITI_REQUIRED_MODULES)
        )
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=comps,
            verified_at=now,
        )
        gate = ComplianceGate(researcher_identity=identity)
        alerts = generate_renewal_alerts(gate, warning_days=90, critical_days=30)
        citi_alerts = [a for a in alerts if "CITI" in a.component]
        assert len(citi_alerts) > 0

    def test_alerts_sorted_by_urgency(self) -> None:
        from ml.data.compliance import generate_renewal_alerts
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        irb.expiration_date = datetime.now(tz=timezone.utc) + timedelta(days=60)
        att, _ = _make_signed_attestation(identity)
        att.expires_at = datetime.now(tz=timezone.utc) + timedelta(days=10)
        gate = ComplianceGate(irb_application=irb, security_attestation=att)
        alerts = generate_renewal_alerts(gate)
        if len(alerts) >= 2:
            assert alerts[0].days_remaining <= alerts[-1].days_remaining

    def test_no_alerts_empty_gate(self) -> None:
        from ml.data.compliance import generate_renewal_alerts
        gate = ComplianceGate()
        alerts = generate_renewal_alerts(gate)
        assert alerts == []


# ═══════════════════════════════════════════════════════════════════════════
# Jurisdiction Enum Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestJurisdictionEnum:
    """Basic Jurisdiction enum tests."""

    def test_all_jurisdictions_defined(self) -> None:
        from ml.data.compliance import Jurisdiction
        assert len(Jurisdiction) == 5

    def test_jurisdiction_values(self) -> None:
        from ml.data.compliance import Jurisdiction
        assert Jurisdiction.USA_HIPAA.value == "usa_hipaa"
        assert Jurisdiction.EU_GDPR.value == "eu_gdpr"
        assert Jurisdiction.BRAZIL_LGPD.value == "brazil_lgpd"
        assert Jurisdiction.MEXICO_LFPDPPP.value == "mexico_lfpdppp"

    def test_alert_severity_values(self) -> None:
        from ml.data.compliance import AlertSeverity
        assert AlertSeverity.INFO.value == "info"
        assert AlertSeverity.WARNING.value == "warning"
        assert AlertSeverity.CRITICAL.value == "critical"


# ═══════════════════════════════════════════════════════════════════════════
# Final Coverage Completeness — targeting remaining uncovered lines
# ═══════════════════════════════════════════════════════════════════════════


class TestFinalCoverage:
    """Tests targeting the last uncovered lines."""

    def test_irb_is_current_tz_naive_hits_replace(self) -> None:
        """Line 542: irb.is_current returns False when expiration_date is None."""
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        irb.expiration_date = None
        result = irb.is_current()
        assert result is False

    def test_attestation_is_current_tz_naive_hits_replace(self) -> None:
        """Line 1042: attestation.is_current returns False when expires_at is None."""
        att, _ = _make_signed_attestation()
        att.expires_at = None
        assert att.is_current() is False

    def test_jurisdiction_compliance_score_empty_requirements(self) -> None:
        """Line 1440: compliance_score returns 1.0 when no requirements defined."""
        from ml.data.compliance import (
            JurisdictionCompliance,
            Jurisdiction,
            _JURISDICTION_REQUIREMENTS,
        )
        jc = JurisdictionCompliance(jurisdiction=Jurisdiction.USA_HIPAA)
        # Temporarily remove the jurisdiction from the requirements dict
        # to exercise the empty-requirements early return
        saved = _JURISDICTION_REQUIREMENTS[Jurisdiction.USA_HIPAA]
        _JURISDICTION_REQUIREMENTS.pop(Jurisdiction.USA_HIPAA)
        try:
            assert jc.compliance_score() == pytest.approx(1.0)
        finally:
            _JURISDICTION_REQUIREMENTS[Jurisdiction.USA_HIPAA] = saved

    def test_renewal_alerts_irb_tz_naive(self) -> None:
        """Lines 1552, 1578: tz-naive IRB and attestation exp in alerts."""
        from ml.data.compliance import generate_renewal_alerts
        from datetime import datetime as dt_plain
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        # Set tz-naive expiration (5 days from now)
        irb.expiration_date = dt_plain(
            *(datetime.now(tz=timezone.utc) + timedelta(days=5)).timetuple()[:6]
        )
        att, _ = _make_signed_attestation(identity)
        att.expires_at = dt_plain(
            *(datetime.now(tz=timezone.utc) + timedelta(days=5)).timetuple()[:6]
        )
        gate = ComplianceGate(irb_application=irb, security_attestation=att)
        alerts = generate_renewal_alerts(gate, critical_days=30)
        # Should not crash with tz-naive dates
        assert len(alerts) >= 2

    def test_renewal_alerts_irb_info_severity(self) -> None:
        """Line 1560: IRB alert with info severity (far from expiry)."""
        from ml.data.compliance import generate_renewal_alerts
        identity = _make_valid_identity()
        irb = _make_approved_irb(identity)
        irb.expiration_date = datetime.now(tz=timezone.utc) + timedelta(days=500)
        gate = ComplianceGate(irb_application=irb)
        alerts = generate_renewal_alerts(gate, warning_days=90, critical_days=30)
        irb_alerts = [a for a in alerts if "IRB" in a.component]
        assert len(irb_alerts) == 1
        assert irb_alerts[0].severity == "info"
        assert irb_alerts[0].recommended_action == "Monitor expiration date"

    def test_renewal_alerts_attestation_warning_severity(self) -> None:
        """Line 1584: attestation alert with WARNING severity (between critical and warning)."""
        from ml.data.compliance import generate_renewal_alerts
        att, _ = _make_signed_attestation()
        # Set expiration between critical_days and warning_days from now
        att.expires_at = datetime.now(tz=timezone.utc) + timedelta(days=60)
        gate = ComplianceGate(security_attestation=att)
        alerts = generate_renewal_alerts(gate, warning_days=90, critical_days=30)
        att_alerts = [a for a in alerts if "Attestation" in a.component]
        assert len(att_alerts) == 1
        assert att_alerts[0].severity == "warning"

    def test_renewal_alerts_attestation_info_severity(self) -> None:
        """Line 1586: attestation alert with info severity."""
        from ml.data.compliance import generate_renewal_alerts
        att, _ = _make_signed_attestation()
        att.expires_at = datetime.now(tz=timezone.utc) + timedelta(days=500)
        gate = ComplianceGate(security_attestation=att)
        alerts = generate_renewal_alerts(gate, warning_days=90, critical_days=30)
        att_alerts = [a for a in alerts if "Attestation" in a.component]
        assert len(att_alerts) == 1
        assert att_alerts[0].severity == "info"
        assert att_alerts[0].recommended_action == "Monitor expiration date"

    def test_renewal_alerts_citi_warning_severity(self) -> None:
        """Line 1611: CITI alert with WARNING severity (between critical and warning)."""
        from ml.data.compliance import generate_renewal_alerts, CITI_REQUIRED_MODULES
        now = datetime.now(tz=timezone.utc)
        comps = tuple(
            CITICompletion(
                module_id=m,
                module_name=m.replace("_", " ").title(),
                completion_date=now - timedelta(days=300),
                # 60 days from now: between critical(30) and warning(90)
                expiration_date=now + timedelta(days=60),
                score=95.0,
                certificate_id=f"C-{m[:4].upper()}",
            )
            for m in sorted(CITI_REQUIRED_MODULES)
        )
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=comps,
            verified_at=now,
        )
        gate = ComplianceGate(researcher_identity=identity)
        alerts = generate_renewal_alerts(gate, warning_days=90, critical_days=30)
        citi_alerts = [a for a in alerts if "CITI" in a.component]
        assert len(citi_alerts) > 0
        assert all(a.severity == "warning" for a in citi_alerts)

    def test_renewal_alerts_citi_tz_naive(self) -> None:
        """Lines 1605, 1611: CITI expiration with tz-naive datetime."""
        from ml.data.compliance import generate_renewal_alerts, CITI_REQUIRED_MODULES
        from datetime import datetime as dt_plain
        now = datetime.now(tz=timezone.utc)
        comps = tuple(
            CITICompletion(
                module_id=m,
                module_name=m.replace("_", " ").title(),
                completion_date=now - timedelta(days=300),
                # tz-naive, expiring in 10 days
                expiration_date=dt_plain(
                    *(now + timedelta(days=10)).timetuple()[:6]
                ),
                score=95.0,
                certificate_id=f"C-{m[:4].upper()}",
            )
            for m in sorted(CITI_REQUIRED_MODULES)
        )
        identity = ResearcherIdentity(
            orcid="0000-0002-1825-0097",
            full_name="Test",
            email="test@weber.edu",
            institution="Test",
            department="CS",
            citi_completions=comps,
            verified_at=now,
        )
        gate = ComplianceGate(researcher_identity=identity)
        alerts = generate_renewal_alerts(gate, warning_days=90, critical_days=30)
        citi_alerts = [a for a in alerts if "CITI" in a.component]
        assert len(citi_alerts) > 0


# ═══════════════════════════════════════════════════════════════════════════
# Data Protection Impact Assessment Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestDPIAStatus:
    """DPIAStatus and DPIARiskLevel enum tests."""

    def test_dpia_statuses(self) -> None:
        from ml.data.compliance import DPIAStatus
        assert DPIAStatus.DRAFT.value == "draft"
        assert DPIAStatus.APPROVED.value == "approved"
        assert DPIAStatus.REQUIRES_CONSULTATION.value == "requires_consultation"

    def test_risk_levels(self) -> None:
        from ml.data.compliance import DPIARiskLevel
        assert DPIARiskLevel.LOW.value == "low"
        assert DPIARiskLevel.VERY_HIGH.value == "very_high"


class TestDataProtectionImpactAssessment:
    """GDPR Article 35 DPIA tests."""

    def test_default_dpia(self) -> None:
        from ml.data.compliance import (
            DataProtectionImpactAssessment,
            DPIARiskLevel,
            DPIAStatus,
        )
        dpia = DataProtectionImpactAssessment()
        assert dpia.dpia_id.startswith("DPIA-")
        assert dpia.status == DPIAStatus.DRAFT
        assert dpia.overall_risk == DPIARiskLevel.LOW
        assert dpia.dpo_consulted is False

    def test_respond_to_valid_section(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(project_name="Amoeba Study")
        dpia.respond_to_section(
            "DPIA-S01",
            "Processing microscopy images for PAM classification using de-identified records.",
        )
        assert "DPIA-S01" in dpia.section_responses

    def test_respond_to_invalid_section_raises(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment()
        with pytest.raises(ValueError, match="Unknown DPIA section"):
            dpia.respond_to_section("DPIA-S99", "Invalid")

    def test_all_sections_completed(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment()
        assert dpia.all_sections_completed() is False

        long_text = "This is a detailed response with enough words " * 5
        for sid in ("DPIA-S01", "DPIA-S02", "DPIA-S03", "DPIA-S04"):
            dpia.respond_to_section(sid, long_text)
        assert dpia.all_sections_completed() is True

    def test_validate_missing_project_name(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(controller="University X")
        issues = dpia.validate()
        errors = [i for i in issues if i.field_name == "project_name"]
        assert len(errors) == 1
        assert errors[0].severity == "error"

    def test_validate_missing_controller(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(project_name="Study")
        issues = dpia.validate()
        errors = [i for i in issues if i.field_name == "controller"]
        assert len(errors) == 1

    def test_validate_dpo_warning(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(
            project_name="Test", controller="Org",
        )
        issues = dpia.validate()
        dpo_issues = [i for i in issues if i.field_name == "dpo_consulted"]
        assert len(dpo_issues) == 1
        assert dpo_issues[0].severity == "warning"

    def test_validate_brief_response_warning(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(
            project_name="Test", controller="Org", dpo_consulted=True,
        )
        dpia.respond_to_section("DPIA-S01", "Brief.")
        issues = dpia.validate()
        brief = [i for i in issues if "brief" in i.message.lower()]
        assert len(brief) == 1

    def test_validate_very_high_risk_no_dpo(self) -> None:
        from ml.data.compliance import (
            DataProtectionImpactAssessment,
            DPIARiskLevel,
        )
        dpia = DataProtectionImpactAssessment(
            project_name="Test", controller="Org",
        )
        dpia.overall_risk = DPIARiskLevel.VERY_HIGH
        issues = dpia.validate()
        consultation = [i for i in issues if "supervisory" in i.message.lower()]
        assert len(consultation) == 1
        assert consultation[0].severity == "error"

    def test_risk_recomputation_with_mitigations(self) -> None:
        from ml.data.compliance import (
            DataProtectionImpactAssessment,
            DPIARiskLevel,
        )
        dpia = DataProtectionImpactAssessment()
        long_text = "Detailed description of processing activities " * 5

        # Section S03 is HIGH risk, provide all mitigations
        dpia.respond_to_section(
            "DPIA-S03", long_text,
            mitigations=("pseudonymisation", "encryption", "access_controls", "data_minimisation"),
        )
        # With full mitigations, risk should not be HIGH
        assert dpia.overall_risk == DPIARiskLevel.LOW

    def test_risk_recomputation_without_mitigations(self) -> None:
        from ml.data.compliance import (
            DataProtectionImpactAssessment,
            DPIARiskLevel,
        )
        dpia = DataProtectionImpactAssessment()
        long_text = "Processing details " * 10

        # Section S03 is HIGH risk, provide NO mitigations
        dpia.respond_to_section("DPIA-S03", long_text, mitigations=())
        assert dpia.overall_risk == DPIARiskLevel.HIGH

    def test_to_dict(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(
            project_name="Amoebanator", controller="University",
        )
        d = dpia.to_dict()
        assert d["project_name"] == "Amoebanator"
        assert d["controller"] == "University"
        assert d["sections_required"] == 4
        assert d["sections_completed"] == 0
        assert "dpia_id" in d

    def test_validate_missing_sections(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(
            project_name="Test", controller="Org", dpo_consulted=True,
        )
        issues = dpia.validate()
        section_errors = [
            i for i in issues
            if i.field_name.startswith("DPIA-S") and i.severity == "error"
        ]
        assert len(section_errors) == 4  # all 4 sections missing

    def test_full_dpia_no_errors(self) -> None:
        from ml.data.compliance import DataProtectionImpactAssessment
        dpia = DataProtectionImpactAssessment(
            project_name="PAM Classification Study",
            controller="Ensign College",
            dpo_consulted=True,
        )
        long_text = "Comprehensive detailed description of all activities " * 5

        dpia.respond_to_section("DPIA-S01", long_text)
        dpia.respond_to_section(
            "DPIA-S02", long_text,
            mitigations=("data_minimisation", "purpose_limitation"),
        )
        dpia.respond_to_section(
            "DPIA-S03", long_text,
            mitigations=(
                "pseudonymisation", "encryption",
                "access_controls", "data_minimisation",
            ),
        )
        dpia.respond_to_section(
            "DPIA-S04", long_text,
            mitigations=(
                "encryption_at_rest", "encryption_in_transit",
                "audit_logging", "breach_notification",
            ),
        )

        issues = dpia.validate()
        errors = [i for i in issues if i.severity == "error"]
        assert len(errors) == 0


# ═══════════════════════════════════════════════════════════════════════════
# ConsentType Enum Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestConsentType:
    """Verify consent type enum values per 45 CFR 46.116."""

    def test_informed_value(self) -> None:
        assert ConsentType.INFORMED.value == "informed"

    def test_tiered_value(self) -> None:
        assert ConsentType.TIERED.value == "tiered"

    def test_broad_value(self) -> None:
        assert ConsentType.BROAD.value == "broad"

    def test_emergency_waiver_value(self) -> None:
        assert ConsentType.EMERGENCY_WAIVER.value == "emergency_waiver"

    def test_waiver_of_consent_value(self) -> None:
        assert ConsentType.WAIVER_OF_CONSENT.value == "waiver_of_consent"

    def test_member_count(self) -> None:
        assert len(ConsentType) == 5


# ═══════════════════════════════════════════════════════════════════════════
# ConsentStatus Enum Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestConsentStatus:
    """Verify consent status enum values per GDPR Art. 7."""

    def test_active_value(self) -> None:
        assert ConsentStatus.ACTIVE.value == "active"

    def test_withdrawn_value(self) -> None:
        assert ConsentStatus.WITHDRAWN.value == "withdrawn"

    def test_expired_value(self) -> None:
        assert ConsentStatus.EXPIRED.value == "expired"

    def test_superseded_value(self) -> None:
        assert ConsentStatus.SUPERSEDED.value == "superseded"

    def test_member_count(self) -> None:
        assert len(ConsentStatus) == 4


# ═══════════════════════════════════════════════════════════════════════════
# ConsentRecord Dataclass Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestConsentRecord:
    """Verify ConsentRecord construction and default values."""

    def test_default_construction(self) -> None:
        rec = ConsentRecord(subject_id="SUBJ-001")
        assert rec.subject_id == "SUBJ-001"
        assert rec.consent_type == ConsentType.INFORMED
        assert rec.version == "1.0"
        assert rec.status == ConsentStatus.ACTIVE
        assert rec.withdrawn_at is None
        assert rec.withdrawal_reason is None
        assert rec.jurisdiction == "usa_hipaa"
        assert "primary_research" in rec.purposes

    def test_custom_construction(self) -> None:
        rec = ConsentRecord(
            consent_id="CNS-CUSTOM001",
            subject_id="SUBJ-002",
            consent_type=ConsentType.TIERED,
            version="2.1",
            granted_at="2025-01-15T09:00:00+00:00",
            purposes=("primary_research", "secondary_analysis"),
            status=ConsentStatus.ACTIVE,
            jurisdiction="eu_gdpr",
        )
        assert rec.consent_id == "CNS-CUSTOM001"
        assert rec.consent_type == ConsentType.TIERED
        assert rec.version == "2.1"
        assert len(rec.purposes) == 2
        assert rec.jurisdiction == "eu_gdpr"

    def test_consent_id_autogenerated(self) -> None:
        rec = ConsentRecord(subject_id="SUBJ-003")
        assert rec.consent_id.startswith("CNS-")
        assert len(rec.consent_id) == 16  # CNS- + 12 hex chars

    def test_granted_at_autogenerated(self) -> None:
        rec = ConsentRecord(subject_id="SUBJ-004")
        dt = datetime.fromisoformat(rec.granted_at)
        assert dt.tzinfo is not None


# ═══════════════════════════════════════════════════════════════════════════
# ConsentRegistry Tests
# ═══════════════════════════════════════════════════════════════════════════


class TestConsentRegistry:
    """Full lifecycle tests for ConsentRegistry."""

    def test_register_returns_record(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-REG001",
            subject_id="SUBJ-100",
        )
        result = registry.register(rec)
        assert result is rec
        assert "CNS-REG001" in registry.records

    def test_register_empty_subject_raises(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(consent_id="CNS-EMPTY", subject_id="")
        with pytest.raises(ValueError, match="subject_id is required"):
            registry.register(rec)

    def test_register_duplicate_raises(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-DUP001",
            subject_id="SUBJ-200",
        )
        registry.register(rec)
        dup = ConsentRecord(
            consent_id="CNS-DUP001",
            subject_id="SUBJ-201",
        )
        with pytest.raises(ValueError, match="already registered"):
            registry.register(dup)

    def test_withdraw_success(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-WDR001",
            subject_id="SUBJ-300",
        )
        registry.register(rec)
        result = registry.withdraw("CNS-WDR001", reason="Subject request")
        assert result.status == ConsentStatus.WITHDRAWN
        assert result.withdrawn_at is not None
        assert result.withdrawal_reason == "Subject request"

    def test_withdraw_not_found_raises(self) -> None:
        registry = ConsentRegistry()
        with pytest.raises(KeyError, match="not found"):
            registry.withdraw("CNS-NONEXIST")

    def test_withdraw_already_withdrawn_raises(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-WDR002",
            subject_id="SUBJ-301",
        )
        registry.register(rec)
        registry.withdraw("CNS-WDR002")
        with pytest.raises(ValueError, match="already withdrawn"):
            registry.withdraw("CNS-WDR002")

    def test_check_active_consent_returns_true(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-CHK001",
            subject_id="SUBJ-400",
            purposes=("primary_research", "imaging"),
        )
        registry.register(rec)
        assert registry.check("SUBJ-400", "primary_research") is True
        assert registry.check("SUBJ-400", "imaging") is True

    def test_check_no_consent_returns_false(self) -> None:
        registry = ConsentRegistry()
        assert registry.check("SUBJ-NONE", "primary_research") is False

    def test_check_withdrawn_returns_false(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-CHK002",
            subject_id="SUBJ-401",
        )
        registry.register(rec)
        registry.withdraw("CNS-CHK002")
        assert registry.check("SUBJ-401", "primary_research") is False

    def test_check_wrong_purpose_returns_false(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-CHK003",
            subject_id="SUBJ-402",
            purposes=("primary_research",),
        )
        registry.register(rec)
        assert registry.check("SUBJ-402", "commercial_use") is False

    def test_active_consents_returns_only_active(self) -> None:
        registry = ConsentRegistry()
        rec1 = ConsentRecord(
            consent_id="CNS-ACT001",
            subject_id="SUBJ-500",
        )
        rec2 = ConsentRecord(
            consent_id="CNS-ACT002",
            subject_id="SUBJ-500",
            consent_type=ConsentType.BROAD,
        )
        rec3 = ConsentRecord(
            consent_id="CNS-ACT003",
            subject_id="SUBJ-500",
        )
        registry.register(rec1)
        registry.register(rec2)
        registry.register(rec3)
        registry.withdraw("CNS-ACT001")
        active = registry.active_consents("SUBJ-500")
        assert len(active) == 2
        ids = {r.consent_id for r in active}
        assert "CNS-ACT002" in ids
        assert "CNS-ACT003" in ids

    def test_active_consents_empty_for_unknown_subject(self) -> None:
        registry = ConsentRegistry()
        assert registry.active_consents("SUBJ-UNKNOWN") == []

    def test_subject_consent_summary_structure(self) -> None:
        registry = ConsentRegistry()
        rec1 = ConsentRecord(
            consent_id="CNS-SUM001",
            subject_id="SUBJ-600",
            purposes=("primary_research", "imaging"),
            jurisdiction="usa_hipaa",
        )
        rec2 = ConsentRecord(
            consent_id="CNS-SUM002",
            subject_id="SUBJ-600",
            purposes=("secondary_analysis",),
            jurisdiction="eu_gdpr",
        )
        registry.register(rec1)
        registry.register(rec2)
        registry.withdraw("CNS-SUM002", reason="GDPR Art. 17 request")

        summary = registry.subject_consent_summary("SUBJ-600")
        assert summary["subject_id"] == "SUBJ-600"
        assert summary["total_consents"] == 2
        assert summary["active_consents"] == 1
        assert summary["withdrawn_consents"] == 1
        assert "primary_research" in summary["active_purposes"]
        assert "imaging" in summary["active_purposes"]
        assert "secondary_analysis" not in summary["active_purposes"]
        assert "usa_hipaa" in summary["jurisdictions"]
        assert "eu_gdpr" in summary["jurisdictions"]

    def test_subject_consent_summary_no_records(self) -> None:
        registry = ConsentRegistry()
        summary = registry.subject_consent_summary("SUBJ-GHOST")
        assert summary["total_consents"] == 0
        assert summary["active_consents"] == 0
        assert summary["withdrawn_consents"] == 0
        assert summary["active_purposes"] == []

    def test_records_property_returns_copy(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-CPY001",
            subject_id="SUBJ-700",
        )
        registry.register(rec)
        records_copy = registry.records
        records_copy["CNS-INJECTED"] = rec
        assert "CNS-INJECTED" not in registry.records

    def test_withdraw_default_empty_reason(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-DFLT001",
            subject_id="SUBJ-800",
        )
        registry.register(rec)
        result = registry.withdraw("CNS-DFLT001")
        assert result.withdrawal_reason == ""

    def test_multiple_subjects_isolated(self) -> None:
        registry = ConsentRegistry()
        rec_a = ConsentRecord(
            consent_id="CNS-ISO001",
            subject_id="SUBJ-A",
        )
        rec_b = ConsentRecord(
            consent_id="CNS-ISO002",
            subject_id="SUBJ-B",
        )
        registry.register(rec_a)
        registry.register(rec_b)
        assert registry.check("SUBJ-A", "primary_research") is True
        assert registry.check("SUBJ-B", "primary_research") is True
        registry.withdraw("CNS-ISO001")
        assert registry.check("SUBJ-A", "primary_research") is False
        assert registry.check("SUBJ-B", "primary_research") is True

    def test_check_default_purpose(self) -> None:
        registry = ConsentRegistry()
        rec = ConsentRecord(
            consent_id="CNS-DEF001",
            subject_id="SUBJ-900",
        )
        registry.register(rec)
        assert registry.check("SUBJ-900") is True
