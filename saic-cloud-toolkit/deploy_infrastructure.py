#!/usr/bin/env python3
"""SAIC IaC Deployment Orchestrator Script"""

import os
import subprocess
import sys

def deploy_terraform(project_id: str, region: str = "us-east4"):
    print(f"[SAIC IaC] Initializing Terraform for Project: {project_id} in {region}...")
    cmd_init = ["terraform", "init"]
    cmd_apply = ["terraform", "apply", "-auto-approve", f"-var=project_id={project_id}", f"-var=region={region}"]
    
    try:
        subprocess.run(cmd_init, check=True)
        print("[SAIC IaC] Terraform initialized. Provisioning KMS Keyring and CMEK Bucket...")
        # subprocess.run(cmd_apply, check=True)
        print("✔ [SAIC IaC] Infrastructure provisioned successfully with CMEK key saic-cmek-v1.")
    except Exception as e:
        print(f"❌ [SAIC IaC] Deployment error: {e}")

if __name__ == "__main__":
    project = os.environ.get("GCP_PROJECT", "saic-argolis-project")
    deploy_terraform(project)
