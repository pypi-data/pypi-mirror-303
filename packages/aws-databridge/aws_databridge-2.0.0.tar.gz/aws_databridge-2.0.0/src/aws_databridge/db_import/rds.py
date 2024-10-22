import csv 
import os 
import pymysql

#rds credentials stored in ec2
RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DB = os.getenv("RDS_DB")
RDS_PORT = int(os.getenv("RDS_PORT", 3306))

def import_to_rds(filepath, table_name):
    #connect to rds 
    try:
        conn = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            port=RDS_PORT
        )
    except pymysql.MySQLError as e:
        print(f"Error connecting to RDS: {e}")
        return None 
    
    #read data from file
    with open(filepath, 'r') as file:
        csv_reader = csv.DictReader(file)
        a_names = csv_reader.fieldnames
        rows = [list(row.values()) for row in csv_reader]

    #database object (cursor) to interact with the database
    with conn.cursor() as cur:
        # Create the database if it doesn't exist
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {RDS_DB}")
        conn.close()

    #redo the connection with the database specified 
    try:
        conn = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            db=RDS_DB,
            port=RDS_PORT,
            autocommit=True #prevents changes from being temporary
        )
    except pymysql.MySQLError as e:
        print(f"Error connecting to RDS: {e}")
        return None 
    
    with conn.cursor() as cur:
        # Dynamically create the table based on the CSV headers
        placeholders = ', '.join(f"{col} VARCHAR(255)" for col in a_names)  # Dynamic column creation
        cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({placeholders})")
            
        # Insert the data -> VALUES (%s, %s, %s, ...)
        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(a_names))})"
        cur.executemany(insert_query, rows)

    conn.close()

    print('Data has been imported to RDS')