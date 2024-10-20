from california_municipalities import *
from abstract_utilities import *
class get_from_list_manager:
  def __init__(self):
    self.track_list = [None]
  def track_it(self,obj,obj2):
    self.track_list.append(obj)
    return obj2
  def get_from_last(self):
    return_it = self.track_list[-1]
    if return_it != None:
      self.track_list.append(None)
    return return_it
listMgr = get_from_list_manager()
def if_single_ls(list_obj):
  list_obj_ls = make_list(list_obj)
  if list_obj and len(list_obj_ls)==1:
    list_obj=list_obj_ls[0]
  return list_obj
def normalize_comparison(obj,obj2):
  obj=str(obj).lower()
  obj2 = make_list(obj2)  
  obj2_lowered = [listMgr.track_it(ob2, str(ob2).lower()) if str(ob2).lower() == obj else str(ob2).lower() for ob2 in obj2]
  last_find = listMgr.get_from_last()
  if last_find:
    input(last_find)
    return last_find
  for i,obj2_lower in enumerate(obj2_lowered):
    obj2_lower_spl = obj2_lower.split(' ')
    for j,ob in enumerate(obj.split(' ')):
      if ob in obj2_lower_spl:
        obj2_lower_spl = obj2_lower_spl.remove(ob)
    try:
      if obj2_lower_spl and len(obj2_lower_spl) == 0 or ''.join(make_list(obj2_lower_spl)) in ["county","city"]:
        return obj2[i]
    except:
      input(input(obj2_lower_spl))
def get_all_keys(typ):
  return {"zipcode":"all_zips","county":"all_counties","city":"all_cities"}.get(typ)
def get_places_js(zipcode=None,state=None,county=None,city=None):
  return {"city":city,"county":county,"state":state or "ca","zipcode":zipcode}
def get_new_js(key):
  return {"cities":"city","counties":"county","zipCodes":"zipcode","state":"state"}.get(key,key)
def is_none_in_js(obj):
  if obj and isinstance(obj,dict):
    obj = list(obj.values())
  if isinstance(obj,list) and None in obj:
    return True
def get_zipcode_info(zipcode):
  return all_state_data["all_zips"].get(str(zipcode))
def get_cities_info(city):
  return all_state_data["all_"].get(str(city))
def get_counties_info(county):
  return all_state_data["all_counties"].get(str(county))
def get_from_zipcode(zipcode=None,state=None,county=None,city=None):
  places_js = get_places_js(zipcode=zipcode,state=state,county=county,city=city)
  return_js = places_js
  for key,value in get_places_js(zipcode=zipcode,state=state,county=county,city=city).items():
    get_key = get_all_keys(key)
    info_js  = all_state_data.get(str(get_key))
    if info_js:
      for info_key,info_value in info_js.items():
        norm_comp = normalize_comparison(value,info_key)        
        if norm_comp:
          for value_key,value_value in info_js[norm_comp].items():
            return_js[get_new_js(value_key)] = if_single_ls(return_js[get_new_js(value_key)] or value_value)  
  return return_js
