"""Comprehensive tests for ml.data.acquisition – CDC Data Acquisition Client.

Targets 100 % statement coverage of every class, method, branch, and factory
function in the acquisition module.
"""

from __future__ import annotations

import hashlib
import io
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import pytest

from ml.data.acquisition import (
    BandwidthThrottler,
    CDCDataClient,
    ChecksumCalculator,
    CircuitBreaker,
    CircuitBreakerConfig,
    CircuitOpenError,
    CircuitState,
    DataCategory,
    DataIntegrityValidator,
    IncrementalSyncState,
    ManifestEntry,
    ManifestParser,
    ResilientCDCClient,
    RetryConfig,
    RetryPolicy,
    TelemetryEmitter,
    TransferConfig,
    TransferMetrics,
    TransferProgressTracker,
    TransferQueue,
    TransferResult,
    TransferResumeState,
    TransferStatus,
    create_cdc_client,
    create_resilient_client,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_manifest_dict(
    *,
    version: str = "2.0",
    created_at: str | None = "2026-01-15T12:00:00",
    files: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    if files is None:
        files = [
            {
                "path": "images/img001.tiff",
                "checksum": "abc123",
                "size": 1024,
                "category": "microscopy",
                "description": "Wet-mount image",
            },
            {
                "path": "records/case01.csv",
                "checksum": "def456",
                "size": 512,
                "category": "clinical",
                "description": "Case record",
            },
        ]
    d: dict[str, Any] = {"version": version, "files": files}
    if created_at is not None:
        d["created_at"] = created_at
    return d


def _write_manifest(tmp_path: Path, manifest: dict[str, Any] | None = None) -> Path:
    p = tmp_path / "manifest.json"
    p.write_text(json.dumps(manifest or _make_manifest_dict()), encoding="utf-8")
    return p


def _write_file(path: Path, content: bytes = b"hello") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


class FakeBackend:
    """Minimal TransferProtocol implementation for tests."""

    def __init__(self, file_contents: dict[str, bytes] | None = None) -> None:
        self._files = file_contents or {}
        self.connected = False

    def connect(self) -> None:
        self.connected = True

    def disconnect(self) -> None:
        self.connected = False

    def list_directory(self, path: str) -> list[str]:
        return list(self._files.keys())

    def download_file(
        self,
        remote_path: str,
        local_path: Path,
        callback: Any = None,
    ) -> int:
        content = self._files.get(remote_path, b"data")
        local_path.parent.mkdir(parents=True, exist_ok=True)
        local_path.write_bytes(content)
        return len(content)

    def get_file_size(self, remote_path: str) -> int:
        return len(self._files.get(remote_path, b""))


class FailingBackend:
    """Backend that always raises."""

    def connect(self) -> None: ...
    def disconnect(self) -> None: ...
    def list_directory(self, path: str) -> list[str]:
        return []
    def download_file(self, remote_path: str, local_path: Path, callback: Any = None) -> int:
        raise OSError("Connection refused")
    def get_file_size(self, remote_path: str) -> int:
        return 0


# ===================================================================
# DataCategory / TransferStatus enums
# ===================================================================

class TestEnums:
    def test_data_category_members(self) -> None:
        assert DataCategory.MICROSCOPY.name == "MICROSCOPY"
        assert DataCategory.CLINICAL.name == "CLINICAL"
        assert DataCategory.EPIDEMIOLOGICAL.name == "EPIDEMIOLOGICAL"
        assert DataCategory.METADATA.name == "METADATA"
        assert DataCategory.MANIFEST.name == "MANIFEST"
        assert DataCategory.UNKNOWN.name == "UNKNOWN"

    def test_transfer_status_values(self) -> None:
        assert TransferStatus.PENDING.value == "pending"
        assert TransferStatus.IN_PROGRESS.value == "in_progress"
        assert TransferStatus.COMPLETED.value == "completed"
        assert TransferStatus.FAILED.value == "failed"
        assert TransferStatus.VERIFIED.value == "verified"
        assert TransferStatus.QUARANTINED.value == "quarantined"


# ===================================================================
# TransferResult / TransferConfig
# ===================================================================

class TestTransferResult:
    def test_immutable(self) -> None:
        r = TransferResult(
            success=True, file_path=Path("x"), checksum="abc",
            elapsed_seconds=1.0, bytes_transferred=100,
        )
        assert r.success is True
        assert r.error_message is None

    def test_with_error(self) -> None:
        r = TransferResult(
            success=False, file_path=Path("y"), checksum="",
            elapsed_seconds=0.5, bytes_transferred=0, error_message="fail",
        )
        assert r.error_message == "fail"


class TestTransferConfig:
    def test_defaults(self, tmp_path: Path) -> None:
        cfg = TransferConfig(host="h")
        assert cfg.port == 22
        assert cfg.verify_checksums is True

    def test_invalid_port(self) -> None:
        with pytest.raises(ValueError, match="Invalid port"):
            TransferConfig(host="h", port=0)
        with pytest.raises(ValueError, match="Invalid port"):
            TransferConfig(host="h", port=70000)

    def test_invalid_timeout(self) -> None:
        with pytest.raises(ValueError, match="Timeout"):
            TransferConfig(host="h", timeout_seconds=0)

    def test_invalid_chunk_size(self) -> None:
        with pytest.raises(ValueError, match="Chunk size"):
            TransferConfig(host="h", chunk_size=512)


# ===================================================================
# ChecksumCalculator
# ===================================================================

class TestChecksumCalculator:
    def test_algorithm_property(self) -> None:
        c = ChecksumCalculator(algorithm="sha512")
        assert c.algorithm == "sha512"

    def test_compute_file(self, tmp_path: Path) -> None:
        f = tmp_path / "data.bin"
        f.write_bytes(b"hello world")
        c = ChecksumCalculator()
        digest = c.compute_file(f)
        assert digest == hashlib.sha256(b"hello world").hexdigest()

    def test_compute_stream(self) -> None:
        c = ChecksumCalculator(algorithm="md5")
        stream = io.BytesIO(b"test data")
        digest = c.compute_stream(stream)
        assert digest == hashlib.md5(b"test data").hexdigest()

    def test_verify_match(self, tmp_path: Path) -> None:
        f = tmp_path / "v.bin"
        f.write_bytes(b"abc")
        c = ChecksumCalculator()
        expected = hashlib.sha256(b"abc").hexdigest()
        assert c.verify(f, expected) is True

    def test_verify_mismatch(self, tmp_path: Path) -> None:
        f = tmp_path / "v.bin"
        f.write_bytes(b"abc")
        c = ChecksumCalculator()
        assert c.verify(f, "0000") is False

    def test_verify_case_insensitive(self, tmp_path: Path) -> None:
        f = tmp_path / "v.bin"
        f.write_bytes(b"abc")
        c = ChecksumCalculator()
        expected = hashlib.sha256(b"abc").hexdigest().upper()
        assert c.verify(f, expected) is True


# ===================================================================
# ManifestParser
# ===================================================================

class TestManifestParser:
    def test_load_from_file(self, tmp_path: Path) -> None:
        p = _write_manifest(tmp_path)
        mp = ManifestParser.from_file(p)
        assert mp.version == "2.0"
        assert mp.created_at is not None
        assert len(mp.entries) == 2

    def test_load_from_string(self) -> None:
        mp = ManifestParser()
        mp.load_from_string(json.dumps(_make_manifest_dict()))
        assert len(mp.entries) == 2

    def test_entries_are_copies(self, tmp_path: Path) -> None:
        p = _write_manifest(tmp_path)
        mp = ManifestParser.from_file(p)
        e1 = mp.entries
        e2 = mp.entries
        assert e1 is not e2
        assert e1 == e2

    def test_filter_by_category(self, tmp_path: Path) -> None:
        p = _write_manifest(tmp_path)
        mp = ManifestParser.from_file(p)
        micro = mp.filter_by_category(DataCategory.MICROSCOPY)
        assert len(micro) == 1
        assert micro[0].category == DataCategory.MICROSCOPY

    def test_total_size_bytes(self, tmp_path: Path) -> None:
        p = _write_manifest(tmp_path)
        mp = ManifestParser.from_file(p)
        assert mp.total_size_bytes() == 1024 + 512

    def test_to_dict_roundtrip(self, tmp_path: Path) -> None:
        p = _write_manifest(tmp_path)
        mp = ManifestParser.from_file(p)
        d = mp.to_dict()
        assert d["version"] == "2.0"
        assert len(d["files"]) == 2

    def test_unknown_category(self) -> None:
        mp = ManifestParser(strict_mode=False)
        mp.load_from_string(json.dumps({
            "version": "1.0",
            "files": [{"path": "x", "checksum": "y", "size": 10, "category": "weird"}],
        }))
        assert mp.entries[0].category == DataCategory.UNKNOWN

    def test_strict_missing_path(self) -> None:
        mp = ManifestParser(strict_mode=True)
        with pytest.raises(ValueError, match="missing file path"):
            mp.load_from_string(json.dumps({
                "version": "1.0",
                "files": [{"path": "", "checksum": "y", "size": 10}],
            }))

    def test_strict_missing_checksum(self) -> None:
        mp = ManifestParser(strict_mode=True)
        with pytest.raises(ValueError, match="missing checksum"):
            mp.load_from_string(json.dumps({
                "version": "1.0",
                "files": [{"path": "f", "checksum": "", "size": 10}],
            }))

    def test_strict_negative_size(self) -> None:
        mp = ManifestParser(strict_mode=True)
        with pytest.raises(ValueError, match="invalid size"):
            mp.load_from_string(json.dumps({
                "version": "1.0",
                "files": [{"path": "f", "checksum": "c", "size": -1}],
            }))

    def test_no_created_at(self) -> None:
        mp = ManifestParser(strict_mode=False)
        mp.load_from_string(json.dumps({"version": "1.0", "files": []}))
        assert mp.created_at is None
        d = mp.to_dict()
        assert d["created_at"] is None

    def test_missing_version_strict(self) -> None:
        mp = ManifestParser(strict_mode=True)
        # version defaults to "1.0" if key is present but set to ""
        mp.load_from_string(json.dumps({"version": "1.0", "files": [{"path": "f", "checksum": "c", "size": 0}]}))
        assert mp.version == "1.0"

    def test_all_categories(self) -> None:
        files = [
            {"path": f"f{i}", "checksum": f"c{i}", "size": 10, "category": cat}
            for i, cat in enumerate([
                "microscopy", "clinical", "epidemiological", "metadata", "manifest",
            ])
        ]
        mp = ManifestParser(strict_mode=False)
        mp.load_from_string(json.dumps({"version": "1.0", "files": files}))
        cats = {e.category for e in mp.entries}
        assert DataCategory.MICROSCOPY in cats
        assert DataCategory.CLINICAL in cats
        assert DataCategory.EPIDEMIOLOGICAL in cats
        assert DataCategory.METADATA in cats
        assert DataCategory.MANIFEST in cats


# ===================================================================
# CDCDataClient
# ===================================================================

class TestCDCDataClient:
    def _make_client(self, tmp_path: Path) -> CDCDataClient:
        cfg = TransferConfig(host="sftp.cdc.gov", username="u", staging_dir=tmp_path / "staging")
        return CDCDataClient(cfg)

    def test_session_id_format(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        assert c.session_id.startswith("CDC_ACQ_")

    def test_transfer_log_empty(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        assert c.transfer_log == []

    def test_manifest_none_initially(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        assert c.manifest is None

    def test_acquire_no_backend_raises(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        p = _write_manifest(tmp_path)
        with pytest.raises(RuntimeError, match="No transfer backend"):
            c.acquire_from_manifest(p)

    def test_acquire_with_fake_backend(self, tmp_path: Path) -> None:
        """Full acquisition flow with a fake SFTP backend."""
        content = b"pixel data"
        checksum = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "img.tiff", "checksum": checksum, "size": len(content), "category": "microscopy", "description": "d"},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"img.tiff": content}))
        results = c.acquire_from_manifest(p)
        assert len(results) == 1
        assert results[0].success is True
        assert c.transfer_log[0].success is True

    def test_acquire_checksum_mismatch(self, tmp_path: Path) -> None:
        manifest = _make_manifest_dict(files=[
            {"path": "img.tiff", "checksum": "wrong", "size": 5, "category": "microscopy", "description": "d"},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"img.tiff": b"data!"}))
        results = c.acquire_from_manifest(p)
        assert results[0].success is False
        assert "Checksum" in (results[0].error_message or "")

    def test_acquire_no_checksum_verify(self, tmp_path: Path) -> None:
        cfg = TransferConfig(host="h", username="u", staging_dir=tmp_path / "staging", verify_checksums=False)
        c = CDCDataClient(cfg)
        manifest = _make_manifest_dict(files=[
            {"path": "f.csv", "checksum": "placeholder", "size": 4, "category": "clinical", "description": "d"},
        ])
        p = _write_manifest(tmp_path, manifest)
        c.set_backend(FakeBackend({"f.csv": b"data"}))
        results = c.acquire_from_manifest(p)
        assert results[0].success is True

    def test_acquire_backend_raises(self, tmp_path: Path) -> None:
        manifest = _make_manifest_dict(files=[
            {"path": "f.csv", "checksum": "abc", "size": 4, "category": "clinical", "description": "d"},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FailingBackend())
        results = c.acquire_from_manifest(p)
        assert results[0].success is False
        assert "Connection refused" in (results[0].error_message or "")

    def test_acquire_filter_categories(self, tmp_path: Path) -> None:
        content = b"x"
        cs = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "a.tiff", "checksum": cs, "size": 1, "category": "microscopy", "description": ""},
            {"path": "b.csv", "checksum": cs, "size": 1, "category": "clinical", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"a.tiff": content, "b.csv": content}))
        results = c.acquire_from_manifest(p, categories=[DataCategory.MICROSCOPY])
        assert len(results) == 1

    def test_acquire_microscopy_convenience(self, tmp_path: Path) -> None:
        content = b"img"
        cs = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "a.tiff", "checksum": cs, "size": 3, "category": "microscopy", "description": ""},
            {"path": "b.csv", "checksum": cs, "size": 3, "category": "clinical", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"a.tiff": content, "b.csv": content}))
        results = c.acquire_microscopy_images(p)
        assert len(results) == 1

    def test_acquire_clinical_convenience(self, tmp_path: Path) -> None:
        content = b"rec"
        cs = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "b.csv", "checksum": cs, "size": 3, "category": "clinical", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"b.csv": content}))
        results = c.acquire_clinical_records(p)
        assert len(results) == 1

    def test_acquire_epidemiological_convenience(self, tmp_path: Path) -> None:
        content = b"epi"
        cs = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "e.csv", "checksum": cs, "size": 3, "category": "epidemiological", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"e.csv": content}))
        results = c.acquire_epidemiological_data(p)
        assert len(results) == 1

    def test_transfer_single_file_no_backend(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        entry = ManifestEntry("f", "c", 10, DataCategory.CLINICAL, "d")
        result = c._transfer_single_file(entry)
        assert result.success is False
        assert "No backend" in (result.error_message or "")

    def test_generate_inventory(self, tmp_path: Path) -> None:
        content = b"px"
        cs = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "f.tiff", "checksum": cs, "size": 2, "category": "microscopy", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"f.tiff": content}))
        c.acquire_from_manifest(p)
        inv = c.generate_inventory()
        assert inv["summary"]["total_files"] == 1
        assert inv["summary"]["successful"] == 1

    def test_save_inventory(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        out = tmp_path / "inv.json"
        c.save_inventory(out)
        assert out.exists()
        loaded = json.loads(out.read_text())
        assert "session_id" in loaded

    def test_validate_staging_directory(self, tmp_path: Path) -> None:
        content = b"filedata"
        cs = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "f.tiff", "checksum": cs, "size": 8, "category": "microscopy", "description": ""},
        ])
        mp_path = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"f.tiff": content}))
        c.acquire_from_manifest(mp_path)
        report = c.validate_staging_directory()
        assert report["summary"]["invalid"] == 0

    def test_validate_staging_no_manifest(self, tmp_path: Path) -> None:
        staging = tmp_path / "staging"
        staging.mkdir()
        (staging / "f.bin").write_bytes(b"test")
        cfg = TransferConfig(host="h", username="u", staging_dir=staging)
        c = CDCDataClient(cfg)
        report = c.validate_staging_directory()
        assert report["summary"]["total"] == 1
        assert report["summary"]["valid"] == 1  # no expected → valid

    def test_validate_staging_missing_dir(self, tmp_path: Path) -> None:
        cfg = TransferConfig(host="h", username="u", staging_dir=tmp_path / "nodir")
        # staging_dir created in __init__, so delete it
        staging = tmp_path / "nodir"
        if staging.exists():
            staging.rmdir()
        c = CDCDataClient(cfg)
        # Remove the dir again after __init__ creates it
        staging.rmdir()
        report = c.validate_staging_directory()
        assert "error" in report


