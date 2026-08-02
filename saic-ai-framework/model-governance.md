# ⚖️ SAIC Model Governance & Prompt Safety Guidelines

**Classification:** `UNCLASSIFIED // INTERNAL USE ONLY`

## Model Routing Guidelines
1. **Low-Latency / Real-Time Tasks:** Route to `gemini-2.0-flash` on Vertex AI (average latency < 350ms).
2. **Complex Solicitations / 1M+ Token Technical Volumes:** Route to `gemini-3.1-pro` on Vertex AI.
3. **Independent Legal & Compliance Audit:** Route to `claude-3-5-sonnet` on Vertex AI.
4. **Data Privacy Guardrails:** System prompts must mandate retrieval grounding from authorized data stores and prohibit external unverified web scraping.
