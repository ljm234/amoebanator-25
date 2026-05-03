"""ml.schemas — Pydantic v2 vignette schema for 9-class meningitis/encephalitis
differential diagnosis (Amoebanator V1.0).

Public API:
    ClassLabel  — IntEnum for 9 ground-truth diagnostic classes
    VignetteSchema  — top-level vignette container with cross-field validators

Sub-models:
    Demographics, History, ExposureHistory, VitalSigns, PhysicalExam, Labs,
    CSFProfile, Imaging, DxResult, DiagnosticTests, AdjudicationMetadata,
    LiteratureAnchor, Provenance
"""
from ml.schemas.labels import ClassLabel
from ml.schemas.vignette import (
    Demographics,
    History,
    ExposureHistory,
    VitalSigns,
    PhysicalExam,
    Labs,
    CSFProfile,
    Imaging,
    DxResult,
    DiagnosticTests,
    AdjudicationMetadata,
    LiteratureAnchor,
    Provenance,
    VignetteSchema,
)

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
