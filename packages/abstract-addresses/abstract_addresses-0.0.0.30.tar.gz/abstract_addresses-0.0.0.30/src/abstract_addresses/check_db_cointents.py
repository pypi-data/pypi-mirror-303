import sqlite3
import pandas as pd

def fetch_all_tables_and_contents(db_path):
    """
    Connect to the SQLite database, fetch all tables, and print their contents.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    all_data = {}
    for table in tables:
        table_name = table[0]
        print(f"\nTable: {table_name}")
        
        # Fetch all records from the table
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        
        # Get column names
        column_names = [description[0] for description in cursor.description]
        
        # Create DataFrame for better display
        df = pd.DataFrame(records, columns=column_names)
        
        # Print column names and records
        print(df)
        
        all_data[table_name] = {
            "columns": column_names,
            "records": records
        }
    
    # Close the connection
    conn.close()
    return all_data

# Path to the database file
db_path = 'us_addresses.db'  # Ensure this path points to the downloaded addresses.db file

# Fetch and display the contents of the database
fetch_all_tables_and_contents(db_path)
