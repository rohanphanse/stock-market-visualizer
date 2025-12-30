import json
import os

tickers_data = {}
base_dir = os.path.dirname(os.path.abspath(__file__))
tickers_path = os.path.join(base_dir, "tickers.txt")
with open(tickers_path, "r") as tickers:
    for t in tickers.readlines():
        t_split = t.split("|")
        if t_split[0].isalpha():
            try:
                tickers_data[t_split[0]] = t_split[1]
            except:
                pass

json_path = os.path.join(base_dir, "tickers.json")
with open(json_path, "w") as tickers_json:
    json.dump(tickers_data, tickers_json)
