# variables.tf

variable "project_id" {
  description = "The Google Cloud project ID"
}

variable "region" {
  description = "The region where resources will be created (e.g., us-central1)"
}

variable "name" {
  description = "Name of the VM instance"
}

variable "machine_type" {
  description = "Machine type for the VM (e.g., n1-standard-2)"
}

variable "image" {
  description = "The image for the VM's boot disk (e.g., debian-cloud/debian-10)"
}

variable "git_repository" {
  description = "URL of the Git repository with your MLOps code"
}

variable "expose_port" {
  description = "Port to expose for the API endpoint (e.g., 8000)"
}