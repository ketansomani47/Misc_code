import boto3
region = "us-east-1"
queue = "DecisionAdapterQueue-lab.fifo"
sqs = boto3.resource("sqs", region_name=region)
queue = sqs.get_queue_by_name(QueueName=queue)
print(queue)
