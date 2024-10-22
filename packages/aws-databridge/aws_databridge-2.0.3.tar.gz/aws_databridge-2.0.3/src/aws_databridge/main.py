from aws_databridge.utils.convert_to import text_to_csv, json_to_csv, xml_to_csv, csv_to_json
from aws_databridge.db_import.rds import import_to_rds
from aws_databridge.db_import.dynamodb import import_to_dynamodb
from aws_databridge.db_import.document import import_to_documentdb
from aws_databridge.db_import.neptune import import_to_neptune
import boto3
import os

def main():
    import_path = input('Do you want to import data from your ec2 or s3? (ec2 = 1, s3 = 2): ')
    if import_path == '1':
        file = input('Enter the full name of the file (e.g. animals.txt , include folder path if applicable-> folder/animals.txt):')
        file = os.path.join('/home/ec2-user/', file)
        file_type = file.split('.')[1]
    elif import_path == '2':
        bucket = input('Enter the name of the bucket you would like to import data from: ')
        file = input('Enter the full name of the file (e.g. animals.txt): ')
        file_type = file.split('.')[1]
        s3 = boto3.client('s3')
        local_file_path = os.path.join('/home/ec2-user/', file) 
        s3.download_file(bucket, file, local_file_path )
        file = local_file_path
        file_type = file.split('.')[1]


    db_choice = input('What database would you like to import this data to? (rds = 1, dynamo = 2, neptune = 3, documentDB = 4): ')
    table_name = input('Enter the name of the table you would like to import this data to: ')

   # import data to the selected database, allowing for multiple imports if neccessary 
    stop = 0;
    while stop == 0:

        #convert supported non csv types to csv
        if file_type != 'csv':
            if file_type == 'txt':
                print('Converting data to csv...')
                file = text_to_csv(file)
                print('Data has been converted to csv')
                file_type = 'csv'
            elif file_type == 'json' and db_choice != '3':
                print('Converting data to csv...')
                file = json_to_csv(file)
                print('Data has been converted to csv')
                file_type = 'csv'
            elif file_type == 'xml':
                print('Converting data to csv...')
                file = xml_to_csv(file)
                print('Data has been converted to csv')
                file_type = 'csv'
        if db_choice == '3' and file_type == 'csv':
            print('Converting data to json...')
            file = csv_to_json(file)
            print('Data has been converted to json')
            file_type = 'json'

        if db_choice == '1':
            import_to_rds(file, table_name)
        elif db_choice == '2':
            primary_key = input('Enter the primary key for the table: ')
            import_to_dynamodb(file, table_name, primary_key)
        elif db_choice == '3':
            import_to_neptune(file)
            print('Data has been imported to Neptune')
        elif db_choice == '4':
            import_to_documentdb(file)
            print('Data has been imported to DocumentDB')
        stop = int(input('Would you like to import this file to another database? (yes = 0, no = 1): '))
        if stop == 0:
            db_choice = input('What database would you like to import this data to? (rds = 1, dynamo = 2, neptune = 3, documentDB = 4): ')
            table_name = input('Enter the name of the table you would like to import this data to: ')

    # Delete the S3 file after processing
    if import_path == '2':
        try:
            os.remove(file)
            print(f"File '{file}' has been deleted from the EC2 instance.")
        except FileNotFoundError:
            print(f"File '{file}' not found.")
        except Exception as e:
            print(f"Error deleting file: {e}")

if __name__ == '__main__':
    main()