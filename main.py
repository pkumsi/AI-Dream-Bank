import boto3
from botocore.exceptions import ClientError
from dreambank import fetch_dreams

# Initialize a session using your credentials
dynamodb = boto3.resource('dynamodb')

# Specify your DynamoDB table
table_name = 'Dreams'  # Update this with your table name
table = dynamodb.Table(table_name)

# Example dream data (assuming `dreams` is a list of dream texts)
dreams = [
    "I was looking at the moon and another thing that kinda looked like a cutesie-poo sun...",
    "It was Bring Your Pet Day at the Science Faire at my school..."
    # Add more dreams as needed
]

# Upload each dream to DynamoDB
for i, dream_text in enumerate(dreams):
    try:
        # Prepare the item to insert
        item = {
            'ID': f'dream-{i}',  # Unique identifier for each dream
            'DreamText': dream_text  # The dream text
        }

        # Insert the item into the table
        table.put_item(Item=item)
        print(f"Successfully inserted dream {i} into DynamoDB.")
    except ClientError as e:
        print(f"Error inserting dream {i}: {e.response['Error']['Message']}")
