import json
import os.path
import pandas as pd
from glob import glob


def json_helper(path):

    def read_json(path):
        with open(path, 'r') as f:
            data = json.load(f)
            return data

    for dirpath, dirnames, filenames in os.walk(path):
            result = []
            for f in filenames:
                if f.endswith('.json'):
                    json_content_2 = read_json(os.path.join(path, f))
                    for i in json_content_2["results"]:
                        i["source"] = f
                        result.append(i)
            df_loc = pd.DataFrame(result)
            return df_loc


if __name__ == "__main__":
    print(json_helper('/Users/cchavez/dev/DataEngineering.Labs.NOAADailySummaries/data/daily_summaries'))

#/Users/cchavez/dev/DataEngineering.Labs.NOAADailySummaries/data/daily_summaries




"""
def json_helper(json_root):
    for root, _, files in os.walk(json_root):
        result = []
        for f in files:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(json_root, f))
                result.append(json_content)
            with open('data.json_content') as json_file:
                data = json.load(json_content)
    return data

with open('data.json') as json_file:
    data = json.load(json_file)

print(data)



with open('data.json') as json_file:
    data = json.load(json_file)

print(data)


path = os.path.join('file location')
json_contents = read_json(path)
all_results = pd.DataFrame(json_contents['results'])
"""
