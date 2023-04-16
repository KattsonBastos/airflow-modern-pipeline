#!/usr/bin/env bash
install() {
  echo "### Installing Astro CLI..."
 
  #curl -sSL install.astronomer.io | sudo bash -s -- v1.8.4

  # terraform
  echo "### Installing Terraform"
  sudo apt update && sudo apt install -y gnupg software-properties-common

  wget -O- https://apt.releases.hashicorp.com/gpg | \
    gpg --dearmor | \
    sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg

  gpg --no-default-keyring \
    --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
    --fingerprint

  echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
    https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/hashicorp.list

  sudo apt update
  sudo apt install terraform

  # gcloud
  echo "### Installing GCLOUD"
  echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

  sudo apt update

  sudo apt-get install google-cloud-sdk

  gcloud init

}

up() {

  ## 
  echo "Initializing Astro dev component.."
  #astro dev init ## uncomment if you're running for the first time

  ##
  echo "Starting Airflow Services"
  astro dev start --no-cache

}

case $1 in
  install)
    install
    ;;
  up)
    up
    ;;
  *)
    echo "Usage: $0 {up, install}"
    ;;
esac