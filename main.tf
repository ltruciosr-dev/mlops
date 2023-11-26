# main.tf

provider "google" {
  credentials = file("<path-to-your-service-account-json>")
  project     = "your-gcp-project-id"
  region      = "us-central1"
}

module "compute_instance" {
  source = "./modules/compute"

  # Pass necessary variables to the module
  name          = "ml-torch"
  machine_type  = "n1-standard-2"
  image         = "debian-cloud/debian-10"
  expose_port   = 8000
}