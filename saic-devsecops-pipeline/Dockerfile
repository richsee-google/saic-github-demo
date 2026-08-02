# SAIC Hardened Enterprise Microservice Dockerfile
# Base: Minimal Distroless Python for FedRAMP Compliance
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3-debian12
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . /app

WORKDIR /app
EXPOSE 8080

# Enforce Non-Root Execution
USER 10001
CMD ["agent_service.py"]