# ===================================================================
# CircuitBreaker
# ===================================================================

class TestCircuitBreaker:
    def test_initial_state_closed(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(), name="test")
        assert cb.state == CircuitState.CLOSED
        assert cb.name == "test"

    def test_successful_operations_stay_closed(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(failure_threshold=3))
        for _ in range(10):
            with cb.protect():
                pass
        assert cb.state == CircuitState.CLOSED

    def test_failures_trip_open(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(failure_threshold=2))
        for _ in range(2):
            with pytest.raises(ValueError):
                with cb.protect():
                    raise ValueError("boom")
        assert cb.state == CircuitState.OPEN

    def test_open_rejects_requests(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(failure_threshold=1))
        with pytest.raises(ValueError):
            with cb.protect():
                raise ValueError("x")
        assert cb.state == CircuitState.OPEN
        with pytest.raises(CircuitOpenError):
            with cb.protect():
                pass

    def test_half_open_after_timeout(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(
            failure_threshold=1, timeout_seconds=0.01, success_threshold=1,
        ))
        with pytest.raises(ValueError):
            with cb.protect():
                raise ValueError("x")
        assert cb.state == CircuitState.OPEN
        time.sleep(0.02)
        with cb.protect():
            pass
        assert cb.state == CircuitState.CLOSED  # type: ignore[comparison-overlap]

    def test_half_open_failure_reopens(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(
            failure_threshold=1, timeout_seconds=0.01,
        ))
        with pytest.raises(ValueError):
            with cb.protect():
                raise ValueError
        time.sleep(0.02)
        with pytest.raises(ValueError):
            with cb.protect():
                raise ValueError
        assert cb.state == CircuitState.OPEN

    def test_excluded_exceptions(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(
            failure_threshold=1, excluded_exceptions=(TypeError,),
        ))
        with pytest.raises(TypeError):
            with cb.protect():
                raise TypeError
        assert cb.state == CircuitState.CLOSED

    def test_telemetry_callback(self) -> None:
        events: list[dict[str, Any]] = []
        cb = CircuitBreaker(CircuitBreakerConfig(failure_threshold=1))
        cb.set_telemetry_callback(events.append)
        with pytest.raises(ValueError):
            with cb.protect():
                raise ValueError
        assert any("circuit_opened" in str(e) for e in events)

    def test_success_resets_failure_count(self) -> None:
        cb = CircuitBreaker(CircuitBreakerConfig(failure_threshold=3))
        # 2 failures
        for _ in range(2):
            with pytest.raises(ValueError):
                with cb.protect():
                    raise ValueError
        # 1 success resets
        with cb.protect():
            pass
        # 2 more failures should not trip (count reset)
        for _ in range(2):
            with pytest.raises(ValueError):
                with cb.protect():
                    raise ValueError
        assert cb.state == CircuitState.CLOSED

    def test_open_no_last_failure_time(self) -> None:
        """Edge: circuit open but _last_failure_time is None."""
        cb = CircuitBreaker(CircuitBreakerConfig(failure_threshold=1))
        # Force state
        cb._state = CircuitState.OPEN
        cb._last_failure_time = None
        with pytest.raises(CircuitOpenError):
            with cb.protect():
                pass


