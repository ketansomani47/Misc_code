import boto3
import json
from datetime import datetime


def send_to_event_bus(payload, detail_type):
    """
    Send the payload to event bus to further process and send to event framework application
    :param payload: data that need to be sent
    :param detail_type: Type of event action
    :return: response returned from put_events or None on exception
    """
    try:
        active_region = "us-east-1"
        env = "lab"
        entries = [
            {
                "EventBusName": f"settings-event-auditing-bus-{active_region}-{env}",
                "Source": "Common Settings Auditing",
                "Time": datetime.now(),
                "DetailType": detail_type,
                "Detail": json.dumps(payload),
            }
        ]
        client = boto3.client("events", region_name=active_region)
        response = client.put_events(Entries=entries)
        return response
    except Exception as e:
        print(str(e))


detail = "AuditCheck"
data = {
    "key1": "value1",
    "key2": [1, 2],
    "key3": {"flag": False}
}
respons = send_to_event_bus(data, detail)
print(respons)
