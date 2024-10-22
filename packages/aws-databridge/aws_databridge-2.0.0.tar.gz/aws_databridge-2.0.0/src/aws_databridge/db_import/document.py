import pymongo as pym
import json
import os

# add a possible check for dictionaries

MONGO_URL = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
MONGO_USERNAME = os.getenv('MONGO_USERNAME', 'default-user')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'default_password')
MONGO_TLS = os.getenv('MONGO_TLS', 'global-bundle.pem')

CONNECT_URL = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_URL}?tls=true&tlsCAFile={MONGO_TLS}&retryWrites=false'

def import_to_documentdb(file):
    try:
        client = pym.MongoClient(CONNECT_URL) 

        db = client['database']
        collection = db['collection']
    except pym.errors.ConnectionFailure as err:
        print(f'Unable to connect to MongoDB: {err}')
        return None

    with open(file, 'r') as data:
        imported_data = json.load(data)

    if isinstance(imported_data, list):
        try:
            collection.insert_many(imported_data)
            print('Successfully inserted multiple collections.')
        except Exception as ex:
            print(f'Unable to insert documents: {ex}')
    else:
        try:
            collection.insert_one(imported_data)
            print('Successfully inserted singular collection.')
        except Exception as ex:
            print(f'Unable to insert document: {ex}')

    print('Now printing document to the terminal.')

    try:
        doc_doc = collection.find()
        for doc in doc_doc:
            print(doc)
    except Exception as err:
        print(f'Cannot fetch documents: {err}')

    print('Data has been imported to DocumentDB.')
    client.close()