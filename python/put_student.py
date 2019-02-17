import boto3
import json

dynamo_db = boto3.resource('dynamodb')
student_table = dynamo_db.Table('student')
key_sequence_table = dynamo_db.Table('key_sequence')

def get_sequence():
	print('getting sequence')
	key_sequence = key_sequence_table.get_item(
		Key={
			'table_name': 'student'
		}
	)
	return key_sequence['Item']['sequence_no']

def create_student(student_id, payload):
	print('creating student')
	student_table.put_item(
		Item={
			'id': student_id,
			'firstname': payload['firstname'],
			'lastname': payload['lastname'],
			'email': payload['email'],
			#'birthdate': payload['birthdate'],
			'address': payload['address'],
			'gender': payload['gender']
		}
	)

def increment_sequence(sequence):
	print('incrementing sequence')
	newSequence = sequence + 1
	key_sequence_table.update_item(
		Key={
			'table_name': 'student'
		},
		UpdateExpression='SET sequence_no = :sequence_no',
		ExpressionAttributeValues={
			':sequence_no': newSequence
		}
	)
	print('incrementing sequence 123')

def handler(event, context):
	payload = json.loads(event['body'])
	print('payload', payload)
	message = 'Success'
	try:
		sequence = get_sequence()
		student_id = 'STD-' + str(sequence)
		create_student(student_id, payload)
		increment_sequence(sequence)
	except BaseException as e:
		message = str(e)

	print(message)
	response = {
		'statusCode': 200,
		'body': json.dumps({
			'message': message,
			'id': student_id
		}),
		'headers': {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*',
			'Access-Control-Allow-Credentials': 'true'
		}
	}
	return response

