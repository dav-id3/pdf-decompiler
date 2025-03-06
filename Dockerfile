### for builder
FROM python:3.13-slim AS builder

WORKDIR /workdir
RUN pip install --upgrade pip && pip install poetry
RUN poetry self add poetry-plugin-export poetry-plugin-shell
COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

### for prod
FROM python:3.13-bookworm AS prod
ENV PYTHONUNBUFFERED=1

WORKDIR /workdir
COPY src/ ./src
COPY --from=builder /workdir/requirements.txt requirements.txt
RUN apt-get update && apt-get install -y python3-tk poppler-utils
RUN pip install -r requirements.txt
