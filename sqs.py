import boto3

def create_queue(qn):
    result=False
    try:
        queue = sqs.create_queue(QueueName=qn)
        print('Queue created')
        result = True
    except:
        print('Could not create queue: '+ qn)
    return result


def send_message(qn, body, dly, att):
    queue = sqs.get_queue_by_name(QueueName=qn)
    response = queue.send_message(MessageBody=body, DelaySeconds=dly, MessageAttributes=att)
    return response

def send_messages(qn, lst):
    queue = sqs.get_queue_by_name(QueueName=qn)
    response = queue.send_messages(Entries=lst)
    return response 

def receive_messages(qn, att):
    queue = sqs.get_queue_by_name(QueueName=qn)
    response = queue.receive_messages(MessageAttributeNames=att)
    return response

sqs=boto3.resource('sqs')
