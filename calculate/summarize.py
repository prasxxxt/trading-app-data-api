import json
import datetime
from calculate.scoring import *

today = datetime.date.today()

currency_map = {
    "EUR": "euro-area",
    "GBP": "united-kingdom",
    "AUD": "australia",
    "NZD": "new-zealand",
    "USD": "united-states",
    "CAD": "canada",
    "CHF": "switzerland",
    "JPY": "japan",
}


def get_summary(pair):

    base = pair[:3]
    quote = pair[3:]
    json_data = open("./data/data.json")
    data = json.load(json_data)

    fundamental_data = data["fundamental-data"]
    retail_data = data["retail-data"]
    cot_data = data["cot-data"]
    technical_data = data["technical-data"]
    seasonality_data = data["seasonality-data"]


    int_diff = float(fundamental_data[currency_map[base]]["interest-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["interest-rate"]["last"])
    int_change_diff = (float(fundamental_data[currency_map[base]]["interest-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["interest-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[quote]]["interest-rate"]["last"]) - float(
                          fundamental_data[currency_map[quote]]["interest-rate"]["previous"]))

    gdp_diff = float(fundamental_data[currency_map[base]]["gdp-growth-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["gdp-growth-rate"]["last"])
    gdp_change_diff = (float(fundamental_data[currency_map[base]]["gdp-growth-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["gdp-growth-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[quote]]["gdp-growth-rate"]["last"]) - float(
                          fundamental_data[currency_map[quote]]["gdp-growth-rate"]["previous"]))

    inf_diff = float(fundamental_data[currency_map[quote]]["inflation-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["inflation-rate"]["last"])
    inf_change_diff = (float(fundamental_data[currency_map[quote]]["inflation-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["inflation-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[base]]["inflation-rate"]["last"]) - float(
                          fundamental_data[currency_map[base]]["inflation-rate"]["previous"]))

    une_diff = float(fundamental_data[currency_map[quote]]["unemployment-rate"]["last"]) - float(
        fundamental_data[currency_map[base]]["unemployment-rate"]["last"])
    une_change_diff = (float(fundamental_data[currency_map[quote]]["unemployment-rate"]["last"]) - float(
        fundamental_data[currency_map[quote]]["unemployment-rate"]["previous"])) - (
                              float(fundamental_data[currency_map[base]]["unemployment-rate"]["last"]) - float(
                          fundamental_data[currency_map[base]]["unemployment-rate"]["previous"]))

    int_score = score_fundamental(int_diff, int_change_diff)
    gdp_score = score_fundamental(gdp_diff, gdp_change_diff)
    inf_score = score_fundamental(inf_diff, inf_change_diff)
    une_score = score_fundamental(une_diff, une_change_diff)
    cot_score = score_cot(cot_data[base], cot_data[quote])
    ret_score = score_retail(float(retail_data[pair]["long"]), float(retail_data[pair]["short"]))
    tec_score = score_technical(technical_data[pair])
    sea_score = score_seasonality(seasonality_data[pair][str(today.month).zfill(2)])

    total = round(int_score + gdp_score + inf_score + une_score + cot_score + ret_score + tec_score + sea_score, 0)
    return (int_score, gdp_score, inf_score, une_score, cot_score, ret_score, tec_score, sea_score, total)
