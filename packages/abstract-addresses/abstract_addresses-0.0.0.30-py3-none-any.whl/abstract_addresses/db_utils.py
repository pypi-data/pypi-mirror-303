import os,sqlite3
from .pre_parse import *
from abstract_utilities import *
import uuid
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
def get_this_path():
  return os.path.abspath(__file__)
def get_abs_dir():
  return os.path.dirname(get_this_path())
class db_path_mgr(metaclass=SingletonMeta):
    def __init__(self,db_dir=None,db_file=None,dbType=None):
        self.db_dir = db_dir or get_dbs_dir()
        self.db_path = os.path.join(self.db_dir,db_file) if db_file else self.get_db_path(dbType)
    def get_db_path(self,dbType=None):
        db_js = {"master_addresses":"master_addresses.db"}
        return os.path.join(self.get_dbs_dir(),db_js.get(dbType or 'master_addresses',list(db_js.values())[0]))
    def get_dbs_dir(self):
      return self.db_dir

def generate_uuid():
    return uuid.uuid4()
def get_types():
    types="""Column: objectid, Type: INTEGER
Column: shape, Type: BLOB
Column: addno_full, Type: VARCHAR(100)
Column: st_premod, Type: VARCHAR(15)
Column: st_predir, Type: VARCHAR(10)
Column: st_pretyp, Type: VARCHAR(50)
Column: st_presep, Type: VARCHAR(20)
Column: st_name, Type: VARCHAR(60)
Column: st_postyp, Type: VARCHAR(50)
Column: st_posdir, Type: VARCHAR(10)
Column: st_posmod, Type: VARCHAR(25)
Column: stnam_full, Type: VARCHAR(255)
Column: seat, Type: VARCHAR(75)
Column: subaddress, Type: VARCHAR(255)
Column: post_city, Type: VARCHAR(40)
Column: census_plc, Type: VARCHAR(100)
Column: natamarea, Type: VARCHAR(100)
Column: natamsub, Type: VARCHAR(100)
Column: urbnztn_pr, Type: VARCHAR(100)
Column: placeother, Type: VARCHAR(100)
Column: placenmtyp, Type: VARCHAR(50)
Column: uuid, Type: VARCHAR
Column: addrrefsys, Type: VARCHAR(75)
Column: natgrid, Type: VARCHAR(50)
Column: elevation, Type: INTEGER_INT16
Column: addrpoint, Type: VARCHAR(50)
Column: related_id, Type: VARCHAR(50)
Column: relatetype, Type: VARCHAR(50)
Column: parcelsrc, Type: VARCHAR(50)
Column: parcel_id, Type: VARCHAR(50)
Column: addrclass, Type: VARCHAR(50)
Column: lifecycle, Type: VARCHAR(50)
Column: expire, Type: TIMESTAMP
Column: dateupdate, Type: TIMESTAMP
Column: anomstatus, Type: VARCHAR(50)
Column: locatndesc, Type: VARCHAR(75)
Column: delivertyp, Type: VARCHAR(50)
Column: nad_source, Type: VARCHAR(75)
Column: dataset_id, Type: VARCHAR(75)
Column: addnum_pre, Type: VARCHAR(15)
Column: add_number, Type: INTEGER
Column: addnum_suf, Type: VARCHAR(15)
Column: building, Type: VARCHAR(75)
Column: floor, Type: VARCHAR(75)
Column: unit, Type: VARCHAR(75)
Column: room, Type: VARCHAR(75)
Column: addtl_loc, Type: VARCHAR(225)
Column: landmkname, Type: VARCHAR(150)
Column: county, Type: VARCHAR(40)
Column: inc_muni, Type: VARCHAR(100)
Column: uninc_comm, Type: VARCHAR(100)
Column: nbrhd_comm, Type: VARCHAR(100)
Column: state, Type: VARCHAR(2)
Column: zip_code, Type: VARCHAR(7)
Column: plus_4, Type: VARCHAR(4)
Column: addauth, Type: VARCHAR(75)
Column: longitude, Type: FLOAT
Column: latitude, Type: FLOAT
Column: placement, Type: VARCHAR(25)
Column: effective, Type: TIMESTAMP
Column: addr_type, Type: VARCHAR(50)"""
    types = types.split('\n')
    return {str(typ).split('Column: ')[1].split(',')[0]:str(typ).split('Type: ')[-1] for typ in types}
def display_results(cursor, results):
    """Display the search results in a user-friendly format."""
    column_names = get_table_columns(cursor, 'address_points_from_national_address_database')
    for row in results:
        row_dict = dict(zip(column_names, row))
        print(row_dict)
def display_table_data(cursor, table_name):
    """Display column headers and first 10 data rows from a specific table."""
    print(f"\nContents of table: {table_name}")
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 100")  # Limits to 10 rows for brevity
    columns = [description[0] for description in cursor.description]
    print("Columns:", columns)
    rows = cursor.fetchall()
    input(len(rows))
    for row in rows:
        print(row)
def if_types(types_js,obj,key):
    if obj in ["",None]:
        return None
    typ = str(types_js[key]).lower()
    if is_number(obj) and typ in ['float','integer']:
        if typ == "float":
            return float(obj)
        if typ == 'integer':
            return int(obj)
    return obj
def get_default_layer():
    return 'address_points_from_national_address_database'
def get_source_data_dir():
  return os.path.join(get_abs_dir(),'source_data')
def get_county_vars_path():
    return os.path.join(get_source_data_dir(),'county_vars.json')
