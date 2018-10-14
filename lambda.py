# import boto3

# client = boto3.client('s3')
# s3 = boto3.resource('s3')

# bucket = 'mike-culhane'
# key = 'file.txt'

# resp = s3.meta.client.download_file(bucket, key, 'downloaded.txt')
# print(resp)

def lambda_handler(event, context):
	print('Hello World')