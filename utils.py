import time
import json
import config
from scrapper import *
import concurrent.futures
    
    
# update data in data.json if expired 
def collect_data():
    json_data = open("data.json")
    data = json.load(json_data)
    old_timestamp = data["timestamp"] 
    new_timestamp = round(time.time())
    json_data.close()
    # print(f"Last update JSON: {old_timestamp}")
    # print(f"Time right now: {new_timestamp}")
    if update_required(old_timestamp, new_timestamp):
            
        # print("Data is outdated. Collecting new Data...")
        data["timestamp"] = new_timestamp

        # collect and store fundamental data
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for i in fundamental_urls:
                executor.submit(get_fundamental_data, i)
        data["fundamental-data"] = fundamental_data
        
        # collect and store cot data
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for j in cot_currency_codes:
                executor.submit(get_cot_data, j)
        data["cot-data"] = cot_data

        # collect and store retail data
        get_retail_data()
        data["retail-data"] = retail_data
        
            # update data in data.json
        with open("data.json", "w") as outfile:
            json.dump(data, outfile)

        outfile.close()
    else:
        # print("Data is fresh")
        return data


def update_required(old_timestamp, new_timestamp):
    diff_min  = (new_timestamp - old_timestamp) / 60
    # print(f"Time time difference is: {round(diff_min)} Minutes")
    return True if diff_min > config.DATA_EXPIRATION_MINUTES else False


def return_retail():
    json_data = open("data.json")
    data = json.load(json_data)
    retail = data["retail-data"]
    json_data.close()
    return retail


def return_cot():
    json_data = open("data.json")
    data = json.load(json_data)
    cot = data["cot-data"]
    json_data.close()
    return cot


def return_fundamental():
    json_data = open("data.json")
    data = json.load(json_data)
    fundamental = data["fundamental-data"]
    json_data.close()
    return fundamental
