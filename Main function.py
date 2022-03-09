from Aplication import *
import requests
import json
from datetime import date,datetime
import requests

url = "http://127.0.0.1:8000/rest/workers/"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



_employeeInfos = json.loads(response.text)


def mainFunc(data):
  mainData = getSeniorEmployeeData(data)
  with open('mytexty.txt', 'w') as file:
    for person in mainData:
        file.write('name:')
        file.write(person['name'])
        file.write(' ')
        file.write('\n')
        file.write('work days:')
        file.write(str(person['work_days']))
        file.write('\n')