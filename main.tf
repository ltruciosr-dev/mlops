# main.tf

provider "google" {
  credentials = file("<path-to-your-service-account-json>")
  project     = var.project_id
  region      = var.region
}

module "compute_instance" {
  source = "./modules/compute"

  # Pass necessary variables to the module
  name          = "ml-torch"
  machine_type  = "n1-standard-2"
  image         = "debian-cloud/debian-10"
  expose_port   = 8000
}