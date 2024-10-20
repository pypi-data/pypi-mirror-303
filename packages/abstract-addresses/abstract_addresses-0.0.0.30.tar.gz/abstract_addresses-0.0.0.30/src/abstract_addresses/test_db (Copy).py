import sqlite3

def usaddress_key_values():
    return {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "AddressNumber": "TEXT",
        "StreetNamePreDirectional": "TEXT",
        "StreetName": "TEXT",
        "StreetNamePostType": "TEXT",
        "OccupancyType": "TEXT",
        "OccupancyIdentifier": "TEXT",
        "PlaceName": "TEXT",
        "StateName": "TEXT",
        "ZipCode": "TEXT",
        "Recipient": "TEXT",
        "NotAddress": "TEXT",
        "raw_address": "TEXT NOT NULL",
        "standardized_address": "TEXT",
        "dwelling": "TEXT",
        "solar": "BOOL",
        "battery": "BOOL"
    }

def create_table(cursor):
    columns = usaddress_key_values()
    columns_def = ", ".join([f"{k} {v}" for k, v in columns.items()])
    create_table_sql = f"CREATE TABLE IF NOT EXISTS addresses ({columns_def})"
    cursor.execute(create_table_sql)

def address_exists(cursor, raw_address):
    check_sql = "SELECT COUNT(1) FROM addresses WHERE raw_address = ?"
    cursor.execute(check_sql, (raw_address,))
    return cursor.fetchone()[0] > 0

def add_address(cursor, address_data):
    if address_exists(cursor, address_data["raw_address"]):
        print("Address already exists in the database.")
        return
    columns = usaddress_key_values()
    columns_names = ", ".join(columns.keys())
    placeholders = ", ".join(["?" for _ in columns.keys()])
    insert_sql = f"INSERT INTO addresses ({columns_names}) VALUES ({placeholders})"
    cursor.execute(insert_sql, list(address_data.values()))

def update_address(cursor, raw_address, dwelling=None, solar=None, battery=None):
    updates = []
    values = []
    if dwelling is not None:
        updates.append("dwelling = ?")
        values.append(dwelling)
    if solar is not None:
        updates.append("solar = ?")
        values.append(solar)
    if battery is not None:
        updates.append("battery = ?")
        values.append(battery)
    
    if updates:
        update_sql = f"UPDATE addresses SET {', '.join(updates)} WHERE raw_address = ?"
        values.append(raw_address)
        cursor.execute(update_sql, values)
        print("Address updated successfully.")
    else:
        print("No fields to update.")

def view_addresses(cursor):
    cursor.execute("SELECT * FROM addresses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('us_addresses.db')
    cursor = conn.cursor()

    ## Create the table
    #create_table(cursor)
    
    # Example address data
    address_data = {
        "id": None,
        "AddressNumber": "1234",
        "StreetNamePreDirectional": "N",
        "StreetName": "Main",
        "StreetNamePostType": "St",
        "OccupancyType": "Apt",
        "OccupancyIdentifier": "4C",
        "PlaceName": "Springfield",
        "StateName": "IL",
        "ZipCode": "62704",
        "Recipient": "John Doe",
        "NotAddress": None,
        "raw_address": "123 N Main St Apt 4B, Springfield, IL 62704",
        "standardized_address": "123 N Main St Apt 4B, Springfield, IL 62704",
        "dwelling": "Apartment",
        "solar": False,
        "battery": False
    }
    
    # Add address to the database
    add_address(cursor, address_data)
    
    # Update address information
    update_address(cursor, "123 N Main St Apt 4B, Springfield, IL 62704", dwelling="apartnment", solar=True, battery=True)
    
    # Commit the changes
    conn.commit()
    
    # View the addresses in the database
    view_addresses(cursor)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
