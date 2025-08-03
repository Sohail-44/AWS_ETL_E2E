# import json
# import boto3
# import pandas as pd
# import io
# from datetime import datetime 

# def lambda_handler(event, context):
#     # TODO implement

#     # flatten fucntion to flatten the data if its not flattened
#     def flatten_data(data):
#         orders_data = []
#         for order in data:
#             for product in order['products']:
#                 row_orders = {
#                     'order_id': order['order_id'],
#                     'order_date': order['order_date'],
#                     'total_amount': order['total_amount'],
#                     'customer_id': order['customer']['customer_id'],
#                     'customer_name': order['customer']['name'],
#                     'email' : order['customer']['email'],
#                     'address': order['customer']['address'],
#                     'product_id': product['product_id'],
#                     'product_name': product['name'],
#                     'category': product['category'],
#                     'price' : product['price'],
#                     'quantity': product['quantity']
#                 }
#                 orders_data.append(row_orders)
#         df_orders = pd.DataFrame(orders_data)
#         return df_orders

#     current_bucket_name = event['Records'][0]['s3']['bucket']['name']
#     file_object_name = event['Records'][0]['s3']['object']['key']

#     # don't need to pass credential keys as we have already given permission access to s3 
#     s3_client = boto3.client('s3') 
#     our_response = s3_client.get_object(Bucket=current_bucket_name, Key=file_object_name)

#     # the data in our response se is in bytes so we need to decode it to utf-8 in string format
#     our_data = our_response['Body'].read().decode('utf-8') 

#     # loading it via json's load method
#     data = json.loads(our_data)
#     df = flatten_data(data)

#     print(df) # amazing as the json file is uploaded it triggers the lambda and the unflattenned data is flattened which can be monitored cloud watch logs

#     # converting the df to parquet file (because parquet is better than csv in storage efficiency, query performance and data management)
#     parquet_buffer = io.BytesIO()
#     df.to_parquet(parquet_buffer, index=False, engine='pyarrow')

#     now = datetime.now()
#     timestamp = now.strftime("%Y%m%d%H%M%S")

#     # basically parquetting the data in the orders-parquet-datalake file 
#     key_staging = f"orders-parquet-datalake/orders_etl{timestamp}.parquet"
#     s3_client.put_object(Bucket=current_bucket_name, Key=key_staging, Body=parquet_buffer.getvalue())

#     # triggering the crawler once the data is uploaded in parqueted 
#     crawler = 'aws-etl-pipeline-crawler'
#     glue = boto3.client('glue') # interacting with glue
#     response = glue.start_crawler(Name=crawler)

#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }