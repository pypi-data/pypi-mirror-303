from abstract_utilities import *
from california_municipalities import county_vars 
import os,usaddress
def get_abs_path():
    """ Get the absolute path of the directory containing this script. """
    return os.path.dirname(os.path.abspath(__file__))

def get_county_vars_path():
    """ Return the complete path to the county_vars.json file. """
    return os.path.join(get_abs_path(), "county_vars.json")

def get_county_vars_data():
    """ Read and return the JSON data from county_vars.json file. """
    #county_vars_path = get_county_vars_path()
    return county_vars#safe_read_from_json(county_vars_path)

def normalize_compare(string,list_obj,queryOption=False):
  list_obj = make_list(list_obj)
  list_obj_lowered = [str(obj).lower() for obj in make_list(list_obj)]
  string = str(string).lower()
  for i,obj in enumerate(list_obj):
    if string == obj:
      return list_obj[i]
  if queryOption:
    for i,obj in enumerate(list_obj):
      if string in obj:
        return list_obj[i]
def get_city_zip(city=None, zipcode=None, county=None):
    """ Retrieve city and ZIP code data based on input parameters. """
    vars_js = {"county": county, "city": city, "zipcode": zipcode}
    county_vars = get_county_vars_data()
    if county:
        county_data = county_vars.get(county, {})
        if city:
            city_match = get_normalized_compare(city, county_data.get("cities", []))
            if city_match:
                vars_js["city"] = city_match
                city_zips = county_data.get("city_zip", {}).get(city_match, [])
                if zipcode and str(zipcode) in city_zips:
                    vars_js["zipcode"] = zipcode
        if zipcode:
            for city, zips in county_data.get("city_zip", {}).items():
                if str(zipcode) in zips:
                    vars_js["city"] = city
                    break
    return vars_js
def determine_if_zip_code(obj,addr_js={}):
  obj = str(obj).split('-')[0]
  if is_number(obj) and len(obj)==5:
    county_vars = get_county_vars_data()
    for county,values in county_vars.items():
      if obj in values['zipCodes']:
        addr_js['zipcode']=obj
        addr_js['county']=obj
def format_address(address):
  pieces = address.split(' ')
  for piece in pieces:
    piece = eatAll(piece,['',' ','\n',','])
    piece = ''
    if piece:
      pass
        
def parse_address(input_address):
    state_data = get_county_vars_data()
    # Parsing the address using usaddress or similar library
    try:
        address_parts = usaddress.tag(input_address)
        address_dict = address_parts[0]  # Extracting the address components
    except Exception as e:
        print(f"Error parsing address: {e}")
        return {}
    address_dict=dict(address_dict)
    # Extract base information
    street_number = address_dict.get('AddressNumber', '')
    street_name = address_dict.get('StreetName', '')
    city = address_dict.get('PlaceName', '')
    # Find matching city and zip
    for county, info in state_data.items():
        if city in info["cities"]:
            city_zip_codes = info["city_zip"].get(city, [])
            if city_zip_codes:
                zip_code = city_zip_codes[0]  # Taking the first zip code as default, refine if needed
                address_dict['PlaceName']=city
                address_dict['ZipCode']=zip_code
                break
    
    #keys_js = {"StreetNamePreDirectional":"st_predir",'StreetNamePostType':'st_postyp','AddressNumber':'addno_full','StreetName':'st_name','PlaceName':'post_city','StateName':'state','ZipCode':'zip_code'}
    #address_dict_rev = {}
    #for key,value in address_dict.items():
    #    if key not in 'Recipient':
    #        address_dict_rev[keys_js[key]]=value
    return address_dict
