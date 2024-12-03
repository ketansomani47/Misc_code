
resource "aws_cloudwatch_log_group" "event_logs" {
  name = "settings-events-auditing-logging-${var.region}-${terraform.workspace}"
  retention_in_days = 3
}

resource "aws_cloudwatch_event_bus" "event_bus" {
  name = "settings-event-auditing-bus-${var.region}-${terraform.workspace}"
}

/*resource "aws_cloudwatch_event_rule" "auditing_send_rule" {
  name           = "settings-auditing-send-rule-${var.region}-${terraform.workspace}"
  event_bus_name = aws_cloudwatch_event_bus.event_bus.name

  depends_on = [aws_cloudwatch_event_bus.event_bus]

  event_pattern = <<EOF
{
  "account": [
    "805080102354",
    "581378238327",
    "607694952559"
  ]
}
EOF
}

resource "aws_cloudwatch_event_target" "auditing_send_rule_target" {
  rule           = aws_cloudwatch_event_rule.auditing_send_rule.name
  event_bus_name = aws_cloudwatch_event_bus.event_bus.name
  target_id      = "settings-auditing-send-rule"
  role_arn       = alks_iamrole.fni_settings_auditing_event_rule_role.arn
  arn            = lookup(var.dr_inbound_deal_arn[var.region], terraform.workspace, var.dr_inbound_deal_arn[var.region]["lab"])

  depends_on = [aws_cloudwatch_event_rule.auditing_send_rule]
}
*/
resource "aws_cloudwatch_event_rule" "settings_auditing_log_rule" {
  name           = "settings-auditing-logging-rule-${var.region}-${terraform.workspace}"
  event_bus_name = aws_cloudwatch_event_bus.event_bus.name

  depends_on = [aws_cloudwatch_event_bus.event_bus]

  event_pattern = <<EOF
{
  "account": [
    "805080102354",
    "581378238327",
    "607694952559"
  ],
  "source": ["Common Settings Auditing"]
}
EOF
}

resource "aws_cloudwatch_event_target" "settings_auditing_log_rule_target" {
  rule           = aws_cloudwatch_event_rule.settings_auditing_log_rule.name
  event_bus_name = aws_cloudwatch_event_bus.event_bus.name
  target_id      = "settings-auditing-events-logging"
  arn            = aws_cloudwatch_log_group.event_logs.arn

  depends_on = [aws_cloudwatch_event_rule.settings_auditing_log_rule]
}
