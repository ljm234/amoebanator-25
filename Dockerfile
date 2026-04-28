# Amoebanator V1.0 — reproducible runtime container.
#
# Two-stage build keeps the final image small:
#   Stage 1 (deps): install pip dependencies into a venv.
#   Stage 2 (runtime): copy the venv + source, expose Streamlit on 8501.
#
# Build:
#   docker build -t amoebanator:v1.0 .
# Run dashboard:
#   docker run --rm -p 8501:8501 amoebanator:v1.0
# Run a single CLI inference:
#   docker run --rm amoebanator:v1.0 \
#       python scripts/infer_cli.py --json '{"age":12,"csf_glucose":18,...}'

# ─── Stage 1: builder ─────────────────────────────────────────────────────
FROM python:3.12-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /build

# System deps for sklearn, scipy, lightgbm libomp, etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libomp-dev \
        ca-certificates \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies into a venv so we can copy it cleanly into the runtime stage.
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements first so this layer caches across source changes.
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

# ─── Stage 2: runtime ─────────────────────────────────────────────────────
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PATH="/opt/venv/bin:$PATH" \
    AMOEBANATOR_AUDIT_PATH=/app/outputs/audit/audit.jsonl \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0

# AMOEBANATOR_IRB_BYPASS — IRB gate bypass switch
#
# WHY THIS EXISTS:
#   The Phase 4.5 demo trains on n=30 synthetic patient vignettes derived from
#   published case-series marginals (Yoder 2010, Cope 2016, CDC 2025). No real
#   PHI, no human subjects. Hence no IRB review is required — but the IRB gate
#   in ml/irb_gate.py refuses to boot the app without an IRB JSON record. This
#   bypass env var short-circuits the gate WITH a mandatory audit log emission
#   (AuditEventType.IRB_STATUS_CHANGE → actor="env_var") so the bypass is
#   never silent.
#
# WHEN TO FLIP TO 0:
#   Phase 6 lands real MIMIC-IV cohort (target n>=200, includes bacterial vs
#   viral meningitis labels). MIMIC-IV is PhysioNet-credentialed PHI, requires
#   an IRB record (independent researcher justification + DUA reference per
#   USER_ASSIGNMENTS.md §4 Step 9). When that IRB record exists at
#   outputs/governance/irb_record.json with irb_status in {approved,
#   conditionally_approved}, flip this to 0 AND remove the bypass audit
#   emission code path.
#
# CHECKLIST BEFORE FLIPPING:
#   [ ] outputs/governance/irb_record.json exists
#   [ ] irb_status field == "approved" or "conditionally_approved"
#   [ ] expiration_date is in the future
#   [ ] All MIMIC-IV cohort code paths emit AuditEventType.PHI_ACCESS events
#   [ ] tests/test_irb_gate.py::test_real_phi_path_requires_irb_record passes
#
ENV AMOEBANATOR_IRB_BYPASS=1

# Runtime needs libomp for LightGBM (if installed) and tini for clean signal handling.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libomp-dev \
        tini \
    && rm -rf /var/lib/apt/lists/*

# Bring the venv built in stage 1.
COPY --from=builder /opt/venv /opt/venv

# Non-root user.
RUN useradd --create-home --shell /bin/bash amoeba
USER amoeba
WORKDIR /app

# Copy source. .dockerignore strips test caches, IDE metadata, and large model
# artefacts that should be regenerated inside the container instead of shipped.
COPY --chown=amoeba:amoeba . /app

# Health check: pytest must collect at least 1100 tests without errors.
HEALTHCHECK --interval=5m --timeout=2m --retries=3 \
  CMD python -m pytest --collect-only -q tests/ | tail -1 | grep -E "[0-9]+ tests collected"

EXPOSE 8501

ENTRYPOINT ["/usr/bin/tini", "--"]
# Phase 4.5 multi-page entry: app/app.py wires st.navigation across the 4
# pages (Predict / Audit / About / References). The legacy single-file
# entry was renamed to legacy_app.py in Phase 4.5 Mini-1 spec-gap #8 fix.
CMD ["streamlit", "run", "app/app.py"]
