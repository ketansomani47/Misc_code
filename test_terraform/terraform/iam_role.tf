
resource "alks_iamrole" "fni_settings_auditing_event_rule_role" {
  name = "fni-settings-auditing-event-rule-role-${var.region}-${terraform.workspace}"
  type = "Amazon CloudWatch Events"
  include_default_policies = true
}


resource "aws_iam_role_policy" "fni_settings_auditing_events_rule_role_policy" {
  name = "Acct-fni-settings-auditing-event-policy"
  role = alks_iamrole.fni_settings_auditing_event_rule_role.name
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "events:PutEvents",
        "events:PutRule"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
EOF
}