# Load the JSON data
def get_county_vars_data():
    county_vars_path = get_county_vars_path()
    data = safe_load_from_file(county_vars_path)
    return data
def connect_to_db(db_path=None,dbType=None):
  try:
      if db_path==None:
          db_mgr = db_path_mgr()
          db_path = db_mgr.get_db_path(dbType=dbType)
      return sqlite3.connect(db_path)
  except sqlite3.Error as e:
      print(f"Error connecting to database: {e}")
      return None
def get_cursor(conn=None,db_path=None,dbType=None):
  if conn == None:
    conn = connect_to_db(db_path=db_path,dbType=dbType)
  return conn.cursor()
def create_table(cursor=None,conn=None,types_dict=None,db_path=None,dbType=None):
    cursor = cursor or get_cursor(conn=conn,db_path=db_path,dbType=dbType)
    types_dict=types_dict or get_types()
    """ Create a SQL table using types from types_dict """
    sql_create = "CREATE TABLE IF NOT EXISTS addresses ("
    sql_create += ', '.join([f"{col_name} {data_type}" for col_name, data_type in types_dict.items()])
    sql_create += ")"
    cursor.execute(sql_create.replace(',,',','))
    return cursor
def insert_key_values(db_insert_js,cursor=None,conn=None,db_path=None,dbType=None,types_dict=None):
    conn = conn or connect_to_db(db_path=db_path,dbType=dbType)
    types_dict=types_dict or get_types()
    cursor = cursor or create_table(cursor=cursor,conn=conn,types_dict=types_dict,db_path=db_path,dbType=dbType)
    question_set=[]
    value_set = []
    key_set = ""
    for key,value in db_insert_js.items():
        input(db_insert_js)
        question_set.append('?')
        key_set += f"{key},"
        if key == 'uuid' and str(value).lower() in ['',[],'nan','none']:
            value = generate_uuid()
        value_set.append(if_types(types_dict,value,key) or None)
    key_set = eatAll(key_set, [',','','\n','\t'])
    question_set = ','.join(question_set)
    cursor.execute(f'INSERT INTO addresses ({key_set}) VALUES ({question_set})', tuple(value_set))
    conn.commit()
    conn.close()
# Update database records to set state as California based on city or zip code
def change_records(conn, layer,column,value,search_column,search_values):
    cursor = conn.cursor()
    try:
        # Update based on city
        query = "UPDATE {layer} SET {column} = {value} WHERE {search_column} IN ({})".format(','.join('?'*len(search_values)))
        cursor.execute(query, cities)
        conn.commit()
        print("Database updated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
def list_tables(cursor):
    """List all tables in the database."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])
    return tables
def get_table_columns(cursor, table_name):
    """Retrieve and print column names for a specific table."""
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    print("Columns in the table:", table_name)
    column_names = [column[1] for column in columns]
    return column_names
def normalize_value(value):
    """Normalize the value for comparison."""
    if value is not None:
        value = value.lower()  # Convert to lowercase
        value = re.sub(r'[^a-z0-9]', '', value)  # Remove non-alphanumeric characters
    return value
def fetch_all(cursor, columns, values, strict=True):
    """Search the database for a specific step in the search hierarchy."""
    if not isinstance(columns, list) or not isinstance(values, list) or len(columns) != len(values):
        raise ValueError("Columns and values must be lists of the same length.")
    
    query = "SELECT DISTINCT * FROM address_points_from_national_address_database WHERE 1=1"
    params = []
    for column, value in zip(columns, values):
        if value is not None:
            normalized_value = normalize_value(value)
            query += f" AND REPLACE(LOWER({column}), ' ', '') LIKE ?"
            params.append(f"%{normalized_value}%")
    
    print(f"Executing query: {query}")
    print(f"With parameters: {params}")
    cursor.execute(query, params)
    results = cursor.fetchall()
    return results
def perform_search(cursor, **kwargs):
    """Perform the hierarchical search and relay the results."""
    # Step 1: Search by state
    state = kwargs.get('state')
    if not state:
        print("State is required to perform the search.")
        return
    
    states = fetch_all(cursor, ['state'], [state])
    if not states:
        print("Unable to fulfill query: state")
        return
    # Step 2: Search by post_city or zip_code
    post_city = kwargs.get('post_city')
    zip_code = kwargs.get('zip_code')

    if post_city:
        cities = fetch_all(cursor, ['post_city'], [post_city])
        if not cities:
            print("Unable to fulfill query: post_city")
            return
    if zip_code:
        zips = fetch_all(cursor, ['zip_code'], [zip_code])
        if not zips:
            print("Unable to fulfill query: zip_code")
            return
    else:
        print("Either post_city or zip_code is required to perform the search.")
        return

    # Step 3: Search by detailed address parameters
    address_params = {k: v for k, v in kwargs.items() if k not in ['state', 'post_city', 'zip_code']}
    for key,value in address_params.items():
        results = fetch_all(cursor, [key], [value], strict=False)
    else:
        results = states if post_city else zips
    
    if not results:
        print("No matching results found.")
    else:
        print("Search successful. Results:")
        display_results(cursor, results)

    return results
def search_query(address_dict,layer=None,conn=None,cursor=None,db_path=None,dbType=None):
    conn = conn or connect_to_db(db_path=db_path,dbType=dbType)
    cursor=cursor or get_cursor(conn=conn,db_path=db_path,dbType=dbType)
    if cursor:
        # List columns in the specific table
        columns = get_table_columns(cursor, layer or get_default_layer())
        results = perform_search(cursor, **address_dict)
        conn.close()
        return results
    conn.close()
