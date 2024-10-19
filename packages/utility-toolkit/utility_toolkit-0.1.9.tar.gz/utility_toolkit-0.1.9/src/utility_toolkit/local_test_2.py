import log
import dynamodb_handler as dynamodb
import sqs_handler as sqs
import json
import time
import general_tools as gt
from boto3.dynamodb.conditions import Key, Attr

dynamodb_table = "html_to_pdf"
# Assuming you've already created your DynamoDBHandler instance
handler = dynamodb.DynamoDBHandler(dynamodb_table, 'us-east-2', 'eslam')

# Create a filter expression for status = 'failed'
filter_expression = Attr('status').eq('failed')


# Scan the table with the filter
failed_items = handler.scan_items(filter_expression=filter_expression)

# Print the results
print(f"Found {len(failed_items)} items with status 'failed':")
for item in failed_items:
  print(item)



# Create a key condition expression for status = 'failed'
key_condition_expression = Key('project_id').eq('123') & Key('status').eq('completed')
# filter_expression = Attr('s3_path').eq('s3://bitbucket/file_8.html')

# Query the GSI
failed_items = handler.query_items(
  key_condition_expression=key_condition_expression,
  # filter_expression=filter_expression,
  index_name='StatusProjectIndex'
)

# Print the results
print(f"Found {len(failed_items)} items with status 'failed':")
for item in failed_items:
  print(item)