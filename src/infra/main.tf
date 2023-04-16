resource "google_storage_bucket" "taxi_landing" {
  name = "k-taxi-landing-zone"
  location = var.region
  project = var.project_id
  force_destroy = true
}

resource "google_storage_bucket" "taxi_processing" {
  name = "k-taxi-processing-zone"
  location = var.region
  project = var.project_id
  force_destroy = true
}

resource "google_bigquery_dataset" "dataset_taxi_staging" {
  dataset_id    = "k_taxi_staging"
  friendly_name = "k_taxi_staging"
  description   = "Data Platform - Taxi Staging DW"
  location      = var.region
  project = var.project_id
}

