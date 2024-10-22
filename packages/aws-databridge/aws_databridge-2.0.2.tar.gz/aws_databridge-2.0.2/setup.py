from setuptools import setup, find_packages

setup(
    name="aws-databridge",
    version="2.0.2",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
       "boto3>=1.20.0",  
        "pandas",
        "pymysql",
        "lxml"
    ],
    entry_points={
        "console_scripts": [
           "aws-databridge=aws_databridge.main:main",
        ]
    },
    author="Jay, Aban, Matt",
    description="An AWS EC2 CLI application that supports XML, TXT, JSON, and CSV imports to various AWS databases.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jaysalgado/aws-databridge",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