# ===================================================================
# RetryPolicy
# ===================================================================

class TestRetryPolicy:
    def test_succeeds_first_try(self) -> None:
        rp = RetryPolicy(RetryConfig(max_attempts=3))
        result = rp.execute(lambda: 42)
        assert result == 42

    def test_retries_then_succeeds(self) -> None:
        attempts = {"n": 0}
        def flaky() -> str:
            attempts["n"] += 1
            if attempts["n"] < 3:
                raise OSError("transient")
            return "ok"
        rp = RetryPolicy(RetryConfig(max_attempts=3, base_delay_seconds=0.001, max_delay_seconds=0.01))
        assert rp.execute(flaky) == "ok"

    def test_retries_exhausted(self) -> None:
        rp = RetryPolicy(RetryConfig(max_attempts=2, base_delay_seconds=0.001, max_delay_seconds=0.01))
        with pytest.raises(OSError, match="fail"):
            rp.execute(lambda: (_ for _ in ()).throw(OSError("fail")))

    def test_non_retryable_raises_immediately(self) -> None:
        rp = RetryPolicy(RetryConfig(max_attempts=5, retryable_exceptions=(OSError,)))
        with pytest.raises(ValueError):
            rp.execute(lambda: (_ for _ in ()).throw(ValueError("bad")))

    def test_telemetry_callback(self) -> None:
        events: list[dict[str, Any]] = []
        rp = RetryPolicy(RetryConfig(max_attempts=2, base_delay_seconds=0.001, max_delay_seconds=0.01))
        rp.set_telemetry_callback(events.append)
        with pytest.raises(OSError):
            rp.execute(lambda: (_ for _ in ()).throw(OSError("x")))
        assert any("retry" in str(e) for e in events)

    def test_telemetry_on_retry_success(self) -> None:
        events: list[dict[str, Any]] = []
        attempts = {"n": 0}
        def fn() -> str:
            attempts["n"] += 1
            if attempts["n"] < 2:
                raise OSError("x")
            return "ok"
        rp = RetryPolicy(RetryConfig(max_attempts=3, base_delay_seconds=0.001))
        rp.set_telemetry_callback(events.append)
        rp.execute(fn)
        assert any("retry_succeeded" in str(e) for e in events)

    def test_compute_delay_exponential(self) -> None:
        rp = RetryPolicy(RetryConfig(
            base_delay_seconds=1.0, exponential_base=2.0,
            max_delay_seconds=100.0, jitter_factor=0.0,
        ))
        d0 = rp._compute_delay(0)
        d1 = rp._compute_delay(1)
        d2 = rp._compute_delay(2)
        assert d0 == pytest.approx(1.0)
        assert d1 == pytest.approx(2.0)
        assert d2 == pytest.approx(4.0)

    def test_compute_delay_capped(self) -> None:
        rp = RetryPolicy(RetryConfig(
            base_delay_seconds=1.0, exponential_base=2.0,
            max_delay_seconds=3.0, jitter_factor=0.0,
        ))
        d10 = rp._compute_delay(10)
        assert d10 == pytest.approx(3.0)


