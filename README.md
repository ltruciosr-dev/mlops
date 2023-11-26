# MLOps Lifecycle

This project serves as a demonstration of the Machine Learning (ML) lifecycle using Docker and Continuous Integration/Continuous Deployment (CI/CD)

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [CI/CD](#cicd-integration)
- [IaC with Terraform](#iac-with-terraform)
- [Contributing](#contributing)

## Overview

The primary goal of this project is to showcase the end-to-end ML lifecycle, highlighting the use of Docker for containerization, CI/CD pipleines for automation, and unit testing for ensuring code quality.

1. **ML Model Endpoint Service:** This deploys a container with a FastAPI endpoint for the ML model.

2. **ML Model Testing Service:** This deploys a container for testing the ML model.

In order to deploy a GCP infrastructure that is able to deploy the ML endpoint in a VM over a defined networking configuration, a terraform structure is implemented.

## Getting Started

To get a local copy of the project up and running, follow the steps below.

### Prerequisites

Ensure you have the following software and dependencies installed:

- [Docker](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/ltruciosr-dev/mlops.git

2. Navigate to the project directory:
    ```bash
    cd mlops

3. Deploy the FastAPI endpoint.
    ```bash
    docker-compose up --build

### ML Model Testing Service

Testing is automated for each pull-request by using [CML (CI/CD)](#cicd-integration), and also, a single run is performed each time the composed services are deployed.
```yml
tests:
  build: .
  command: pytest /tests  # Run pytest for the tests in the '/tests' directory
  volumes:
    - ./tests:/tests  # Mount the 'tests' directory from the local machine to '/tests' in the container
    - ./models:/app/models  # Mount the 'models' directory from the local machine to '/app/models' in the container
  depends_on:
    - app  # Ensure that the 'app' service is started before running tests
```

### ML Model Endpoint Service

Once the Docker Compose is up, you can access the FastAPI endpoint at [http://localhost:8000](http://localhost:8000).

```yml
app:
  build: .
  command: uvicorn main:app --host 0.0.0.0 --port 8000  # Run the UVicorn server for the FastAPI app
  ports:
    - "8000:8000"
  volumes:
    - ./models:/app/models  # Mount the 'models' directory from the local machine to '/app/models' in the container
```

## CI/CD Integration

The project utilizes CML (Continuous Machine Learning) by Iterative.AI for Continuous Integration & Continuous Deployment. The CI/CD pipeline is triggered automatically on both push and pull requests to the GitHub repository.

``` yaml
name: CML
on: [push]
jobs:
  train-and-report:
    permissions: write-all
    runs-on: ubuntu-latest
    container: docker://ghcr.io/iterative/cml:0-dvc2-base1
    steps:
      - uses: actions/checkout@v3
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - name: Test Model
        env:
          REPO_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          pip install -r ./.github/workflows/requirements.txt
          pytest -v ./tests > report.md # generate pytest output
          # Create CML report
          cml comment create report.md
```

The output of the model testing (training/monitor in other cases) is added as a comment in the [merge-commit](https://github.com/ltruciosr-dev/mlops/pull/3).

```c
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.4.3, pluggy-1.3.0 -- /usr/bin/python
cachedir: .pytest_cache
rootdir: /__w/mlops/mlops
collecting ... collected 2 items

tests/test_model.py::test_uniformity PASSED [ 50%]
tests/test_model.py::test_reproducibility PASSED [100%]

=============================== warnings summary ===============================
../../../usr/local/lib/python3.8/dist-packages/torch/nn/modules/transformer.py:20
/usr/local/lib/python3.8/dist-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: numpy.core.multiarray failed to import (Triggered internally at ../torch/csrc/utils/tensor_numpy.cpp:84.)
device: torch.device = torch.device(torch._C._get_default_device()), # torch.device('cpu'),

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================= 2 passed, 1 warning in 1.80s =========================
```

## IaC with Terraform

This project follows an Infrastructure as Code (IaC) approach for managing and provisioning cloud resources using Terraform. The IaC code is organized as follows:

### Directory Structure

The Terraform code is organized into modular and maintainable directories:

- **`main.tf`**: The main Terraform configuration file that defines the core infrastructure components and providers.

- **`variables.tf`**: Variable declarations used throughout the Terraform configuration to parameterize the infrastructure.

- **`modules/`**: Directory containing modularized Terraform modules for different components of the infrastructure. Each module focuses on a specific set of resources or functionalities.

### Modules

The Terraform modules are designed for reusability and encapsulation. Each module addresses a specific aspect of the infrastructure, such as networking, compute instances, or storage.

Here is an overview of the key modules used in this project:

- **`compute/`**: Manages compute resources such as virtual machines, instances, and associated configurations.

### Usage

To deploy or update the infrastructure, follow these steps:

1. Run `terraform init` to initialize the Terraform configuration.
2. Run `terraform plan` to review the proposed changes.
3. Run `terraform apply` to apply the changes and provision/update the infrastructure.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request.

## Acknowledgments

- Hat tip to [@ohsi36](https://github.com/oshi36/ml-ops-cml) for the CI/CD pipeline inspiration.
- Inspiration: [Continuous Machine Learning (CML)](https://cml.dev/)