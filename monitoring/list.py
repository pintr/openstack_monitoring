"""
List monasca resources
"""


def list_alarms(client):
    print("Monasca Alarms")

    for alarm in client.alarms.list():
        print(alarm)


def list_alarm_definitions(client):
    print("Monasca Alarms Definitions")

    for definition in client.alarm_definitions.list():
        print(definition)


def list_metrics(client):
    print("Monasca Metrics")

    for metric in client.metrics.list():
        print(metric)


def list_notifications(client):
    print("Monasca Notifications")

    for notification in client.notifications.list():
        print(notification)
