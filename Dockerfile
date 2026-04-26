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
CMD ["streamlit", "run", "app.py"]
