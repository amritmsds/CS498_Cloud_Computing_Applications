import boto3
import time
from datetime import datetime

AWS_REGION = "us-east-1"

client = boto3.client('logs', region_name=AWS_REGION)

message = "Test CS410_MP2_Sec1_Logs/Stream creation" # replace here with your custom logging message
logGroupName = 'CS410_MP2_Sec1_Logs'# replace here with your log group name
logStreamName = 'CS410_MP2_Sec1_Stream' # replace here with your stream log name

# initial Cloudwatch configuration
response = client.create_log_stream(
    logGroupName=logGroupName,
    logStreamName=logStreamName
)

# log1
seq_token = None
log_event = {
    'logGroupName': logGroupName,
    'logStreamName': logStreamName,
    'logEvents': [
        {
            'timestamp': int(round(time.time() * 1000)),
            'message': message
        },
    ],
}
log_event['sequenceToken'] = seq_token
log1_response = client.put_log_events(**log_event)

# sleep for one second
time.sleep(1)

# log2
seq_token = log1_response['nextSequenceToken']
log_event = {
    'logGroupName': logGroupName,
    'logStreamName': logStreamName,
    'logEvents': [
        {
            'timestamp': int(round(time.time() * 1000)),
            'message': message
        },
    ],
}
log_event['sequenceToken'] = seq_token
log2_response = client.put_log_events(**log_event)