# AWS-DataBridge

AWS-DataBridge is a CLI application designed for AWS EC2 instances that allows users to import data from various file formats (XML, TXT, JSON, CSV) into multiple AWS databases including RDS, DynamoDB, Neptune, and DocumentDB. This tool automates the process of data conversion and storage, ensuring flexibility and ease of use for different database needs.

## Features

- Converts and imports XML, TXT, JSON, and CSV files into AWS databases.
- Supports AWS RDS, DynamoDB, Neptune, and DocumentDB.
- Provides flexibility for users to import data into multiple databases from a single file.
- Automatically creates tables and databases if they do not already exist.

## Installation

### To install AWS DataBridge using pip:

In your Ec2 instance run the following command

```bash
pip install aws-databridge
```

## Usage

After the install you can run the following command to run the program

```bash
aws-databridge
```

## Neccessary Environment Setup

There are some neccessary set up requirements in order to use the application without errors for each database

### IAM Role

Make sure your EC2 has the required IAM Role permissions attached to your EC2 instance for each of the databases you are attempting to import to

### RDS env variables

To interact with your RDS instance you need to have the following credentials stored on your EC2

```bash
export RDS_HOST="your-rds-endpoint.rds.amazonaws.com"
export RDS_USER="your-username"
export RDS_PASSWORD="your-password"
export RDS_DB="your-database-name"
export RDS_PORT="3306"
```
### DocumentDB env variables 

To import into DocmunetDB you need to have the following credentials stored on your EC2 
```bash
MONGO_URL = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
MONGO_USERNAME = os.getenv('MONGO_USERNAME', 'default-user')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'default_password')
MONGO_TLS = os.getenv('MONGO_TLS', 'global-bundle.pem')
```
### Neptune env variables 

To import into Neptune you need to have the following credentials stored on your EC2 
```bash
NEP_ENDPOINT = os.getenv('NEP_ENDPOINT', 'db-neptune-1.cluster-cfsssmgsia9l.us-east-1.neptune.amazonaws.com')
IAM_ROLE_ARN = os.getenv('IAM_ROLE_ARN', 'arn:aws:iam::123456789012:role/NeptuneAccessDev')
IMPORT_BUCKET = os.getenv('IMPORT_BUCKET', 'default-bucket-name')

```

### Data Location

Currently data can be imported from an S3 bucket or from the local EC2 instance. To transfer a file from your machine to the EC2 use the following command:

```bash
rsync -avz --exclude '.venv' -e "ssh -i ~/.ssh/<your pem name>.pem" <path to your code> ec2-user@<ec2 ip>:/home/ec2-user/
```
## Example Workflow

To demonstrate how to use AWS-DataBridge, here’s an example of importing a JSON file into an RDS instance:

### Step 1: Prepare Your Data File

Ensure your data file (e.g., `data.json`) is either stored locally on your EC2 instance or in an S3 bucket. If it's not on your EC2 instance, you can transfer it using the command listed above in the Data Location section.

### Step 2: Run the Application

Use the command provided above to run the program.

### Step 3: Follow the Prompts

The CLI will guide you through the steps, including specifying the table name and confirming the import. **Be cautious of typos**, as they may cause errors in the import process. AWS-DataBridge will convert the JSON file to the necessary format (if needed) and import the data to your RDS instance.

> **Note**: 
> - When importing into **RDS**, **DynamoDB**, and **DocumentDB**, the file will be converted into a CSV format.
> - For **Neptune**, the file will be converted to JSON if it isn't already in that format.


## Compatibility

This code has been tested and verified to work on the AWS Linux 2023 AMI EC2. Compatibility with other environments or operating systems is not guaranteed.

## Contributing

If you would like to Contribute:

1. Fork the repository
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit (git commit -m 'Add new feature').
4. Push your changes (git push origin feature-branch).
5. Open a pull request.

Also feel free to open an issue if you spot any problems with the program!

## License

This project is licensed under the MIT License.
