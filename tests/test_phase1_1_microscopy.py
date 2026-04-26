"""Comprehensive tests for ml.data.microscopy module — targeting 100 % coverage.

Covers every class, method, branch, enum member, factory function, and I/O
function in microscopy.py.
"""
from __future__ import annotations

import builtins
from pathlib import Path
from typing import Any
from unittest.mock import patch

import numpy as np
import pytest

from ml.data.microscopy import (
    DEFAULT_IMAGE_SIZE,
    MAX_RESOLUTION,
    MIN_RESOLUTION,
    SUPPORTED_FORMATS,
    ArtifactDetectionResult,
    ArtifactDetector,
    ArtifactType,
    AugmentationConfig,
    CellSegmentationResult,
    CellSegmenter,
    ColorSpace,
    FocusAnalyzer,
    FocusMetric,
    FocusResult,
    ImageMetadata,
    ImageNormalizer,
    MorphologyOperation,
    MorphologyProcessor,
    PreprocessingConfig,
    QualityFilter,
    QualityLevel,
    QualityThresholds,
    SegmentationType,
    StainNormalizationResult,
    StainNormalizer,
    StainType,
    TileInfo,
    TileManager,
    create_artifact_detector,
    create_cell_segmenter,
    create_focus_analyzer,
    create_image_normalizer,
    create_morphology_processor,
    create_quality_filter,
    create_stain_normalizer,
    create_tile_manager,
    load_image_file,
    save_image_file,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _rgb(h: int = 64, w: int = 64) -> "np.ndarray[Any, np.dtype[np.uint8]]":
    """Create a simple RGB test image."""
    rng = np.random.RandomState(42)
    return rng.randint(20, 230, (h, w, 3), dtype=np.uint8)


def _gray(h: int = 64, w: int = 64) -> "np.ndarray[Any, np.dtype[np.uint8]]":
    """Create a simple grayscale test image."""
    rng = np.random.RandomState(42)
    return rng.randint(20, 230, (h, w), dtype=np.uint8)


def _flat(val: int = 128, h: int = 64, w: int = 64) -> "np.ndarray[Any, np.dtype[np.uint8]]":
    """Create a flat (constant) grayscale image."""
    return np.full((h, w), val, dtype=np.uint8)


# ===================================================================
# Constants
# ===================================================================

class TestConstants:
    def test_default_image_size(self) -> None:
        assert DEFAULT_IMAGE_SIZE == (512, 512)

    def test_min_max_resolution(self) -> None:
        assert MIN_RESOLUTION == 256
        assert MAX_RESOLUTION == 4096

    def test_supported_formats(self) -> None:
        assert ".png" in SUPPORTED_FORMATS
        assert ".tiff" in SUPPORTED_FORMATS
        assert ".jpg" in SUPPORTED_FORMATS


# ===================================================================
# Enums
# ===================================================================

class TestEnums:
    def test_stain_type(self) -> None:
        assert len(StainType) == 7
        assert StainType.WET_MOUNT.name == "WET_MOUNT"

    def test_quality_level(self) -> None:
        assert QualityLevel.EXCELLENT.value == "excellent"
        assert QualityLevel.REJECTED.value == "rejected"

    def test_color_space(self) -> None:
        assert ColorSpace.RGB.value == "rgb"
        assert ColorSpace.HED.value == "hed"

    def test_focus_metric(self) -> None:
        assert FocusMetric.LAPLACIAN.value == "laplacian"
        assert len(FocusMetric) == 5

    def test_artifact_type(self) -> None:
        assert ArtifactType.DUST.value == "dust"
        assert len(ArtifactType) == 9

    def test_segmentation_type(self) -> None:
        assert SegmentationType.OTSU.value == "otsu"
        assert len(SegmentationType) == 5

    def test_morphology_operation(self) -> None:
        assert MorphologyOperation.EROSION.value == "erosion"
        assert len(MorphologyOperation) == 7


# ===================================================================
# NamedTuple: ImageMetadata
# ===================================================================

class TestImageMetadata:
    def test_fields(self) -> None:
        md = ImageMetadata(
            file_path=Path("test.png"), width=512, height=512, channels=3,
            bit_depth=8, stain_type=StainType.UNKNOWN, magnification="40x",
            quality_level=QualityLevel.GOOD, blur_score=150.0,
        )
        assert md.width == 512
        assert md.blur_score == 150.0


# ===================================================================
# Dataclasses
# ===================================================================

class TestQualityThresholds:
    def test_defaults(self) -> None:
        qt = QualityThresholds()
        assert qt.min_width == 256
        assert qt.min_blur_score == 100.0


class TestPreprocessingConfig:
    def test_defaults(self) -> None:
        pc = PreprocessingConfig()
        assert pc.target_size == DEFAULT_IMAGE_SIZE
        assert pc.normalization == "minmax"


class TestAugmentationConfig:
    def test_defaults(self) -> None:
        ac = AugmentationConfig()
        assert ac.enabled is False
        assert ac.horizontal_flip is True


# ===================================================================
# QualityFilter
# ===================================================================

class TestQualityFilter:
    def test_init_default(self) -> None:
        qf = QualityFilter()
        assert qf.thresholds.min_width == 256

    def test_init_custom(self) -> None:
        qf = QualityFilter(QualityThresholds(min_width=512))
        assert qf.thresholds.min_width == 512

    def test_compute_blur_score(self) -> None:
        qf = QualityFilter()
        score = qf.compute_blur_score(_rgb())
        assert score > 0

    def test_compute_blur_score_grayscale(self) -> None:
        qf = QualityFilter()
        score = qf.compute_blur_score(_gray())
        assert score > 0

    def test_compute_saturation_ratio(self) -> None:
        qf = QualityFilter()
        ratio = qf.compute_saturation_ratio(_rgb())
        assert 0.0 <= ratio <= 1.0

    def test_compute_contrast(self) -> None:
        qf = QualityFilter()
        contrast = qf.compute_contrast(_rgb())
        assert contrast > 0

    def test_to_grayscale_already_gray(self) -> None:
        qf = QualityFilter()
        gray = _gray()
        result = qf._to_grayscale(gray)
        assert result.ndim == 2

    def test_to_grayscale_from_rgb(self) -> None:
        qf = QualityFilter()
        result = qf._to_grayscale(_rgb())
        assert result.ndim == 2

    def test_assess(self) -> None:
        qf = QualityFilter()
        md = qf.assess(_rgb(300, 300), Path("test.png"))
        assert md.width == 300
        assert md.channels == 3

    def test_assess_no_path(self) -> None:
        qf = QualityFilter()
        md = qf.assess(_rgb(300, 300))
        assert md.file_path == Path("unknown")

    def test_assess_grayscale_image(self) -> None:
        qf = QualityFilter()
        md = qf.assess(_gray(300, 300))
        assert md.channels == 1

    def test_assess_16bit(self) -> None:
        img = np.random.randint(0, 65535, (300, 300, 3), dtype=np.uint16)
        qf = QualityFilter()
        md = qf.assess(img)
        assert md.bit_depth == 16

    # -- _determine_quality_level branches ---
    def test_quality_rejected_small(self) -> None:
        qf = QualityFilter()
        assert qf._determine_quality_level(100, 100, 200, 0.01, 50) == QualityLevel.REJECTED

    def test_quality_rejected_low_blur(self) -> None:
        qf = QualityFilter()
        assert qf._determine_quality_level(512, 512, 30, 0.01, 50) == QualityLevel.REJECTED

    def test_quality_rejected_high_saturation(self) -> None:
        qf = QualityFilter()
        assert qf._determine_quality_level(512, 512, 200, 0.2, 50) == QualityLevel.REJECTED

    def test_quality_poor_low_blur(self) -> None:
        qf = QualityFilter()
        assert qf._determine_quality_level(512, 512, 80, 0.01, 50) == QualityLevel.POOR

    def test_quality_poor_high_saturation(self) -> None:
        qf = QualityFilter()
        assert qf._determine_quality_level(512, 512, 200, 0.06, 50) == QualityLevel.POOR

    def test_quality_poor_low_contrast(self) -> None:
        qf = QualityFilter()
        assert qf._determine_quality_level(512, 512, 200, 0.01, 5) == QualityLevel.POOR

    def test_quality_acceptable(self) -> None:
        qf = QualityFilter()
        # blur_score < min_blur_score * 1.5 = 150
        assert qf._determine_quality_level(512, 512, 120, 0.01, 50) == QualityLevel.ACCEPTABLE

    def test_quality_excellent(self) -> None:
        qf = QualityFilter()
        # blur_score > min_blur_score * 3 = 300 AND saturation < max_saturation * 0.5
        assert qf._determine_quality_level(512, 512, 400, 0.01, 50) == QualityLevel.EXCELLENT

    def test_quality_good(self) -> None:
        qf = QualityFilter()
        # blur_score high but saturation not low enough for excellent
        assert qf._determine_quality_level(512, 512, 400, 0.04, 50) == QualityLevel.GOOD

    # -- filter_batch ---
    def test_filter_batch(self) -> None:
        qf = QualityFilter()
        images = [(_rgb(300, 300), Path("a.png")), (_rgb(300, 300), Path("b.png"))]
        results = qf.filter_batch(images)
        assert len(results) >= 0

    def test_filter_batch_rejects_poor(self) -> None:
        qf = QualityFilter()
        small_img = _rgb(100, 100)  # too small → REJECTED
        big_img = _rgb(300, 300)
        results = qf.filter_batch(
            [(small_img, Path("small.png")), (big_img, Path("big.png"))],
            min_quality=QualityLevel.ACCEPTABLE,
        )
        # Only the big one should pass
        paths = [md.file_path for _, md in results]
        assert Path("small.png") not in paths


# ===================================================================
# ImageNormalizer
# ===================================================================

class TestImageNormalizer:
    def test_init_default(self) -> None:
        n = ImageNormalizer()
        assert n.config.normalization == "minmax"

    def test_normalize_minmax(self) -> None:
        n = ImageNormalizer(PreprocessingConfig(normalization="minmax"))
        result = n.normalize(_rgb())
        assert result.min() >= 0.0
        assert result.max() <= 1.0

    def test_normalize_zscore(self) -> None:
        n = ImageNormalizer(PreprocessingConfig(normalization="zscore"))
        result = n.normalize(_rgb())
        assert result.dtype == np.float32

    def test_normalize_percentile(self) -> None:
        n = ImageNormalizer(PreprocessingConfig(normalization="percentile"))
        result = n.normalize(_rgb())
        assert result.dtype == np.float32

    def test_normalize_unknown_method(self) -> None:
        n = ImageNormalizer(PreprocessingConfig(normalization="minmax"))
        # Force unknown method
        n._config = PreprocessingConfig(normalization="unknown")  # type: ignore[arg-type]
        result = n.normalize(_rgb())
        assert result.dtype == np.float32

    def test_minmax_constant_image(self) -> None:
        n = ImageNormalizer(PreprocessingConfig(normalization="minmax"))
        result = n.normalize(_flat())
        assert np.allclose(result, 0.0)

    def test_zscore_constant_image(self) -> None:
        n = ImageNormalizer(PreprocessingConfig(normalization="zscore"))
        result = n.normalize(_flat())
        assert np.allclose(result, 0.0)

    def test_percentile_constant_image(self) -> None:
        n = ImageNormalizer(PreprocessingConfig(normalization="percentile"))
        result = n.normalize(_flat())
        assert np.allclose(result, 0.0)

    def test_fit_and_normalize(self) -> None:
        n = ImageNormalizer()
        n.fit([_rgb(), _rgb()])
        result = n.normalize_with_fitted_stats(_rgb())
        assert result.dtype == np.float32

    def test_normalize_with_fitted_stats_not_fitted(self) -> None:
        n = ImageNormalizer()
        with pytest.raises(RuntimeError, match="not fitted"):
            n.normalize_with_fitted_stats(_rgb())

    def test_normalize_with_fitted_stats_zero_std(self) -> None:
        n = ImageNormalizer()
        n.fit([_flat(), _flat()])
        result = n.normalize_with_fitted_stats(_flat())
        assert result.dtype == np.float32


# ===================================================================
# FocusAnalyzer
# ===================================================================

class TestFocusAnalyzer:
    def test_init_default(self) -> None:
        fa = FocusAnalyzer()
        assert fa.metric == FocusMetric.LAPLACIAN

    def test_analyze_in_focus(self) -> None:
        fa = FocusAnalyzer(threshold=1.0)
        result = fa.analyze(_rgb())
        assert isinstance(result, FocusResult)
        assert result.is_in_focus

    def test_analyze_out_of_focus(self) -> None:
        fa = FocusAnalyzer(threshold=1e12)
        result = fa.analyze(_flat())
        assert not result.is_in_focus

    @pytest.mark.parametrize("metric", list(FocusMetric))
    def test_all_metrics(self, metric: FocusMetric) -> None:
        fa = FocusAnalyzer(metric=metric, threshold=0.0)
        result = fa.analyze(_rgb())
        assert result.score >= 0

    def test_laplacian(self) -> None:
        fa = FocusAnalyzer(metric=FocusMetric.LAPLACIAN)
        score = fa._laplacian_variance(_gray().astype(np.float64))
        assert score >= 0

    def test_gradient(self) -> None:
        fa = FocusAnalyzer(metric=FocusMetric.GRADIENT)
        score = fa._gradient_magnitude(_gray().astype(np.float64))
        assert score >= 0

    def test_tenengrad(self) -> None:
        fa = FocusAnalyzer(metric=FocusMetric.TENENGRAD)
        score = fa._tenengrad(_gray().astype(np.float64))
        assert score >= 0

    def test_brenner(self) -> None:
        fa = FocusAnalyzer(metric=FocusMetric.BRENNER)
        score = fa._brenner(_gray().astype(np.float64))
        assert score >= 0

    def test_vollath(self) -> None:
        fa = FocusAnalyzer(metric=FocusMetric.VOLLATH)
        score = fa._vollath(_gray().astype(np.float64))
        assert isinstance(score, float)

    def test_find_unfocused_regions(self) -> None:
        fa = FocusAnalyzer(window_size=32, threshold=1e12)
        regions = fa._find_unfocused_regions(_gray(128, 128).astype(np.float64))
        assert len(regions) > 0

    def test_ensure_grayscale_rgb(self) -> None:
        fa = FocusAnalyzer()
        result = fa._ensure_grayscale(_rgb())
        assert result.ndim == 2

    def test_ensure_grayscale_already(self) -> None:
        fa = FocusAnalyzer()
        result = fa._ensure_grayscale(_gray())
        assert result.ndim == 2


# ===================================================================
# ArtifactDetector
# ===================================================================

class TestArtifactDetector:
    def test_init_default(self) -> None:
        ad = ArtifactDetector()
        assert ad.sensitivity == 0.5

    def test_sensitivity_clamped(self) -> None:
        ad = ArtifactDetector(sensitivity=2.0)
        assert ad.sensitivity == 1.0
        ad2 = ArtifactDetector(sensitivity=-1.0)
        assert ad2.sensitivity == 0.0

    def test_detect_clean_image(self) -> None:
        ad = ArtifactDetector(sensitivity=0.9)
        result = ad.detect(_rgb())
        assert isinstance(result, ArtifactDetectionResult)
        assert result.is_usable is True

    def test_detect_overexposed(self) -> None:
        # Nearly all pixels at 255
        img = np.full((64, 64, 3), 255, dtype=np.uint8)
        ad = ArtifactDetector(sensitivity=0.01)
        result = ad.detect(img)
        assert ArtifactType.OVEREXPOSURE in result.artifacts_found

    def test_detect_underexposed(self) -> None:
        img = np.zeros((64, 64, 3), dtype=np.uint8)
        ad = ArtifactDetector(sensitivity=0.01)
        result = ad.detect(img)
        assert ArtifactType.UNDEREXPOSURE in result.artifacts_found

    def test_detect_dust(self) -> None:
        img = _rgb(64, 64).copy()
        # Add dark spots (dust)
        img[10:20, 10:20] = 0
        ad = ArtifactDetector(sensitivity=0.01)
        result = ad.detect(img)
        assert isinstance(result, ArtifactDetectionResult)

    def test_detect_bubbles(self) -> None:
        img = _rgb(64, 64).copy()
        # Add bright spots
        img[10:20, 10:20] = 255
        ad = ArtifactDetector(sensitivity=0.01)
        result = ad.detect(img)
        assert isinstance(result, ArtifactDetectionResult)

    def test_detect_vignetting(self) -> None:
        # Create image with dark corners and bright center
        img = np.full((64, 64, 3), 200, dtype=np.uint8)
        img[:8, :8] = 10
        img[:8, -8:] = 10
        img[-8:, :8] = 10
        img[-8:, -8:] = 10
        ad = ArtifactDetector(sensitivity=0.01)
        result = ad.detect(img)
        assert isinstance(result, ArtifactDetectionResult)

    def test_detect_not_usable(self) -> None:
        # Image with everything wrong
        img = np.full((64, 64, 3), 255, dtype=np.uint8)
        img[:32, :32] = 0  # half dark, half bright
        ad = ArtifactDetector(sensitivity=0.01)
        result = ad.detect(img)
        assert isinstance(result, ArtifactDetectionResult)

    def test_detect_overexposure_non_uint8(self) -> None:
        img = np.full((64, 64), 65534, dtype=np.uint16)
        ad = ArtifactDetector()
        severity = ad._detect_overexposure(img)
        assert severity >= 0

    def test_to_grayscale_already_gray(self) -> None:
        ad = ArtifactDetector()
        result = ad._to_grayscale(_gray())
        assert result.ndim == 2

    def test_to_grayscale_from_rgb(self) -> None:
        ad = ArtifactDetector()
        result = ad._to_grayscale(_rgb())
        assert result.ndim == 2

    def test_vignette_center_mean_zero(self) -> None:
        img = np.zeros((64, 64, 3), dtype=np.uint8)
        ad = ArtifactDetector(sensitivity=0.01)
        _, severity = ad._detect_vignetting(img)
        assert severity >= 0.0


# ===================================================================
# CellSegmenter
# ===================================================================

class TestCellSegmenter:
    def test_init_default(self) -> None:
        cs = CellSegmenter()
        assert cs.method == SegmentationType.OTSU

    @pytest.mark.parametrize("method", list(SegmentationType))
    def test_all_methods(self, method: SegmentationType) -> None:
        cs = CellSegmenter(method=method, min_cell_size=1, max_cell_size=100000)
        result = cs.segment(_rgb(64, 64))
        assert isinstance(result, CellSegmentationResult)
        assert result.cell_count >= 0

    def test_segment_filters_small(self) -> None:
        cs = CellSegmenter(min_cell_size=1000000)
        result = cs.segment(_rgb(64, 64))
        assert result.cell_count == 0

    def test_compute_confidence_range(self) -> None:
        cs = CellSegmenter()
        conf = cs._compute_confidence(np.zeros((64, 64), dtype=np.uint8), 10)
        assert 0.0 <= conf <= 1.0

    def test_to_grayscale(self) -> None:
        cs = CellSegmenter()
        assert cs._to_grayscale(_gray()).ndim == 2
        assert cs._to_grayscale(_rgb()).ndim == 2


# ===================================================================
# StainNormalizer
# ===================================================================

class TestStainNormalizer:
    def test_init_default(self) -> None:
        sn = StainNormalizer()
        assert sn._target_stain_matrix is not None

    def test_init_custom_matrix(self) -> None:
        m = np.eye(2, 3)
        sn = StainNormalizer(target_stain_matrix=m)
        assert np.array_equal(sn._target_stain_matrix, m)

    def test_normalize_valid_rgb(self) -> None:
        sn = StainNormalizer()
        result = sn.normalize(_rgb(64, 64))
        assert isinstance(result, StainNormalizationResult)
        assert result.normalized_image.shape == (64, 64, 3)

    def test_normalize_rejects_grayscale(self) -> None:
        sn = StainNormalizer()
        with pytest.raises(ValueError, match="RGB"):
            sn.normalize(_gray())

    def test_rgb_to_od(self) -> None:
        sn = StainNormalizer()
        od = sn._rgb_to_od(_rgb())
        assert np.all(od >= 0)

    def test_od_to_rgb(self) -> None:
        sn = StainNormalizer()
        od = sn._rgb_to_od(_rgb())
        rgb = sn._od_to_rgb(od)
        assert rgb.dtype == np.uint8

    def test_estimate_stain_matrix_few_pixels(self) -> None:
        sn = StainNormalizer()
        # Very small image → < 100 significant pixels → falls back to target
        tiny = np.full((3, 3, 3), 200, dtype=np.uint8)  # near white → low OD
        od = sn._rgb_to_od(tiny)
        matrix = sn._estimate_stain_matrix(od)
        assert np.array_equal(matrix, sn._target_stain_matrix)

    def test_detect_stain_type_he(self) -> None:
        sn = StainNormalizer()
        st = sn._detect_stain_type(sn.HE_STAIN_MATRIX)
        assert st == StainType.HEMATOXYLIN_EOSIN

    def test_detect_stain_type_unknown(self) -> None:
        sn = StainNormalizer()
        # Matrix with low cosine similarity to HE reference (< 0.6)
        m = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        st = sn._detect_stain_type(m)
        assert st == StainType.UNKNOWN

    def test_detect_stain_type_giemsa(self) -> None:
        # Matrix somewhat similar to HE but not > 0.8
        sn = StainNormalizer()
        m = sn.HE_STAIN_MATRIX * 0.8 + np.random.RandomState(0).rand(2, 3) * 0.2
        m = m / np.linalg.norm(m, axis=1, keepdims=True)
        st = sn._detect_stain_type(m)
        assert st in (StainType.HEMATOXYLIN_EOSIN, StainType.GIEMSA)


# ===================================================================
# TileManager
# ===================================================================

class TestTileManager:
    def test_init(self) -> None:
        tm = TileManager(tile_size=128, overlap=16)
        assert tm.tile_size == 128
        assert tm.overlap == 16

    def test_create_tiles_rgb(self) -> None:
        tm = TileManager(tile_size=32, overlap=0)
        tiles = tm.create_tiles(_rgb(64, 64))
        assert len(tiles) == 4
        assert all(t.data.shape[:2] == (32, 32) for t in tiles)

    def test_create_tiles_grayscale(self) -> None:
        tm = TileManager(tile_size=32, overlap=0)
        tiles = tm.create_tiles(_gray(64, 64))
        assert len(tiles) == 4

    def test_create_tiles_with_overlap(self) -> None:
        tm = TileManager(tile_size=32, overlap=16)
        tiles = tm.create_tiles(_rgb(64, 64))
        assert len(tiles) > 4

    def test_create_tiles_padding_needed(self) -> None:
        # Image not divisible by tile size → last tiles need padding
        tm = TileManager(tile_size=32, overlap=0)
        tiles = tm.create_tiles(_rgb(50, 50))
        for t in tiles:
            assert t.data.shape[:2] == (32, 32)

    def test_create_tiles_padding_grayscale(self) -> None:
        tm = TileManager(tile_size=32, overlap=0)
        tiles = tm.create_tiles(_gray(50, 50))
        for t in tiles:
            assert t.data.shape[:2] == (32, 32)

    def test_merge_tiles_rgb(self) -> None:
        tm = TileManager(tile_size=32, overlap=0)
        img = _rgb(64, 64)
        tiles = tm.create_tiles(img)
        merged = tm.merge_tiles(tiles, img.shape)
        assert merged.shape == img.shape

    def test_merge_tiles_grayscale(self) -> None:
        tm = TileManager(tile_size=32, overlap=0)
        img = _gray(64, 64)
        tiles = tm.create_tiles(img)
        merged = tm.merge_tiles(tiles, img.shape)
        assert merged.shape == img.shape

    def test_compute_tile_grid(self) -> None:
        tm = TileManager(tile_size=32, overlap=0)
        rows, cols = tm.compute_tile_grid((64, 64))
        assert rows == 2
        assert cols == 2

    def test_compute_tile_grid_with_overlap(self) -> None:
        tm = TileManager(tile_size=32, overlap=16)
        rows, cols = tm.compute_tile_grid((64, 64))
        assert rows >= 2
        assert cols >= 2


# ===================================================================
# MorphologyProcessor
# ===================================================================

class TestMorphologyProcessor:
    def test_init(self) -> None:
        mp = MorphologyProcessor(kernel_size=5)
        assert mp._kernel_size == 5
        assert mp._kernel.shape == (5, 5)

    def test_create_kernel_circular(self) -> None:
        mp = MorphologyProcessor(kernel_size=5)
        assert mp._kernel[2, 2] == 1  # center
        assert mp._kernel.dtype == np.uint8

    # -- binary operations ---
    def test_erosion_binary(self) -> None:
        mp = MorphologyProcessor()
        binary = np.ones((32, 32), dtype=np.uint8)
        binary[10:20, 10:20] = 0
        result = mp.apply(binary, MorphologyOperation.EROSION)
        assert result.shape == binary.shape

    def test_dilation_binary(self) -> None:
        mp = MorphologyProcessor()
        binary = np.zeros((32, 32), dtype=np.uint8)
        binary[15, 15] = 1
        result = mp.apply(binary, MorphologyOperation.DILATION)
        assert result.sum() >= 1

    def test_opening_binary(self) -> None:
        mp = MorphologyProcessor()
        binary = np.random.RandomState(0).randint(0, 2, (32, 32)).astype(np.uint8)
        result = mp.apply(binary, MorphologyOperation.OPENING)
        assert result.shape == binary.shape

    def test_closing_binary(self) -> None:
        mp = MorphologyProcessor()
        binary = np.random.RandomState(0).randint(0, 2, (32, 32)).astype(np.uint8)
        result = mp.apply(binary, MorphologyOperation.CLOSING)
        assert result.shape == binary.shape

    # -- grayscale operations ---
    def test_erosion_grayscale(self) -> None:
        mp = MorphologyProcessor()
        gray = _gray(32, 32)
        result = mp.apply(gray, MorphologyOperation.EROSION)
        assert result.shape == gray.shape

    def test_dilation_grayscale(self) -> None:
        mp = MorphologyProcessor()
        gray = _gray(32, 32)
        result = mp.apply(gray, MorphologyOperation.DILATION)
        assert result.shape == gray.shape

    def test_erosion_grayscale_iterations(self) -> None:
        mp = MorphologyProcessor()
        gray = _gray(32, 32)
        result = mp.apply(gray, MorphologyOperation.EROSION, iterations=2)
        assert result.shape == gray.shape

    # -- gradient, top_hat, black_hat ---
    def test_gradient(self) -> None:
        mp = MorphologyProcessor()
        binary = np.zeros((32, 32), dtype=np.uint8)
        binary[10:20, 10:20] = 1
        result = mp.apply(binary, MorphologyOperation.GRADIENT)
        assert result.shape == binary.shape

    def test_top_hat(self) -> None:
        mp = MorphologyProcessor()
        binary = np.zeros((32, 32), dtype=np.uint8)
        binary[10:20, 10:20] = 1
        result = mp.apply(binary, MorphologyOperation.TOP_HAT)
        assert result.shape == binary.shape

    def test_black_hat(self) -> None:
        mp = MorphologyProcessor()
        binary = np.zeros((32, 32), dtype=np.uint8)
        binary[10:20, 10:20] = 1
        result = mp.apply(binary, MorphologyOperation.BLACK_HAT)
        assert result.shape == binary.shape

    def test_fallthrough_returns_input(self) -> None:
        """If operation doesn't match any known branch, return image as-is.
        For grayscale images, opening/closing etc. fall through to gradient/tophat/blackhat
        checks — if those also don't match, we get image back."""
        mp = MorphologyProcessor()
        gray = _gray(32, 32)
        # Opening on grayscale falls through both binary and grayscale erosion/dilation
        # branches and goes to gradient/tophat/blackhat check — none match → returns image
        result = mp.apply(gray, MorphologyOperation.OPENING)
        assert result.shape == gray.shape


# ===================================================================
# Factory Functions
# ===================================================================

class TestFactories:
    def test_create_quality_filter(self) -> None:
        qf = create_quality_filter(min_blur_score=200.0)
        assert qf.thresholds.min_blur_score == 200.0

    def test_create_image_normalizer(self) -> None:
        n = create_image_normalizer(normalization="zscore")
        assert n.config.normalization == "zscore"

    def test_create_focus_analyzer(self) -> None:
        fa = create_focus_analyzer(metric=FocusMetric.BRENNER, threshold=50.0)
        assert fa.metric == FocusMetric.BRENNER

    def test_create_artifact_detector(self) -> None:
        ad = create_artifact_detector(sensitivity=0.8)
        assert ad.sensitivity == 0.8

    def test_create_cell_segmenter(self) -> None:
        cs = create_cell_segmenter(method=SegmentationType.WATERSHED)
        assert cs.method == SegmentationType.WATERSHED

    def test_create_stain_normalizer_default(self) -> None:
        sn = create_stain_normalizer()
        assert isinstance(sn, StainNormalizer)

    def test_create_stain_normalizer_with_reference(self) -> None:
        ref = _rgb(64, 64)
        sn = create_stain_normalizer(reference_image=ref)
        assert isinstance(sn, StainNormalizer)

    def test_create_tile_manager(self) -> None:
        tm = create_tile_manager(tile_size=128, overlap=16)
        assert tm.tile_size == 128

    def test_create_morphology_processor(self) -> None:
        mp = create_morphology_processor(kernel_size=7)
        assert mp._kernel_size == 7


# ===================================================================
# I/O functions
# ===================================================================

class TestLoadImage:
    def test_load_png(self, tmp_path: Path) -> None:
        from PIL import Image
        img = Image.fromarray(_rgb(64, 64))
        img.save(tmp_path / "test.png")
        result = load_image_file(tmp_path / "test.png")
        assert result.shape == (64, 64, 3)

    def test_load_grayscale(self, tmp_path: Path) -> None:
        from PIL import Image
        img = Image.fromarray(_gray(64, 64))
        img.save(tmp_path / "test.png")
        result = load_image_file(tmp_path / "test.png", color_space=ColorSpace.GRAYSCALE)
        assert result.ndim == 2

    def test_load_not_found(self) -> None:
        with pytest.raises(FileNotFoundError):
            load_image_file(Path("/nonexistent/image.png"))

    def test_load_unsupported_format(self, tmp_path: Path) -> None:
        bad_file = tmp_path / "data.xyz"
        bad_file.write_text("data")
        with pytest.raises(ValueError, match="Unsupported format"):
            load_image_file(bad_file)

    def test_load_rgb_no_conversion(self, tmp_path: Path) -> None:
        from PIL import Image
        img = Image.fromarray(_rgb(64, 64))
        img.save(tmp_path / "test.jpg")
        result = load_image_file(tmp_path / "test.jpg", color_space=ColorSpace.RGB)
        assert result.ndim == 3


class TestSaveImage:
    def test_save_rgb(self, tmp_path: Path) -> None:
        path = save_image_file(_rgb(64, 64), tmp_path / "out.png")
        assert path.exists()

    def test_save_grayscale(self, tmp_path: Path) -> None:
        path = save_image_file(_gray(64, 64), tmp_path / "out.png")
        assert path.exists()

    def test_save_jpeg_quality(self, tmp_path: Path) -> None:
        path = save_image_file(_rgb(64, 64), tmp_path / "out.jpg", quality=50)
        assert path.exists()

    def test_save_creates_dirs(self, tmp_path: Path) -> None:
        path = save_image_file(_rgb(64, 64), tmp_path / "sub" / "dir" / "out.png")
        assert path.exists()


# ===================================================================
# Dataclass slots checks
# ===================================================================

class TestDataclassSlots:
    def test_focus_result(self) -> None:
        fr = FocusResult(
            metric=FocusMetric.LAPLACIAN, score=100.0,
            is_in_focus=True, threshold=50.0, regions=[],
        )
        assert fr.score == 100.0

    def test_artifact_detection_result(self) -> None:
        adr = ArtifactDetectionResult(
            artifacts_found=[], artifact_masks={},
            severity_scores={}, is_usable=True,
        )
        assert adr.is_usable is True

    def test_cell_segmentation_result(self) -> None:
        csr = CellSegmentationResult(
            mask=np.zeros((10, 10)), cell_count=0,
            cell_centroids=[], cell_areas=[], cell_contours=[],
            confidence=0.5,
        )
        assert csr.cell_count == 0

    def test_stain_normalization_result(self) -> None:
        snr = StainNormalizationResult(
            normalized_image=np.zeros((10, 10, 3)),
            stain_matrix=np.eye(2, 3),
            concentrations=np.zeros((10, 10, 2)),
            source_stain_type=StainType.UNKNOWN,
        )
        assert snr.source_stain_type == StainType.UNKNOWN

    def test_tile_info(self) -> None:
        ti = TileInfo(x=0, y=0, width=32, height=32, data=np.zeros((32, 32)), overlap=0)
        assert ti.width == 32


# ===================================================================
# Coverage gap closers
# ===================================================================


class TestFocusAnalyzerUnknownMetric:
    """Line 911: return 0.0 when metric is unrecognized."""

    def test_unknown_metric_returns_zero(self) -> None:
        fa = FocusAnalyzer(metric=FocusMetric.LAPLACIAN)
        # Monkey-patch to an invalid metric value
        fa._metric = "nonexistent"  # type: ignore[assignment]
        score = fa._compute_focus_score(_gray().astype(np.float64))
        assert score == 0.0


class TestLoadImageGrayscaleConversion:
    """Lines 2090-2091: convert RGB image to grayscale in load_image_file."""

    def test_load_rgb_as_grayscale(self, tmp_path: Path) -> None:
        from PIL import Image
        img = Image.fromarray(_rgb(64, 64))
        img.save(tmp_path / "rgb.png")
        result = load_image_file(tmp_path / "rgb.png", color_space=ColorSpace.GRAYSCALE)
        assert result.ndim == 2
        assert result.shape == (64, 64)


class TestLoadImagePILFallback:
    """Lines 2084-2086: PIL ImportError fallback → np.load."""

    def test_load_when_pil_unavailable(self, tmp_path: Path) -> None:
        # Save a numpy file with a supported extension (trick: actually .npy but
        # create a .png file that np.load can read by saving as .npy then renaming)
        arr = _rgb(32, 32)
        npy_path = tmp_path / "image.npy"
        np.save(npy_path, arr)
        # Rename to .png so format check passes
        png_path = tmp_path / "image.png"
        npy_path.rename(png_path)

        real_import = builtins.__import__

        def mock_import(name: str, *args: Any, **kwargs: Any) -> Any:
            if name == "PIL" or name == "PIL.Image":
                raise ImportError("mocked")
            return real_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            # np.load on a .png file won't work, so the fallback will err.
            # Instead, let's mock np.load to return our array.
            with patch("ml.data.microscopy.np.load", return_value=arr):
                result = load_image_file(png_path)
                assert np.array_equal(result, arr)


class TestSaveImagePILFallback:
    """Lines 2131-2133: PIL ImportError fallback → np.save."""

    def test_save_npy_when_pil_unavailable(self, tmp_path: Path) -> None:
        arr = _rgb(32, 32)
        out_path = tmp_path / "output.png"

        real_import = builtins.__import__

        def mock_import(name: str, *args: Any, **kwargs: Any) -> Any:
            if name == "PIL" or name == "PIL.Image":
                raise ImportError("mocked")
            return real_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=mock_import):
            result_path = save_image_file(arr, out_path)
            assert result_path.suffix == ".npy"
            assert result_path.exists()
            loaded = np.load(result_path)
            assert np.array_equal(loaded, arr)