# ===================================================================
# TelemetryEmitter
# ===================================================================

class TestTelemetryEmitter:
    def test_session_id_auto(self) -> None:
        te = TelemetryEmitter()
        assert te.session_id  # UUID

    def test_session_id_explicit(self) -> None:
        te = TelemetryEmitter(session_id="S1")
        assert te.session_id == "S1"

    def test_emit_and_buffer(self) -> None:
        te = TelemetryEmitter(buffer_size=10)
        te.emit("test_event", key="val")
        assert te.buffer_count == 1

    def test_flush_returns_events(self) -> None:
        te = TelemetryEmitter(buffer_size=10)
        te.emit("ev1")
        te.emit("ev2")
        events = te.flush()
        assert len(events) == 2
        assert te.buffer_count == 0

    def test_callback_receives_events(self) -> None:
        received: list[dict[str, Any]] = []
        te = TelemetryEmitter()
        te.add_callback(received.append)
        te.emit("ping")
        assert len(received) == 1
        assert received[0]["event_type"] == "ping"

    def test_remove_callback(self) -> None:
        def cb(e: dict[str, Any]) -> None:
            pass

        te = TelemetryEmitter()
        te.add_callback(cb)
        assert te.remove_callback(cb) is True
        assert te.remove_callback(cb) is False

    def test_callback_failure_does_not_crash(self) -> None:
        te = TelemetryEmitter()
        te.add_callback(lambda e: 1 / 0)  # type: ignore[arg-type]
        te.emit("ev")  # Should not raise

    def test_auto_flush_on_buffer_full(self) -> None:
        delivered: list[dict[str, Any]] = []
        te = TelemetryEmitter(buffer_size=2)
        te.add_callback(delivered.append)
        te.emit("e1")
        te.emit("e2")  # triggers flush
        # After flush + new event delivery, buffer refilled then cleared
        assert len(delivered) >= 2

    def test_get_summary(self) -> None:
        te = TelemetryEmitter(session_id="S")
        te.emit("a")
        te.emit("a")
        te.emit("b")
        s = te.get_summary()
        assert s["session_id"] == "S"
        assert s["buffer_count"] == 3
        assert s["event_types"]["a"] == 2
        assert s["event_types"]["b"] == 1


