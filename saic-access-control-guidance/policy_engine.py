#!/usr/bin/env python3
"""
SAIC Access Guidance Policy Evaluation Engine Code
"""

import json
import re

class GuidancePolicyEngine:
    def __init__(self, policy_json_path: str = "Access_Control_Policy.json"):
        self.policy_json_path = policy_json_path
        self.rules = self._load_rules()

    def _load_rules(self):
        return [
            {"id": "RULE-001", "scope": ["UNCLASSIFIED", "INTERNAL"], "action": "ALLOW"},
            {"id": "RULE-002", "scope": ["CUI", "RESTRICTED"], "keywords": ["passphrase", "master key", "siprnet"], "action": "DENY_WITH_REDACTION"}
        ]

    def evaluate_request(self, user_role: str, file_path: str, content: str) -> dict:
        if "RESTRICTED_CUI" in file_path or any(kw in content.lower() for kw in ["master passphrase", "siprnet"]):
            return {
                "decision": "DENY_WITH_REDACTION",
                "rule": "RULE-002",
                "redacted_content": re.sub(r"0x[0-9A-Fa-f]+", "[REDACTED_CUI_PASSPHRASE]", content)
            }
        return {"decision": "ALLOW", "rule": "RULE-001", "redacted_content": content}
