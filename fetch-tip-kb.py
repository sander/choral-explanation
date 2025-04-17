import choral_explanation
import json
import os
import urllib
from urllib.request import Request


TIP_UUID = 'dbc665a4-5364-468c-8bbc-e48790f3907e'
DIR_PATH = f"target/tip"


def _read_queries():
    with open("queries.graphql", 'r') as reader:
        return reader.read()

def _http_request(queries, operation, variables):
    endpoint = "https://alkem.io/api/private/graphql"
    payload = {
        'query': queries,
        'operationName': operation,
        'variables': variables
    }
    headers = {
        'Content-Type': 'application/json'
    }
    body = json.dumps(payload).encode('utf-8')
    return Request(endpoint, body, headers)

def _fetch_json(http_request):
    response = urllib.request.urlopen(http_request)
    text = response.read().decode('utf-8')
    return json.loads(text)


queries = _read_queries()
variables = {'spaceID': TIP_UUID}
request = _http_request(queries, 'questions', variables)
raw_data = _fetch_json(request)

os.makedirs(f"{DIR_PATH}", exist_ok=True)

with open(f"{DIR_PATH}/raw-data.json", 'w', encoding='utf-8') as file:
	json.dump(raw_data, file, indent=2, ensure_ascii=False)
	file.write("\n")
