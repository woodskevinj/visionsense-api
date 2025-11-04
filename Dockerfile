# ==============================================================
# 🐳  VisionSense API - Dockerfile
# ==============================================================

# -----------------------------
# Stage 1 — Build Environment
# -----------------------------
FROM python:3.10-slim AS builder

# Set work directory
WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install OS dependencies (for pillow, torch, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application source
COPY . .

# -----------------------------
# Stage 2 — Final Runtime Image
# -----------------------------
FROM python:3.10-slim AS runtime

WORKDIR /app

# Copy only installed packages and source code from builder
COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

# Expose FastAPI port
EXPOSE 8000

# Set default environment variable for host
ENV PORT=8000

# Run the FastAPI app via Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
