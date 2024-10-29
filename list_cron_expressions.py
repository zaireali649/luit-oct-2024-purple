import boto3

eventbridge = boto3.client('events')

response = eventbridge.list_rules()

rules = response["Rules"]

for rule in rules:
    response = eventbridge.describe_rule(Name=rule["Name"])

    print(response["Name"], response["ScheduleExpression"])