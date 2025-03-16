# Set the base image
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

# Set the working directory in the container
WORKDIR /app

# Vopy deps contracts and application code
COPY pyproject.toml uv.lock ./
COPY src/ /app/src/

# Install the application
RUN uv pip install -r pyproject.toml --system
RUN uv pip install -e . --system

# copy data
COPY data/00_asset/ /app/data/00_asset/

# Expose the port used by the application
EXPOSE 8080

# Start the application
ENTRYPOINT ["gunicorn", "src.ui.app:server", "--workers", "4", "--bind", "0.0.0.0:8080"]
