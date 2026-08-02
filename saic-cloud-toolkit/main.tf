# SAIC Enterprise Cloud Automation - Terraform Module
# Classification: UNCLASSIFIED // INTERNAL

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# KMS Keyring for FIPS 140-3 CMEK Encryption
resource "google_kms_key_ring" "saic_keyring" {
  name     = "saic-proposal-keyring"
  location = var.region
}

# Symmetric CryptoKey for Vertex AI & GCS
resource "google_kms_crypto_key" "cmek_key" {
  name            = "saic-cmek-v1"
  key_ring        = google_kms_key_ring.saic_keyring.id
  rotation_period = "7776000s" # 90 days

  purpose = "ENCRYPT_DECRYPT"
}

# IAM Binding for Vertex AI Service Agent
resource "google_kms_crypto_key_iam_binding" "vertex_cmek_binding" {
  crypto_key_id = google_kms_crypto_key.cmek_key.id
  role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"

  members = [
    "serviceAccount:service-${var.project_number}@gcp-sa-aiplatform.iam.gserviceaccount.com",
    "serviceAccount:${var.pipeline_service_account}"
  ]
}

# Secure Grounding Storage Bucket
resource "google_storage_bucket" "grounding_bucket" {
  name                        = "saic-proposal-grounding-bucket"
  location                    = var.region
  force_destroy               = false
  uniform_bucket_level_access = true

  encryption {
    default_kms_key_name = google_kms_crypto_key.cmek_key.id
  }

  versioning {
    enabled = true
  }
}
