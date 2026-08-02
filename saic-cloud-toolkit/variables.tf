variable "project_id" {
  description = "Target GCP Project ID for SAIC Workloads"
  type        = string
  default     = "saic-argolis-project"
}

variable "project_number" {
  description = "GCP Project Number"
  type        = string
}

variable "region" {
  description = "Primary GCP Region (FIPS compliant)"
  type        = string
  default     = "us-east4"
}

variable "pipeline_service_account" {
  description = "Service Account for CI/CD Pipelines"
  type        = string
  default     = "saic-agent-pipeline-sa@saic-proposal-ops.iam.gserviceaccount.com"
}
