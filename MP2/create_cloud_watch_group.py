import boto3
import json
AWS_REGION = "us-east-1"
client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 7
# Back end Log Group
# log_group = 'CS410_MP2_Sec1_Logs'
# response = client.create_log_group(
#     logGroupName=log_group,
#     tags={
#         'Type': 'Back end',
#         'Frequency': '30 seconds',
#         'Environment': 'Production',
#         'RetentionPeriod': str(retention_period_in_days)
#     }
# )
# print(json.dumps(response, indent=4))
# response = client.put_retention_policy(
#           logGroupName=log_group,
#           retentionInDays=retention_period_in_days
# )
#print(json.dumps(response, indent=4))
# Front end Log Group
log_group = 'CS410_MP2_Sec2_Logs'
response = client.create_log_group(
    logGroupName=log_group,
    tags={
        'Type': 'Front end',
        'Frequency': '30 seconds',
        'Environment': 'Production',
        'RetentionPeriod': str(retention_period_in_days)
    }
)
response = client.put_retention_policy(
          logGroupName=log_group,
          retentionInDays=retention_period_in_days
)
print(json.dumps(response, indent=4))