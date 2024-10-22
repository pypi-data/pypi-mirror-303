import csv
import pandas as pd
import json

def text_to_csv(filepath):
    
    #test
    # test_text = """name age city
    # Jay 25 New_York
    # Abahn 30 Vegas
    # Matt 22 connecticut
    # name 28 Houston
    # """
    # with open("test_data.txt", "w") as file:
    #     file.write(test_text)
    #     filepath = "test_data.txt"

    with open(filepath, 'r') as file:
        lines = file.readlines()

    a_names = lines[0].split() #attribute names
    rows = [line.split() for line in lines[1:]] #tuple values

    new_filepath = filepath.replace('txt', 'csv')
    with open(new_filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(a_names)
        writer.writerows(rows)
    
    return new_filepath

def json_to_csv(filepath):
    #test
    # test_json = [
    #     {"name": "Jay", "age": 25, "city": "New York"},
    #     {"name": "Abahn", "age": 30, "city": "Vegas"},
    #     {"name": "Matt", "age": 22, "city": "connecticut"},
    #     {"name": "name", "age": 28, "city": "Houston"}
    # ]
    # with open("test_data.json", "w") as file:
    #     json.dump(test_json, file, indent=4)
    #     filepath = "test_data.json"
    data = pd.read_json(filepath)
    new_filepath = filepath.replace('json', 'csv')
    data.to_csv(new_filepath, index=False)

    return new_filepath

def xml_to_csv(filepath):

    # test 
    # test_xml = """<?xml version="1.0"?>
    # <data>
    #     <person>
    #         <name>Jay</name>
    #         <age>25</age>
    #         <city>New York</city>
    #     </person>
    #     <person>
    #         <name>Abahn</name>
    #         <age>30</age>
    #         <city>Vegas</city>
    #     </person>
    #     <person>
    #         <name>Matt</name>
    #         <age>22</age>
    #         <city>connecticut</city>
    #     </person>
    #     <person>
    #         <name>name</name>
    #         <age>28</age>
    #         <city>Houston</city>
    #     </person>
    # </data>"""

    # # Write the XML to a file
    # with open("test_data.xml", "w") as file:
    #     file.write(test_xml)
    #     filepath = "test_data.xml"

   data = pd.read_xml(filepath)
   new_filepath = filepath.replace('xml', 'csv')
   data.to_csv(new_filepath, index=False)
    
   return new_filepath

def csv_to_json(filepath):
    data = pd.read_csv(filepath)
    new_filepath = filepath.replace('csv', 'json')
    data.to_json(new_filepath, orient='records', indent=4)
    
    return new_filepath


