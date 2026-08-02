#!/usr/bin/env python3
"""
SAIC Antigravity Multi-Model Router Code
========================================================================
Dynamically routes prompts between Google Gemini 3.1 Pro and Anthropic Claude 3.5 Sonnet.
"""

import os

class ModelRouter:
    def __init__(self, gcp_project: str):
        self.gcp_project = gcp_project

    def route_prompt(self, prompt: str, task_type: str = "synthesis") -> str:
        if task_type == "code_analysis" or "terraform" in prompt.lower():
            print(f"[Router] Directing prompt to Vertex AI Gemini 2.0 Flash...")
            return "gemini-2.0-flash"
        elif task_type == "legal_audit" or "compliance" in prompt.lower():
            print(f"[Router] Directing prompt to Vertex AI Anthropic Claude 3.5 Sonnet...")
            return "claude-3-5-sonnet@20240620"
        else:
            print(f"[Router] Directing prompt to Vertex AI Gemini 3.1 Pro...")
            return "gemini-3.1-pro"

if __name__ == "__main__":
    router = ModelRouter("saic-argolis-project")
    model = router.route_prompt("Review federal proposal compliance against CISA SLA", "compliance")
    print(f"✔ Selected Foundation Model: {model}")
