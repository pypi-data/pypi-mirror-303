FROM python:3.10-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Install git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

ADD . /app
WORKDIR /app
RUN uv sync --frozen

ENV PATH="/app/.venv/bin:$PATH"
RUN uv build
CMD ["uv", "run", "whiteduck"]