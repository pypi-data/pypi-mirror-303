
# requirements_dev.txt we use for the testing
It makes it easier to install and manage dependencies for development and testing, separate from the dependencies required for production.

# difference between requirements_dev.txt and requirements.txt

requirements.txt is used to specify the dependencies required to run the production code of a Python project, while requirements_dev.txt is used to specify the dependencies required for development and testing purposes.

# tox.ini
We use if for the testing in the python package testing against different version of the python 

## how tox works tox enviornment creation
1. Install depedencies and packages 
2. Run commands
3. Its a combination of the (virtualenvwrapper and makefile)
4. It creates a .tox


# pyproject.toml
it is being used for configuration the python project it is a alternative of the setup.cfg file. its contains configuration related to the build system
such as the build tool used package name version author license and dependencies

# setup.cfg
In summary, setup.cfg is used by setup tools to configure the packaging and installation of a Python project

# Testing python application
*types of testing*
1. Automated testing 
2. Manual testing

*Mode of testing*
1. Unit testing
2. Integration tests

*Testing frameworks*

1. pytest
2. unittest
3. robotframework
4. selenium
5. behave
6. doctest

# check with the code style formatting and syntax(coding standard)

1. pylint
2. flake8(it is best because it containt 3 library pylint pycodestyle mccabe)
3. pycodestyle


# How to use the package :-

### STEPS:-

```bash
pip install mysql-crud-automation
```

```bash
import mysql.connector
```

```bash
host="hostname",
user="username",
password="<password>",
```

```bash
mysql_connector = mysql_operation(host,user,password)
```

# CRUD Operation on MySQL :-

## How to run :-

### 1. create database
```bash
mysql_connector.create_database()
```

### 2. create table
```bash
mysql_connector.create_table('<table_name>')
```

### 3. insert record 
```bash
mysql_connector.insert_record(table_name="<table_name>", record=record:dict)
```

### 4. insert many record 
```bash
mysql_connector.insert_record(table_name="<table_name>",record=[record:dict])
```

### 5. bulk insert record 
- in this datafile is in .csv or .xlsx file 
```bash
mysql_connector.bulk_insert ( datafile= "<file_path>", table_name="<table_name>", unique_field: str = None)
```

### 6. find query  
```bash
mysql_connector.find(query: dict = {}, table_name="<table_name>")
```

### 7. update query
```bash
mysql_connector.update(query: dict, table_name="<table_name>", new_values: dict)
```

### 8. delete query
```bash
mysql_connector.delete(query: dict, table_name="<table_name>")
```
