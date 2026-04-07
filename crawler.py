import requests
import json

web = requests.get('https://opendata.tycg.gov.tw/api/v1/dataset.api_access?rid=5e6c7a16-3592-4c6d-a6ba-1607dd76980b&format=json')
web.encoding = 'utf-8'

jsonfile = "crawler_data.json"

json_data = json.loads(web.text)
with open(jsonfile, 'w') as fp:
    json.dump(json_data, fp)
