FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    APP_HOME=/app \
    PORT=5001

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

EXPOSE 5001

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s CMD curl -f http://localhost:${PORT}/hello || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "3", "--threads", "4", "--timeout", "120", "app:app"]
