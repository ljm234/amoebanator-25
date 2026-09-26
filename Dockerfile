# Amoebanator V1.1 - runtime container.
#
# Two-stage build keeps the final image small:
#   Stage 1 (builder): install pip dependencies into a venv.
#   Stage 2 (runtime): copy the venv + source, expose Streamlit on 8501.
#
# Build:
#   docker build -t amoebanator:v1.1 .
# Run dashboard:
#   docker run --rm -p 8501:8501 amoebanator:v1.1
# Run a single CLI inference:
#   docker run --rm amoebanator:v1.1 \
#       python scripts/inference/infer_cli.py --json '{"age":12,"csf_glucose":18,...}'

# --- Stage 1: builder -----------------------------------------------------
FROM python:3.12-slim AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /build

# Build tools and certificates for the pip install below.
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
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

# --- Stage 2: runtime -----------------------------------------------------
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PATH="/opt/venv/bin:$PATH" \
    AMOEBANATOR_AUDIT_PATH=/app/outputs/audit/audit.jsonl \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0

# AMOEBANATOR_RESEARCH_MODE - research-mode switch
#
#   The model is trained on 24 of 30 synthetic rows created for this demo: no
#   real PHI and no human subjects, so no IRB review is required. With this
#   variable set, the predict page shows a research-mode banner and writes an
#   audit event (AuditEventType.IRB_STATUS_CHANGE, actor="env_var"), and
#   ml/irb_gate.py, if called, skips the IRB record check and logs the skip.
#
#   The skip applies to any dataset, so this research mode is appropriate only
#   while the app runs on synthetic data. Without it, ml/irb_gate.py treats
#   only simulated, synthetic and bridge sources as synthetic; a MIMIC-IV
#   cohort (source mimic_iv) needs an IRB record like any real dataset. The
#   author holds PhysioNet credentialed access to MIMIC-IV, but the MIMIC-IV
#   proxy study in docs/rare_class_design.md is a pre-specified protocol that
#   is not scheduled, and the repository ships no MIMIC data.
#
ENV AMOEBANATOR_RESEARCH_MODE=1

# tini for clean signal handling.
RUN apt-get update && apt-get install -y --no-install-recommends \
        tini \
    && rm -rf /var/lib/apt/lists/*

# Bring the venv built in stage 1.
COPY --from=builder /opt/venv /opt/venv

# Non-root user.
RUN useradd --create-home --shell /bin/bash amoeba
USER amoeba
WORKDIR /app

# Copy source. .dockerignore leaves out caches, IDE metadata, the local audit
# log and the metrics figures (outputs/metrics/*.png).
COPY --chown=amoeba:amoeba . /app

# Health check: probe Streamlit's own health endpoint, which answers once the
# server is up; torch is imported later, when a session first opens the
# Predict or About page. Failed probes during the 90 s start-period do not
# count toward retries.
HEALTHCHECK --interval=30s --timeout=5s --start-period=90s --retries=3 \
  CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://localhost:8501/_stcore/health', timeout=4).status==200 else 1)"

EXPOSE 8501

ENTRYPOINT ["/usr/bin/tini", "--"]
# streamlit_app.py wires st.navigation across the 4 pages (Predict / Audit /
# About / References). It lives at the repo root, where the CMD below names
# it; its docstring explains why it cannot be app/app.py.
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
