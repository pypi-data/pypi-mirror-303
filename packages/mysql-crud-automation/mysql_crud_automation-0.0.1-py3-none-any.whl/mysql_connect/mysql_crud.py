import mysql.connector
from mysql.connector import Error
import pandas as pd
import json
from typing import Any
from ensure import ensure_annotations
from typing import Optional


class mysql_operation:
    @ensure_annotations 
    def __init__(self, host: str, user: str, password: str, database_name: str):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name
    
    @ensure_annotations 
    def create_connection(self):
        """Create a MySQL connection."""
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database_name
            )
            if connection.is_connected():
                print("Connected to MySQL database")
            return connection
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    @ensure_annotations 
    def create_database(self):
        """Create a MySQL database if it doesn't exist."""
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        cursor = connection.cursor()
        try:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database_name}")
            print(f"Database '{self.database_name}' created or already exists.")
            return self.database_name
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
            connection.close()

    @ensure_annotations 
    def create_table(self, create_table_sql: str):
        """Create a table in the MySQL database using a SQL query."""
        connection = self.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(create_table_sql)
            print("Table created successfully.")
            return True
        except Error as e:
            print(f"Error creating table: {e}")
            return None 
        finally:
            cursor.close()
            connection.close()
            
    @ensure_annotations 
    def insert_record(self, record: dict, table_name: Optional[str] = None):
        """Insert one or many records into the specified MySQL table."""
        connection = self.create_connection()
        cursor = connection.cursor()

        if isinstance(record, list):
            # Ensure all items in the list are dictionaries
            for data in record:
                if not isinstance(data, dict):
                    raise TypeError("Each record in the list must be a dictionary")

            # Prepare SQL for inserting multiple records
            columns = ', '.join(record[0].keys())
            placeholders = ', '.join(['%s'] * len(record[0]))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            # Extract the values for each record as tuples
            values = [tuple(data.values()) for data in record]
            cursor.executemany(sql, values)
            
        elif isinstance(record, dict):
            # Prepare SQL for inserting a single record
            columns = ', '.join(record.keys())
            placeholders = ', '.join(['%s'] * len(record))
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

            # Extract the values as a tuple
            values = tuple(record.values())
            cursor.execute(sql, values)
        else:
            raise TypeError("Record must be a dictionary or a list of dictionaries")

        # Commit the transaction
        connection.commit()
        print(f"Record(s) inserted into {table_name}.")
        
        cursor.close()
        connection.close()

    @ensure_annotations 
    def bulk_insert(self, datafile: str, table_name: Optional[str] = None, unique_field: Optional[str] = None):
        """Bulk insert records from a CSV or Excel file."""
        connection = self.create_connection()
        cursor = connection.cursor()

        if datafile.endswith('.csv'):
            data = pd.read_csv(datafile)
        elif datafile.endswith('.xlsx'):
            data = pd.read_excel(datafile)
        
        data_json = json.loads(data.to_json(orient='records'))

        for record in data_json:
            columns = ', '.join(record.keys())
            placeholders = ', '.join(['%s'] * len(record))
            if unique_field:
                select_query = f"SELECT COUNT(*) FROM {table_name} WHERE {unique_field} = %s"
                cursor.execute(select_query, (record[unique_field],))
                result = cursor.fetchone()
                if result[0] == 0:
                    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                    cursor.execute(sql, tuple(record.values()))
                else:
                    print(f"Record with {unique_field}={record[unique_field]} already exists. Skipping insertion.")
            else:
                sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(sql, tuple(record.values()))
        
        connection.commit()
        print("Bulk insert completed.")
        cursor.close()
        connection.close()

    @ensure_annotations 
    def find(self, query: dict = {}, table_name: Optional[str] = None):
        """Retrieve records from the specified MySQL table based on the query."""
        connection = self.create_connection()
        cursor = connection.cursor(dictionary=True)  # This will return results as dictionaries

        # If no query is specified, fetch all records
        if not query:
            sql = f"SELECT * FROM {table_name}"
            cursor.execute(sql)
        else:
            # Construct the WHERE clause based on the query dictionary
            conditions = ' AND '.join([f"{key} = %s" for key in query.keys()])
            sql = f"SELECT * FROM {table_name} WHERE {conditions}"
            cursor.execute(sql, tuple(query.values()))

        # Fetch all the results
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results

    @ensure_annotations 
    def update(self, query: dict, new_values: dict,table_name: Optional[str] = None):
        """Update records in the MySQL table based on the query and new values."""
        connection = self.create_connection()
        cursor = connection.cursor()

        try:
            # Construct the SET clause from the new_values dictionary
            set_clause = ', '.join([f"{key} = %s" for key in new_values.keys()])

            # Construct the WHERE clause from the query dictionary
            where_clause = ' AND '.join([f"{key} = %s" for key in query.keys()])

            # Prepare the SQL UPDATE statement
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"

            # Combine the values for SET and WHERE clauses
            values = tuple(new_values.values()) + tuple(query.values())

            # Execute the SQL statement
            cursor.execute(sql, values)
            connection.commit()

            print(f"Record(s) updated in {table_name} where {query}.")
            
        except Error as e:  # Make sure to replace `Error` with the relevant exception class
            print(f"Error updating record: {e}")
        
        finally:
            cursor.close()
            connection.close()


    @ensure_annotations 
    def delete(self, query: dict,table_name: Optional[str] = None):
        """Delete records from the MySQL table based on the query."""
        connection = self.create_connection()
        cursor = connection.cursor()

        try:
            # Construct the WHERE clause from the query dictionary
            where_clause = ' AND '.join([f"{key} = %s" for key in query.keys()])

            # Prepare the DELETE statement
            sql = f"DELETE FROM {table_name} WHERE {where_clause}"

            # Combine the values for the WHERE clause
            values = tuple(query.values())

            # Execute the SQL statement
            cursor.execute(sql, values)
            connection.commit()

            print(f"Record(s) deleted from {table_name} where {query}.")
        
        except Error as e:  # Use the appropriate MySQL error handling class
            print(f"Error deleting record: {e}")
        
        finally:
            cursor.close()
            connection.close()