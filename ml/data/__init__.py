"""
ml.data - data-pipeline modules.

Six modules are imported and re-exported at the package level; audit_trail and
deidentification have their own unit tests. Three are used by the rest of the
codebase: audit_trail (ml.audit_hooks,
ml.data_loader, ml.irb_gate, the audit export and the predict page),
deidentification (ml.data_loader) and compliance (ml.irb_gate). acquisition,
clinical and microscopy are not used by this release.

  * audit_trail        - hash-chained, Merkle-checkpointed audit log
                         (wired via ml.audit_hooks)
  * acquisition        - CDC data transfer, manifests, retry/circuit-breaker
                         policies
  * clinical           - clinical record parsing and validation
  * compliance         - IRB / CITI / safeguard state machines
                         (wired via ml.irb_gate)
  * deidentification   - HIPAA Safe Harbor processor
                         (wired via ml.data_loader)
  * microscopy         - image loading and preprocessing primitives
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
from ml.data.acquisition import (
    CDCDataClient,
    ChecksumCalculator,
    CircuitBreaker,
    CircuitBreakerConfig,
    CircuitOpenError,
    CircuitState,
    DataCategory,
    ManifestEntry,
    ManifestParser,
    ResilientCDCClient,
    RetryConfig,
    RetryPolicy,
    TelemetryEmitter,
    TelemetryEvent,
    TransferConfig,
    TransferMetrics,
    TransferResult,
    TransferStatus,
)
from ml.data.clinical import (
    ClinicalRecord,
    ClinicalRecordParser,
    CSVRecordParser,
    ParserConfig,
    RecordValidator,
    ValidationResult,
    ValidationSeverity,
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
from ml.data.microscopy import (
    AugmentationConfig,
    ImageMetadata,
    ImageNormalizer,
    PreprocessingConfig,
    QualityFilter,
    QualityLevel,
    QualityThresholds,
    StainType,
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
    # Acquisition
    "CDCDataClient",
    "ChecksumCalculator",
    "CircuitBreaker",
    "CircuitBreakerConfig",
    "CircuitOpenError",
    "CircuitState",
    "DataCategory",
    "ManifestEntry",
    "ManifestParser",
    "ResilientCDCClient",
    "RetryConfig",
    "RetryPolicy",
    "TelemetryEmitter",
    "TelemetryEvent",
    "TransferConfig",
    "TransferMetrics",
    "TransferResult",
    "TransferStatus",
    # Clinical
    "ClinicalRecord",
    "ClinicalRecordParser",
    "CSVRecordParser",
    "ParserConfig",
    "RecordValidator",
    "ValidationResult",
    "ValidationSeverity",
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
    # Microscopy
    "AugmentationConfig",
    "ImageMetadata",
    "ImageNormalizer",
    "PreprocessingConfig",
    "QualityFilter",
    "QualityLevel",
    "QualityThresholds",
    "StainType",
]
