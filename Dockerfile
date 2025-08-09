FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    APP_HOME=/app

WORKDIR $APP_HOME

# System packages (curl for healthcheck, libenchant for pyenchant, dictionary for en_US lookups)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    curl ca-certificates libenchant-2-2 hunspell-en-us && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN useradd -m appuser && chown -R appuser:appuser $APP_HOME
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s CMD curl -f http://localhost:${PORT:-8080}/hello || exit 1

# Cloud Run sets PORT (default 8080). Use that when launching gunicorn; fall back to 8080 locally if unset.
CMD ["bash", "-c", "gunicorn --bind 0.0.0.0:${PORT:-8080} --workers 3 --threads 4 --timeout 120 app:app"]
