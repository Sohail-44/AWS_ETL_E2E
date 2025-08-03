# AWS_ETL_E2E #
AWS_ETL_E2E is an End to End ETL Pipeline project completed on AWS. I have automated the entire ETL pipeline through a event trigger automation. Any json file containing customers order data when uploaded in  s3 will automatically be converted to parquet file (as parquet file has better storage efficiency and query performance compared to other file formats) in Lambda and can monitored via cloudwatchlogs, then glue extracts the metadata from the parqueted file, additionally I added the crawler and database  which crawls through the s3 and creates tables of the recently uploded file object in s3 and lastly in Athena I have wrote sql queries which views the database tables and adds to the rows whenever there is an incremental json file. I tested it with incremental json file and was able to see the entire automation work and see the added columns in the athena all by itself. 

Tech Stacks used : Python: boto3, io, pandas,datetime, json.  AWS : s3, Lambda(trigger event + python program deployment), glue(crawler, database), athena(sql query)


<img width="1662" height="832" alt="Screenshot 2025-08-03 at 5 19 37 PM" src="https://github.com/user-attachments/assets/7412d368-5f44-4469-a442-0880ca7a17cb" />
<img width="1647" height="481" alt="Screenshot 2025-08-03 at 5 20 23 PM" src="https://github.com/user-attachments/assets/01fdd932-d418-4ced-8843-6e80d615750e" />
<img width="898" height="335" alt="Screenshot 2025-08-03 at 5 22 29 PM" src="https://github.com/user-attachments/assets/d03f10ed-c909-4743-a2f1-c178514f3d90" />
<img width="1655" height="920" alt="Screenshot 2025-08-03 at 5 22 10 PM" src="https://github.com/user-attachments/assets/a1256340-ae49-4b89-9694-565697693189" />
<img width="1662" height="580" alt="Screenshot 2025-08-03 at 5 23 01 PM" src="https://github.com/user-attachments/assets/d6b894e2-e730-4382-82c3-a19157f4b058" />
<img width="1666" height="893" alt="Screenshot 2025-08-03 at 5 23 11 PM" src="https://github.com/user-attachments/assets/169ca56c-ac4c-4f2c-8de0-f530be5b72eb" />
<img width="1675" height="912" alt="Screenshot 2025-08-03 at 5 23 33 PM" src="https://github.com/user-attachments/assets/85acb300-147d-4790-a860-0a23dcc686ca" />
