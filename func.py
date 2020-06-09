#!/usr/bin/env python
import json
import requests 

def getOrg(target,payload):
      urlfix = "https://api.meraki.com/api/v0/"
      with open("config.json") as json_data_file:
        data = json.load(json_data_file)
        #print('ApiKey: '+data["meraki"]["ApiKey"])
        ApiKey = data["meraki"]["ApiKey"]
      headers = {'Content-Type': 'application/json','X-Cisco-Meraki-API-Key':ApiKey}
      payload = payload
      response = requests.get(urlfix + target,headers=headers, params=payload)
      json_data = json.loads(response.text)
      #x = requests.get(URL+'organizations',headers=headers)
      #print('--------------------------------------------------------------------------------------')
      #print(response.text)
      #print(requests.status_code)
      #print('-------------------------------------')
      return json_data


def get(target,payload):
      with open("./meraki/config.json") as json_data_file:
        data = json.load(json_data_file)
        #print('ApiKey: '+data["meraki"]["ApiKey"])
        ApiKey = data["meraki"]["ApiKey"]
        url = data["meraki"]["Url1"]
      # api-endpoint 
      headers = {'Content-Type': 'application/json','X-Cisco-Meraki-API-Key':ApiKey}
      payload = payload
      response = requests.get(url+target,headers=headers, params=payload)
      json_data = json.loads(response.text)
      #x = requests.get(URL+'organizations',headers=headers)
      #print('--------------------------------------------------------------------------------------')
      #print(response.text)
      #print(requests.status_code)
      #print('-------------------------------------')
      return json_data



def delete(target,payload):
      with open("config.json") as json_data_file:
        data = json.load(json_data_file)
        ApiKey = data["meraki"]["ApiKey"]
        Url = data["meraki"]["Url1"]
      data=json.dumps(payload)
      headers = {'Content-Type': 'application/json','X-Cisco-Meraki-API-Key':ApiKey}
      response = requests.delete(Url+target,headers=headers, params=data)
      json_data = json.loads(response.text)
      return json_data

