import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student')

def handler(event, context):
	queryParam = event['queryStringParameters']
	print('query param', queryParam)
	search_by = queryParam['searchBy']
	message = 'Success'
	try:
		if search_by == 'id':
			result = table.query(
				KeyConditionExpression=Key('id').eq(queryParam['id'])
			)
		else:
			firstname = queryParam.get('firstname')
			lastname = queryParam.get('lastname')
			if(firstname and not lastname):
				expression = Attr('firstname').contains(firstname)
			if (firstname and lastname):
				expression = (Attr('firstname').contains(firstname) & Attr('lastname').contains(lastname))
			if(lastname and not firstname):
				expression = Attr('lastname').contains(lastname)
			result = table.scan(
				FilterExpression=expression
			)
		items = result['Items']
	except BaseException as e:
		message = str(e)

	response = {
		'statusCode': 200,
		'body': json.dumps({
			'message': message,
			'items': items
		}),
		'headers': {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*',
			'Access-Control-Allow-Credentials': 'true'
		}
	}
	return response