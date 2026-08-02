# 📜 SAIC Enterprise CI/CD & FedRAMP Compliance Policy

**Classification:** `UNCLASSIFIED // INTERNAL USE ONLY`  
**Policy Standard:** `SAIC-SEC-POL-04`

## Mandatory Pipeline Enforcements
1. All microservice repositories must include `.github/workflows/secops-gate.yml`.
2. Pull requests must pass automated linting, unit tests (>80% coverage), and container vulnerability scans before merging into `main`.
3. Deployment credentials must use short-lived GCP Workload Identity Federation tokens (no hardcoded long-lived service account JSON keys).
