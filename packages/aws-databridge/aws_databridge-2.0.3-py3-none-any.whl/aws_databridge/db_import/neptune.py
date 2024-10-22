import csv
import pandas as pd
import boto3
import requests
import json
import os

NEP_ENDPOINT = os.getenv('NEP_ENDPOINT', 'db-neptune-1.cluster-cfsssmgsia9l.us-east-1.neptune.amazonaws.com')
IAM_ROLE_ARN = os.getenv('IAM_ROLE_ARN', 'arn:aws:iam::123456789012:role/NeptuneAccessDev')
IMPORT_BUCKET = os.getenv('IMPORT_BUCKET', 'default-bucket-name')

def import_to_neptune(file): 
    try:
        d_frame = pd.read_csv(file)
        print(f"Data loaded from {file}")
    except FileNotFoundError:
        print("File not found.")
        exit(1)
    except pd.errors.EmptyDataError:
        print("The provided file is empty. Please load appropriate file.")
        exit(1)

    node_id = input("Which column would you like to use as the unique identifier for the nodes? (Case-sensitive!): ")
    if node_id not in d_frame.columns:
        print(f"{node_id} not found in data.")
        exit(1)

    if d_frame[node_id].isnull().any():
        print("The column you identified contains null values. Please rectify.")
        exit(1)

    property_id = input("What are the column names you would like to use as the properties for your nodes?: ")
    if property_id not in d_frame.columns:
        print(f"{property_id} not found in data.")
        exit(1)

    relationship_id = input("Enter the column names that represent relationships, no name is fine: ")
    relationship_id = [rel.strip() for rel in relationship_id.split(',') if rel.strip()]

    vertex_export = "/home/ec2-user/vertex.csv"
    edges_export = "/home/ec2-user/edges.csv"

    with open(vertex_export, 'w', newline='') as v, open(edges_export, 'w', newline='') as e:
        vertex_mod = csv.writer(v)
        edge_mod = csv.writer(e)

        edge_id = 1

        vertex_mod.writerow(['~id', '~label'] + relationship_id)
        edge_mod.writerow(['~id', '~from', '~to', '~label'])

        for index, row in d_frame.iterrows():
            node_id_trace = f'{row[node_id]}'
            node_properties = [row[col] for col in property_id if col in d_frame.columns]
            vertex_mod.writerow([node_id, 'Node'] + node_properties)

            for rel_col in relationship_id:
                if rel_col in d_frame.columns and pd.notna(row[rel_col]):
                    related_node_id = f'{row[rel_col]}'
                    edge_mod.writerow([f'e{edge_id}', node_id, related_node_id, f'relatedTo_{rel_col.strip()}'])
                    edge_id += 1

    print('Vertices and edges CSV files have been written.')

    client_container = boto3.client('s3') 

    try: 
        client_container.upload_file(vertex_export, IMPORT_BUCKET, 'vertex.csv')
        print(f"{vertex_export} uploaded to S3 bucket: {IMPORT_BUCKET}")
        client_container.upload_file(edges_export, IMPORT_BUCKET, 'edges.csv')
        print(f"{edges_export} uploaded to S3 bucket: {IMPORT_BUCKET}")
    except boto3.exceptions.S3UploadFailedError as aws_err:
        print(f"Upload error: {aws_err}")
    except boto3.exceptions.NoCredentialsError as auth_err:
        print(f"Credentials error: {auth_err}")

    for s3_uri in [f's3://{IMPORT_BUCKET}/vertex.csv', f's3://{IMPORT_BUCKET}/edges.csv']:
        nep_url = f"https://{NEP_ENDPOINT}:8182/loader"

        payload_delivery = {
            "source": s3_uri,
            "format": "csv",
            "iamRoleArn": IAM_ROLE_ARN,
            "region": "us-east-1",
            "failOnError": "TRUE",
        }

        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(nep_url, data=json.dumps(payload_delivery), headers=headers, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            if response is not None:
                print(f"Error loading data to Neptune for {s3_uri}: {e}, Response details: {response.text}")
            else:
                print(f"Error loading data to Neptune for {s3_uri}: {e}")