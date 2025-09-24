FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


# Copy the project into the image
ADD . /app

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app
RUN uv sync --locked
EXPOSE 80
CMD ["uv", "run", "uvicorn", "ml_service.core_api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]