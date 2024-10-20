from .db_utils import *
from abstract_pandas import *
import shutil,os
def get_this_path():
  return os.path.abspath(__file__)
def get_abs_dir():
  return os.path.dirname(get_this_path())
def get_from_designation_desc(designation_desc):
  dwelling = [dwelling for dwelling in ['single','multi'] if dwelling in designation_desc]
  if dwelling == []:
    return None
  dwelling_type = [dwelling_type for dwelling_type in ['unit','family'] if dwelling_type in designation_desc]
  if dwelling and dwelling_type:
    return dwelling

def find_designation(designation_header,row):
  if str(row.get('addr2')) not in ['','nan','none']:
    return 'multi'
  designation_desc = row.get(designation_header)
  if designation_desc:
    dwelling = get_from_designation_desc(designation_desc)
    if dwelling:
      return dwelling
  for itter in row.values():
    dwelling = get_from_designation_desc(itter)
    if dwelling:
      return dwelling
  return 'unknown'
def get_normal_address_string(row):
    return f"{row['addr1']} {row['city']} {row['state']} {row['zip']}"
def get_unique_address_string(row,headers):
  return ' '.join([str(row.get(header)) for header in headers if row.get(header)])
def update_address_from_excel(file_path,headers=[],designations='unknown',designation_header=None,dbType=None,db_path=None):
  baseName = os.path.basename(file_path)
  source_file = os.path.join(get_source_data_dir(),baseName)
  if os.path.isfile(source_file):
    return
  conn = connect_to_db(db_path=db_path,dbType=dbType)
  df = get_df(file_path)
  headers = headers or 'normal'
  for index,row in df.iterrows():
    if headers == 'normal':
      address_str = get_normal_address_string(row)
    else:
      address_str = get_unique_address_string(row,headers)
    address_dict = parse_address(address_str)
    dwelling_type = find_designation(designation_header,row)
    results = search_query(address_dict)
    if results and dwelling_type not in results:
      change_records(conn, layer,"building",dwelling_type,'uuid',results['uuid'])
    else:
      address_dict['building']=dwelling_type
      insert_key_values(address_dict,cursor=conn.cursor,conn=conn,db_path=db_path,dbType=dbType)
  shutil.copy(file_path,source_file)
  
