import log
import dynamodb_handler as dynamodb
import sqs_handler as sqs
import json
import time
import general_tools as gt
from boto3.dynamodb.conditions import Key, Attr

# read messages from SQS
# sqs_url = 'https://sqs.us-east-2.amazonaws.com/120404667225/convert_html_to_pdf' # eslam
# user_profile = "eslam"

sqs_url = "https://sqs.us-east-2.amazonaws.com/319349704364/convert_html_to_pdf" # sandbox
user_profile = "sand"
sqs_handler = sqs.SQSHandler(sqs_url, user_profile=user_profile)
print(f"Number of messages in the queue: {sqs_handler.count_messages()}")
dynamodb_table = "convert_html_to_pdf"

# check if this table exists in DynamoDB if not create it
dynamodb_handler = dynamodb.DynamoDBHandler(table_name=dynamodb_table, user_profile=user_profile)

# get failed records
failed_records = dynamodb_handler.query_items(key_condition_expression=Key("status"), filter_expression=Attr("failed"),
                                              index_name="StatusProjectIndex")

if not dynamodb_handler.table_exists():
    key_schema = [
        {'AttributeName': 's3_path', 'KeyType': 'HASH'},
    ]

    attribute_definitions = [
        {'AttributeName': 's3_path', 'AttributeType': 'S'},
        {'AttributeName': 'status', 'AttributeType': 'S'},
        {'AttributeName': 'project_id', 'AttributeType': 'S'},
        {'AttributeName': 'task_id', 'AttributeType': 'S'},
    ]

    global_secondary_indexes = [
        {
            'IndexName': 'StatusProjectIndex',
            'KeySchema': [
                {'AttributeName': 'status', 'KeyType': 'HASH'},
                {'AttributeName': 'project_id', 'KeyType': 'RANGE'},
                {'AttributeName': 'task_id', 'KeyType': 'RANGE'},
            ],
            'Projection': {'ProjectionType': 'ALL'}
        }
    ]

    dynamodb_handler.create_table_if_not_exists(key_schema=key_schema, attribute_definitions=attribute_definitions,
                                                global_secondary_indexes=global_secondary_indexes,
                                                billing_mode="PAY_PER_REQUEST")

# get record from dynamodb
# record = dynamodb_handler.get_item({"s3_path": "s3://bitbucket/file_8.html"})

# dynamodb_handler.delete_table()
# print(f"Table deleted: {dynamodb_handler.table_name}")

status = ["completed", "failed"]
for message in sqs_handler.receive_messages(max_number=10):
    print(f"Received message: {message['Body']}")
    message_body = json.loads(message['Body'])
    s3_path = message_body['s3_path']
    new_s3_path = message_body['new_s3_path']

    # insert message to dynamodb
    item = {
        "s3_path": s3_path,
        "new_s3_path": new_s3_path,
        "project_id": "123",
        "error_message": "This is an error message",
        "number_of_retries": 1,
        "lambda_function_name": "html-to-pdf",
        "status": status[gt.random_number(0, 1)],
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }

    dynamodb_handler.create_item(item)
    print(f"Message inserted to DynamoDB: {item}")

    # delete message from SQS
    # sqs_handler.delete_message(message['ReceiptHandle'])

    # describe the table
    # print(f"Table description: {dynamodb_handler.describe_table()}")

# get failed records
failed_records = dynamodb_handler.query_items(filter_expression=Attr("failed"), index_name="StatusProjectIndex")

items = dynamodb_handler.query_items(
    Key('status').eq('failed'))
