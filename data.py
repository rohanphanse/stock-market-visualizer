import json

tickers_data = {}
with open("tickers.txt", "r") as tickers:
    for t in tickers.readlines():
        t_split = t.split("|")
        if t_split[0].isalpha():
            try:
                tickers_data[t_split[0]] = t_split[1]
            except:
                pass

with open("tickers.json", "w") as tickers_json:
    json.dump(tickers_data, tickers_json)