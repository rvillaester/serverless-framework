import json

def handler(event, context):
	message = 'Congratulations - this is the lambda function behind a public AUTHENTICATED API'

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