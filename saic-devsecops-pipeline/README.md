# 🚀 SAIC DevSecOps Pipeline Framework (`saic-devsecops-pipeline`)

**Classification:** `UNCLASSIFIED // INTERNAL USE ONLY`  
**Repository Visibility:** `Internal`  
**Maintainer:** SAIC DevSecOps Working Group (`devsecops@saic.com`)

---

## 📌 Overview
Standardized CI/CD pipeline definitions for GitHub Actions and Cloud Build supporting automated security scanning, container signing, and FedRAMP compliance enforcement.

## 🔒 Automated Security Controls
* **Static Application Security Testing (SAST):** SonarQube & Semgrep scanning on every pull request.
* **Software Supply Chain Security:** Container images signed via Cosign / KMS keys.
* **Dependency Vulnerability Thresholds:** Automatic pipeline failure on Critical or High CVEs without approved mitigation waivers.
