# functions to return specific data as per request

import json


def return_retail():
    json_data = open("./data/data.json")
    data = json.load(json_data)
    retail = data["retail-data"]
    json_data.close()
    return retail


def return_cot():
    json_data = open("./data/data.json")
    data = json.load(json_data)
    cot = data["cot-data"]
    json_data.close()
    return cot


def return_fundamental():
    json_data = open("./data/data.json")
    data = json.load(json_data)
    fundamental = data["fundamental-data"]
    json_data.close()
    return fundamental

def return_technical():
    json_data = open("./data/data.json")
    data = json.load(json_data)
    technical = data["technical-data"]
    json_data.close()
    return technical

def return_seasonality():
    json_data = open("./data/data.json")
    data = json.load(json_data)
    seasonality = data["seasonality-data"]
    json_data.close()
    return seasonality

