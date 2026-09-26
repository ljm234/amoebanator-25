"""
ml.data - data-pipeline modules.

Three modules are imported and re-exported at the package level:

  * audit_trail        - hash-chained, Merkle-checkpointed audit log, used by
                         ml.audit_hooks, ml.data_loader, ml.irb_gate, the
                         audit export and the predict page
  * compliance         - IRB / CITI / safeguard state machines, used by
                         ml.irb_gate
  * deidentification   - HIPAA Safe Harbor processor, used by ml.data_loader

audit_trail and deidentification have their own unit tests.
"""
from __future__ import annotations

from ml.data.audit_trail import (
    AuditEntry,
    AuditEventType,
    AuditLog,
    DataProvenance,
    IntegrityStatus,
    MerkleCheckpoint,
    MerkleTree,
    create_audit_log,
    create_provenance_tracker,
)
from ml.data.compliance import (
    ALL_SAFEGUARDS,
    AttestationStatus,
    CDCDataRequestForm,
    CDCFormStatus,
    CITICompletion,
    ComplianceGate,
    ComplianceGateResult,
    IRBApplication,
    IRBStatus,
    IRBTransition,
    ResearcherIdentity,
    ResearcherValidator,
    SafeguardCategory,
    SafeguardCheck,
    SecurityAttestation,
    ValidationIssue as ComplianceValidationIssue,
    create_compliance_gate,
    create_irb_application,
    create_researcher_identity,
)
from ml.data.deidentification import (
    DeidentificationAction,
    DeidentificationConfig,
    DeidentificationMethod,
    DeidentificationPipeline,
    DeidentificationReport,
    ExponentialMechanism,
    GaussianMechanism,
    KAnonymityConfig,
    KAnonymityProcessor,
    LaplaceMechanism,
    PrivacyBudget,
    PrivacyLevel,
    SafeHarborConfig,
    SafeHarborProcessor,
    create_deidentification_pipeline,
)

__all__ = [
    # Audit Trail
    "AuditEntry",
    "AuditEventType",
    "AuditLog",
    "DataProvenance",
    "IntegrityStatus",
    "MerkleCheckpoint",
    "MerkleTree",
    "create_audit_log",
    "create_provenance_tracker",
    # Compliance
    "ALL_SAFEGUARDS",
    "AttestationStatus",
    "CDCDataRequestForm",
    "CDCFormStatus",
    "CITICompletion",
    "ComplianceGate",
    "ComplianceGateResult",
    "ComplianceValidationIssue",
    "IRBApplication",
    "IRBStatus",
    "IRBTransition",
    "ResearcherIdentity",
    "ResearcherValidator",
    "SafeguardCategory",
    "SafeguardCheck",
    "SecurityAttestation",
    "create_compliance_gate",
    "create_irb_application",
    "create_researcher_identity",
    # De-identification
    "DeidentificationAction",
    "DeidentificationConfig",
    "DeidentificationMethod",
    "DeidentificationPipeline",
    "DeidentificationReport",
    "ExponentialMechanism",
    "GaussianMechanism",
    "KAnonymityConfig",
    "KAnonymityProcessor",
    "LaplaceMechanism",
    "PrivacyBudget",
    "PrivacyLevel",
    "SafeHarborConfig",
    "SafeHarborProcessor",
    "create_deidentification_pipeline",
]
