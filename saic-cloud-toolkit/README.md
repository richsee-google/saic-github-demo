# ☁️ SAIC Cloud Automation Toolkit (`saic-cloud-toolkit`)

**Classification:** `UNCLASSIFIED // INTERNAL USE ONLY`  
**Repository Visibility:** `Internal / Public`  
**Maintainer:** SAIC Cloud Architecture Practice (`cloud-architecture@saic.com`)

---

## 📌 Overview
The **SAIC Cloud Automation Toolkit** provides enterprise-grade infrastructure-as-code (IaC) templates, Terraform modules, and GCP Argolis automation scripts tailored for federal civilian and defense workloads.

## 🛠️ Key Capabilities
1. **Automated CMEK KMS Keyring Provisioning:**
   - Terraform modules for creating symmetric KMS keyrings in `us-east4` and `us-central1`.
   - Automatic binding of `roles/cloudkms.cryptoKeyEncrypterDecrypter` to Vertex AI service accounts.

2. **Secure GCS Bucket Hardening:**
   - Enforces uniform bucket-level access, public access prevention, and retention policies.
   - Configures object versioning and default CMEK encryption.

3. **VPC Service Control Perimeter Automation:**
   - Pre-configured Access Context Manager rules for `aiplatform.googleapis.com` and `storage.googleapis.com`.