# ===================================================================
# TransferMetrics
# ===================================================================

class TestTransferMetrics:
    def test_defaults(self) -> None:
        m = TransferMetrics()
        assert m.total_files == 0
        assert m.average_throughput_mbps == 0.0

    def test_update_throughput(self) -> None:
        m = TransferMetrics(total_bytes=1_000_000, total_elapsed_seconds=1.0)
        m.update_throughput()
        assert m.average_throughput_mbps == pytest.approx(8.0)

    def test_update_throughput_zero_time(self) -> None:
        m = TransferMetrics(total_bytes=100, total_elapsed_seconds=0.0)
        m.update_throughput()
        assert m.average_throughput_mbps == 0.0

    def test_to_dict(self) -> None:
        m = TransferMetrics(total_files=2, successful_files=1, failed_files=1)
        d = m.to_dict()
        assert d["success_rate"] == 0.5

    def test_to_dict_zero_files(self) -> None:
        m = TransferMetrics()
        d = m.to_dict()
        assert d["success_rate"] == 0.0


# ===================================================================
# ResilientCDCClient
# ===================================================================

class TestResilientCDCClient:
    def _make_client(self, tmp_path: Path) -> ResilientCDCClient:
        cfg = TransferConfig(host="h", username="u", staging_dir=tmp_path / "staging")
        return ResilientCDCClient(cfg)

    def test_properties(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        assert isinstance(c.metrics, TransferMetrics)
        assert isinstance(c.telemetry, TelemetryEmitter)
        assert isinstance(c.circuit_breaker, CircuitBreaker)

    def test_successful_transfer(self, tmp_path: Path) -> None:
        content = b"img"
        cs = hashlib.sha256(content).hexdigest()
        manifest = _make_manifest_dict(files=[
            {"path": "f.tiff", "checksum": cs, "size": 3, "category": "microscopy", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"f.tiff": content}))
        results = c.acquire_from_manifest(p)
        assert results[0].success is True
        assert c.metrics.successful_files == 1

    def test_failed_transfer_metrics(self, tmp_path: Path) -> None:
        manifest = _make_manifest_dict(files=[
            {"path": "f.csv", "checksum": "wrong", "size": 4, "category": "clinical", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        c = self._make_client(tmp_path)
        c.set_backend(FakeBackend({"f.csv": b"data"}))
        c.acquire_from_manifest(p)
        assert c.metrics.failed_files == 1
        assert c.metrics.checksum_failures == 1

    def test_circuit_open_returns_failure(self, tmp_path: Path) -> None:
        cfg = TransferConfig(host="h", username="u", staging_dir=tmp_path / "staging")
        c = ResilientCDCClient(
            cfg,
            circuit_config=CircuitBreakerConfig(failure_threshold=1),
            retry_config=RetryConfig(max_attempts=1, base_delay_seconds=0.001, retryable_exceptions=(OSError,)),
        )
        c.set_backend(FailingBackend())
        manifest = _make_manifest_dict(files=[
            {"path": "a.csv", "checksum": "x", "size": 1, "category": "clinical", "description": ""},
            {"path": "b.csv", "checksum": "y", "size": 1, "category": "clinical", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        results = c.acquire_from_manifest(p)
        # First fails from backend, circuit opens, second blocked
        assert not all(r.success for r in results)
        assert c.metrics.failed_files >= 1

    def test_generate_inventory_enhanced(self, tmp_path: Path) -> None:
        c = self._make_client(tmp_path)
        inv = c.generate_inventory()
        assert "metrics" in inv
        assert "telemetry_summary" in inv
        assert "circuit_breaker_state" in inv


# ===================================================================
# BandwidthThrottler
# ===================================================================

class TestBandwidthThrottler:
    def test_acquire_within_budget(self) -> None:
        bt = BandwidthThrottler(max_bytes_per_second=10_000)
        assert bt.acquire(100) is True

    def test_acquire_timeout(self) -> None:
        bt = BandwidthThrottler(max_bytes_per_second=1)
        # Drain tokens completely
        bt._tokens = 0.0
        bt._last_update = time.monotonic()
        # Need 1 billion tokens but only get 1/sec → instant timeout
        result = bt.acquire(1_000_000_000, timeout=0.001)
        assert result is False

    def test_get_available_bandwidth(self) -> None:
        bt = BandwidthThrottler(max_bytes_per_second=10_000)
        avail = bt.get_available_bandwidth()
        assert avail > 0


# ===================================================================
# TransferQueue
# ===================================================================

class TestTransferQueue:
    def _entry(self, name: str) -> ManifestEntry:
        return ManifestEntry(name, "cs", 100, DataCategory.MICROSCOPY, "d")

    def test_enqueue_dequeue(self) -> None:
        q = TransferQueue()
        q.enqueue(self._entry("a"), priority=1)
        q.enqueue(self._entry("b"), priority=0)
        assert q.size() == 2
        first = q.dequeue()
        assert first is not None and first.file_path == "b"

    def test_peek(self) -> None:
        q = TransferQueue()
        assert q.peek() is None
        q.enqueue(self._entry("a"))
        assert q.peek() is not None
        assert q.size() == 1  # peek doesn't remove

    def test_dequeue_empty(self) -> None:
        q = TransferQueue()
        assert q.dequeue() is None

    def test_no_duplicates(self) -> None:
        q = TransferQueue()
        q.enqueue(self._entry("a"))
        q.dequeue()
        q.enqueue(self._entry("a"))  # already processed
        assert q.size() == 0

    def test_clear(self) -> None:
        q = TransferQueue()
        q.enqueue(self._entry("a"))
        q.clear()
        assert q.size() == 0

    def test_mark_processed(self) -> None:
        q = TransferQueue()
        q.mark_processed("x")
        assert q.is_processed("x") is True
        assert q.is_processed("y") is False


# ===================================================================
# IncrementalSyncState
# ===================================================================

class TestIncrementalSyncState:
    def test_save_and_load(self, tmp_path: Path) -> None:
        state = IncrementalSyncState()
        state.record_sync(10, 1024, marker="m1")
        f = tmp_path / "state.json"
        state.save(f)
        assert f.exists()

        state2 = IncrementalSyncState()
        state2.load(f)
        assert state2.files_synced == 10
        assert state2.bytes_synced == 1024
        assert state2.last_sync_marker == "m1"

    def test_load_nonexistent(self, tmp_path: Path) -> None:
        state = IncrementalSyncState()
        state.load(tmp_path / "missing.json")
        assert state.files_synced == 0

    def test_load_corrupt(self, tmp_path: Path) -> None:
        f = tmp_path / "bad.json"
        f.write_text("not json!!!")
        state = IncrementalSyncState()
        state.load(f)  # should not raise
        assert state.files_synced == 0

    def test_record_sync_persists(self, tmp_path: Path) -> None:
        f = tmp_path / "s.json"
        state = IncrementalSyncState()
        state.save(f)  # set _state_file
        state.record_sync(5, 500)
        # Should auto-save
        loaded = json.loads(f.read_text())
        assert loaded["files_synced"] == 5

    def test_no_state_file(self) -> None:
        state = IncrementalSyncState()
        state.record_sync(1, 100)
        assert state.files_synced == 1
        assert state.last_sync_time is not None

    def test_history_capped(self, tmp_path: Path) -> None:
        state = IncrementalSyncState()
        for i in range(150):
            state.sync_history.append({"i": i})
        f = tmp_path / "s.json"
        state.save(f)
        loaded = json.loads(f.read_text())
        assert len(loaded["sync_history"]) == 100  # last 100


# ===================================================================
# TransferResumeState
# ===================================================================

class TestTransferResumeState:
    def _make(self) -> TransferResumeState:
        return TransferResumeState(
            transfer_id="T1",
            file_path="/data/f.bin",
            total_bytes=1000,
            transferred_bytes=500,
            chunk_size=256,
            checksum_partial="abc",
            started_at=datetime(2026, 1, 1),
        )

    def test_to_dict_from_dict_roundtrip(self) -> None:
        rs = self._make()
        d = rs.to_dict()
        rs2 = TransferResumeState.from_dict(d)
        assert rs2.transfer_id == "T1"
        assert rs2.transferred_bytes == 500

    def test_progress_percent(self) -> None:
        rs = self._make()
        assert rs.progress_percent == pytest.approx(50.0)

    def test_progress_zero_total(self) -> None:
        rs = TransferResumeState(
            transfer_id="T2", file_path="f", total_bytes=0,
            transferred_bytes=0, chunk_size=256, checksum_partial="",
            started_at=datetime.now(),
        )
        assert rs.progress_percent == 100.0

    def test_remaining_bytes(self) -> None:
        rs = self._make()
        assert rs.remaining_bytes == 500

    def test_from_dict_with_last_chunk(self) -> None:
        d = self._make().to_dict()
        d["last_chunk_at"] = "2026-01-01T00:05:00"
        rs = TransferResumeState.from_dict(d)
        assert rs.last_chunk_at is not None

    def test_from_dict_defaults_status(self) -> None:
        d = self._make().to_dict()
        del d["status"]
        rs = TransferResumeState.from_dict(d)
        assert rs.status == "in_progress"


# ===================================================================
# DataIntegrityValidator
# ===================================================================

class TestDataIntegrityValidator:
    def test_update_and_finalize(self) -> None:
        v = DataIntegrityValidator(algorithms=("sha256", "md5"))
        v.update(b"hello")
        v.update(b" world")
        digests = v.finalize()
        assert digests["sha256"] == hashlib.sha256(b"hello world").hexdigest()
        assert digests["md5"] == hashlib.md5(b"hello world").hexdigest()

    def test_verify_pass(self) -> None:
        v = DataIntegrityValidator()
        expected = {"sha256": hashlib.sha256(b"x").hexdigest()}
        computed = {"sha256": hashlib.sha256(b"x").hexdigest()}
        ok, failures = v.verify(expected, computed)
        assert ok is True
        assert failures == []

    def test_verify_fail(self) -> None:
        v = DataIntegrityValidator()
        ok, failures = v.verify({"sha256": "aaa"}, {"sha256": "bbb"})
        assert ok is False
        assert len(failures) == 1

    def test_verify_missing_algorithm(self) -> None:
        v = DataIntegrityValidator()
        ok, failures = v.verify({"sha256": "aaa"}, {})
        assert ok is True  # missing algorithm not checked


# ===================================================================
# TransferProgressTracker
# ===================================================================

class TestTransferProgressTracker:
    def test_start_and_progress(self) -> None:
        tp = TransferProgressTracker(total_files=2, total_bytes=1000)
        tp.start()
        tp.update_file("f1.bin", 500, 250)
        progress = tp.get_progress()
        assert progress["total_files"] == 2
        assert progress["transferred_bytes"] == 250

    def test_complete_file(self) -> None:
        tp = TransferProgressTracker(total_files=1, total_bytes=100)
        tp.start()
        tp.update_file("f1", 100, 100)
        tp.complete_file(100)
        assert tp.completed_files == 1
        assert tp.current_file == ""

    def test_callback_on_update(self) -> None:
        events: list[dict[str, Any]] = []
        tp = TransferProgressTracker(total_files=1, total_bytes=100)
        tp.register_callback(events.append)
        tp.start()
        tp.update_file("f1", 100, 50)
        assert len(events) == 1

    def test_callback_on_complete(self) -> None:
        events: list[dict[str, Any]] = []
        tp = TransferProgressTracker(total_files=1, total_bytes=100)
        tp.register_callback(events.append)
        tp.complete_file(100)
        assert len(events) == 1

    def test_callback_exception_suppressed(self) -> None:
        tp = TransferProgressTracker()
        tp.register_callback(lambda e: 1 / 0)  # type: ignore[arg-type]
        tp.update_file("f", 10, 5)  # should not raise

    def test_get_progress_no_start(self) -> None:
        tp = TransferProgressTracker(total_bytes=0)
        p = tp.get_progress()
        assert p["elapsed_seconds"] == 0.0
        assert p["percent_complete"] == 0.0

    def test_throughput_and_eta(self) -> None:
        tp = TransferProgressTracker(total_files=1, total_bytes=1000)
        tp.start()
        time.sleep(0.01)
        tp.update_file("f", 1000, 500)
        p = tp.get_progress()
        assert p["throughput_bytes_per_second"] > 0
        assert p["estimated_remaining_seconds"] > 0


# ===================================================================
# Factory functions
# ===================================================================

class TestFactoryFunctions:
    def test_create_cdc_client(self, tmp_path: Path) -> None:
        staging = tmp_path / "staging"
        c = create_cdc_client(
            "sftp.cdc.gov", "user", staging,
            sftp_port=22, max_retries=2, timeout_seconds=60,
            verify_checksums=True
        )
        assert isinstance(c, CDCDataClient)
        assert c.session_id.startswith("CDC_ACQ_")

    def test_create_cdc_client_with_key(self, tmp_path: Path) -> None:
        key = tmp_path / "key.pem"
        key.write_text("fake-key")
        c = create_cdc_client("h", "u", tmp_path / "s", private_key_path=key)
        assert isinstance(c, CDCDataClient)

    def test_create_resilient_client(self, tmp_path: Path) -> None:
        staging = tmp_path / "staging"
        c = create_resilient_client(
            "sftp.cdc.gov", "user", staging,
            circuit_threshold=3, circuit_timeout=30.0,
            max_retries=4, base_delay=0.5, max_delay=30.0,
        )
        assert isinstance(c, ResilientCDCClient)

    def test_create_resilient_client_with_key(self, tmp_path: Path) -> None:
        key = tmp_path / "key.pem"
        key.write_text("fake-key")
        c = create_resilient_client("h", "u", tmp_path / "s", private_key_path=key)
        assert isinstance(c, ResilientCDCClient)


# ===================================================================
# Named tuples
# ===================================================================

class TestNamedTuples:
    def test_manifest_entry(self) -> None:
        e = ManifestEntry("p", "cs", 100, DataCategory.CLINICAL, "desc")
        assert e.file_path == "p"
        assert e.category == DataCategory.CLINICAL

    def test_transfer_result_fields(self) -> None:
        r = TransferResult(True, Path("a"), "cs", 1.0, 100)
        assert r.success is True
        assert r.error_message is None


# ===================================================================
# Additional edge-case tests to reach 100 %
# ===================================================================

class TestMissingCoverageEdges:
    """Tests targeting the specific missed lines."""

    def test_manifest_empty_version_strict(self) -> None:
        """Line 531: missing manifest version in strict mode."""
        mp = ManifestParser(strict_mode=True)
        with pytest.raises(ValueError, match="Missing manifest version"):
            mp.load_from_string(json.dumps({
                "version": "",
                "files": [{"path": "f", "checksum": "c", "size": 0}],
            }))

    def test_circuit_breaker_open_timeout_not_elapsed(self) -> None:
        """Line 1121: circuit OPEN, timeout not yet elapsed → False."""
        cb = CircuitBreaker(CircuitBreakerConfig(
            failure_threshold=1, timeout_seconds=999,
        ))
        # Trip to OPEN via a real failure
        with pytest.raises(ValueError):
            with cb.protect():
                raise ValueError
        assert cb.state == CircuitState.OPEN
        assert cb._last_failure_time is not None
        # Timeout of 999s hasn't elapsed → should reject
        with pytest.raises(CircuitOpenError):
            with cb.protect():
                pass

    def test_circuit_breaker_half_open_allows_request(self) -> None:
        """Line 1123: HALF_OPEN state allows requests through."""
        cb = CircuitBreaker(CircuitBreakerConfig(
            failure_threshold=1, timeout_seconds=999, success_threshold=3,
        ))
        # Force to HALF_OPEN
        cb._state = CircuitState.HALF_OPEN
        # First request in HALF_OPEN should be allowed
        with cb.protect():
            pass
        # Still HALF_OPEN (needs 3 successes to close, only 1 so far)
        assert cb.state == CircuitState.HALF_OPEN
        # Second request should also be allowed (tests line 1123)
        with cb.protect():
            pass

    def test_telemetry_deliver_event(self) -> None:
        """Line 1509: _deliver_event method."""
        received: list[dict[str, Any]] = []
        te = TelemetryEmitter()
        te.add_callback(received.append)
        event = {"event_type": "test", "timestamp": "now"}
        te._deliver_event(event)  # type: ignore[arg-type]
        assert len(received) == 1

    def test_resilient_circuit_open_during_transfer(self, tmp_path: Path) -> None:
        """Lines 1730-1731: CircuitOpenError caught in resilient client."""
        cfg = TransferConfig(host="h", username="u", staging_dir=tmp_path / "staging")
        c = ResilientCDCClient(
            cfg,
            circuit_config=CircuitBreakerConfig(failure_threshold=1, timeout_seconds=999),
            retry_config=RetryConfig(max_attempts=1, base_delay_seconds=0.001),
        )
        # Force circuit open
        c._circuit_breaker._state = CircuitState.OPEN
        c._circuit_breaker._last_failure_time = time.time()
        c.set_backend(FakeBackend())
        manifest = _make_manifest_dict(files=[
            {"path": "a.csv", "checksum": "x", "size": 1, "category": "clinical", "description": ""},
        ])
        p = _write_manifest(tmp_path, manifest)
        results = c.acquire_from_manifest(p)
        assert len(results) == 1
        assert results[0].success is False
        assert "Circuit breaker" in (results[0].error_message or "")

    def test_retry_exhausted_no_exception_edge(self) -> None:
        """Lines 1372-1373: defensive 'retry exhausted with no exception'."""
        rp = RetryPolicy(RetryConfig(max_attempts=1))
        # Monkey-patch config to have 0 max_attempts so loop doesn't execute
        rp._config = RetryConfig(max_attempts=0)
        with pytest.raises(RuntimeError, match="Retry exhausted with no exception"):
            rp.execute(lambda: 42)
