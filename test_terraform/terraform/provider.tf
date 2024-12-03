provider "alks" {
  url = "https://alks.coxautoinc.com/rest"
  default_tags {
    tags = local.tags
  }
  ignore_tags {
    key_prefixes = [
      "cai:",
      "coxauto-ssm",
      "coxauto:ssm",
      ]
  }
}

provider "aws" {
  region = var.region
  default_tags {
    tags = local.tags
  }
  ignore_tags {
    key_prefixes = [
      "cai:",
      "coxauto-ssm",
      "coxauto:ssm",
      ]
  }
}

terraform {
  required_version = "=1.5.7"
  backend "s3" {
    key = "fni-settings-event-bridge"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "=5.24.0"
    }
    alks = {
      source  = "Cox-Automotive/alks"
      version = "=2.5.0"
    }
  }
}
