import sqlite3
import json
import os
import sqlite3,os
import re
def get_abs_dir():
    return os.path.dirname(os.path.abspath(__name__))
def get_dbPath():
    return os.path.join(get_abs_dir(),'output.db')
# Load the JSON data
def load_json_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# Connect to the SQLite database
def connect_to_db(db_path):
    conn = sqlite3.connect(db_path)
    return conn

# Update database records to set state as California based on city or zip code
def update_records(conn, cities, zip_codes):
    cursor = conn.cursor()
    try:
        # Update based on city
        query = "UPDATE address_points_from_national_address_database SET state = 'CA' WHERE post_city IN ({})".format(','.join('?'*len(cities)))
        cursor.execute(query, cities)

        # Update based on zip code
        query = "UPDATE address_points_from_national_address_database SET state = 'CA' WHERE zip_code IN ({})".format(','.join('?'*len(zip_codes)))
        cursor.execute(query, zip_codes)
        
        conn.commit()
        print("Database updated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

def main():
    db_path = get_dbPath()  # Assuming get_dbPath() fetches the path to your database
    json_path = 'county_vars.json'  # Adjust the path to where you have stored the JSON file
    data = load_json_data(json_path)
    
    # Extract all cities and zip codes from the JSON data
    cities = set()
    zip_codes = set()
    for county, details in data.items():
        cities.update(details['cities'])
        zip_codes.update(details['zipCodes'])
    
    # Convert sets to lists for database operations
    cities = list(cities)
    zip_codes = list(zip_codes)
    
    # Connect to the database and update records
    conn = connect_to_db(db_path)
    if conn:
        update_records(conn, cities, zip_codes)
        conn.close()

if __name__ == "__main__":
    main()
