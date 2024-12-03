variable "region" {
  type = string
  default = "us-east-1"
}

variable "environment" {
  type = string
}

locals {
  app_name        = "fni-settings-event-bridge"
  stack_name      = "${local.app_name}-${var.environment}-${var.region}"
  meta_data       = jsondecode(file("meta.json"))
  tags = {
    Stack             = local.stack_name
    "coxauto:ci-id"   = local.meta_data.component
    Environment       = var.environment
    Application       = local.meta_data.application
    Component         = local.meta_data.component
    Email             = local.meta_data.email
    Team              = local.meta_data.team
  }
}

/*variable "dr_inbound_deal_arn" {
  type = map
  default = {

    "us-east-1" = {
      "lab"  = "arn:aws:events:us-east-1:607694952559:event-bus/dr-inbound-deal-event-bus-labs-us-east-1"
      "ci"   = "arn:aws:events:us-east-1:683423058194:event-bus/dr-inbound-deal-event-bus-dev-us-east-1"
      "dvt1" = "arn:aws:events:us-east-1:683423058194:event-bus/dr-inbound-deal-event-bus-dev-us-east-1"
      "dvi1" = "arn:aws:events:us-east-1:683423058194:event-bus/dr-inbound-deal-event-bus-dev-us-east-1"
      "qa1"  = "arn:aws:events:us-east-1:683423058194:event-bus/dr-inbound-deal-event-bus-qa-us-east-1"
      "uat1" = "arn:aws:events:us-east-1:136093617899:event-bus/dr-inbound-deal-event-bus-uat-us-east-1"
      "pa"   =  "arn:aws:events:us-east-2:476603660399:event-bus/dr-inbound-deal-event-bus-pa-us-east-2"
      "prod" = "arn:aws:events:us-east-1:706165609771:event-bus/dr-inbound-deal-event-bus-prod-us-east-1"
    }

    "us-west-2" = {
      "lab"  = "arn:aws:events:us-west-2:607694952559:event-bus/dr-inbound-deal-event-bus-labs-us-west-2"
      "ci"   = "arn:aws:events:us-west-2:683423058194:event-bus/dr-inbound-deal-event-bus-dev-us-west-2"
      "dvt1" = "arn:aws:events:us-west-2:683423058194:event-bus/dr-inbound-deal-event-bus-dev-us-west-2"
      "dvi1" = "arn:aws:events:us-west-2:683423058194:event-bus/dr-inbound-deal-event-bus-dev-us-west-2"
      "qa1"  = "arn:aws:events:us-west-2:683423058194:event-bus/dr-inbound-deal-event-bus-qa-us-west-2"
      "uat1" = "arn:aws:events:us-west-2:136093617899:event-bus/dr-inbound-deal-event-bus-uat-us-west-2"
      "prod" = "arn:aws:events:us-west-2:706165609771:event-bus/dr-inbound-deal-event-bus-prod-us-west-2"
    }

  }
}*/
