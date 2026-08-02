# 🛡️ SAIC GitHub AI Agent Access Guidance & Guardrails

**Document Title:** `SAIC GitHub AI Retrieval Guidance Policy`  
**Target System:** `Enterprise AI Agents / GitHub Integration Connectors`  
**Governance Body:** `SAIC Security Architecture & CISO`

---

## 📋 Executive Mandate
When building or deploying an AI agent to retrieve code, technical documentation, or policy files from SAIC's GitHub organization:

1. **Connection Capability:** The agent connects to GitHub via GitHub REST API / OAuth2 / PAT.
2. **Access Limitation Based on Guidance:**
   - **Step 1:** The agent MUST inspect repository metadata and file classification tags (`UNCLASSIFIED`, `INTERNAL`, `CUI`, `RESTRICTED`).
   - **Step 2:** For `UNCLASSIFIED` / `INTERNAL` repos (e.g. `saic-cloud-toolkit`, `saic-devsecops-pipeline`, `saic-ai-framework`), the agent retrieves and synthesizes data freely.
   - **Step 3:** For `CUI` / `RESTRICTED` repos (e.g. `saic-gov-security-policy`), the agent applies the **Guidance Access Control Engine**. It MUST redact secret key strings, block unauthorized raw file extraction, and log an security audit event to GCP Cloud Audit Logs.
