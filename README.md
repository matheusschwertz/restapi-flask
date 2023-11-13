# Flask API with EKS Cluster using Terraform

Este é um projeto que utiliza Flask para criar uma API e Terraform para provisionar um cluster EKS na AWS.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados:

- [Python](https://www.python.org/) (3.6 ou superior)
- [Terraform](https://www.terraform.io/)
- [AWS CLI](https://aws.amazon.com/cli/)

## Configuração do Ambiente

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

python -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate
pip install -r requirements.txt
