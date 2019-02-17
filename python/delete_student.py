import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student')

def handler(event, context):
	payload = json.loads(event['body'])
	print('payload', payload)
	message = 'Success'
	try:
		table.delete_item(
			Key={
				'id': payload['id']
			}
		)
	except BaseException as e:
		message = str(e)

	response = {
		'statusCode': 200,
		'body': json.dumps({
			'message': message
		}),
		'headers': {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*',
			'Access-Control-Allow-Credentials': 'true'
		}
	}
	return response