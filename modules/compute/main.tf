# modules/compute/main.tf

resource "google_compute_instance" "model_instance" {
  name         = var.name
  machine_type = var.machine_type
  
  # Configure the boot disk with Debian 10 image
  boot_disk {
    initialize_params {
      image = var.image
    }
  }
  
  # Configure the network interface to use the default network
  network_interface {
    network = "default"
  }

  # Define the startup script to be executed when the VM starts
  metadata_startup_script = <<-SCRIPT
    #!/bin/bash
    sudo apt-get update
    sudo apt-get install -y git docker-compose
    
    # Clone the GitHub repository with your MLOps code
    git clone https://github.com/ltruciosr-dev/mlops.git
    
    # Change to the cloned directory and start the services with Docker Compose
    cd mlops
    docker-compose up -d
  SCRIPT


  allow {
    protocol = "tcp"
    ports    = [var.expose_port]
  }
}