import requests 
import json 
import os
from dotenv import load_dotenv

load_dotenv()

def httpRequest(type: str, url: str, body:dict={}, headers:dict={}) -> dict:
	if type == "GET":
		r = requests.get(url, params=body, headers=headers)
	elif type == "POST":
		r = requests.post(url, data=json.dumps(body), headers=headers)
	elif type == "PUT":
		r = requests.put(url, data=json.dumps(body), headers=headers)
	elif type == "DELETE":
		r = requests.delete(url, data=json.dumps(body), headers=headers)

	if r.status_code == 200:
		return r.json()
	else:
		print(r.content)
		raise Exception("Request Failed")

def get_data(name):
    try:
        headers = {
        'Content-Type': 'application/json'
        }
        r = httpRequest("POST", os.getenv("JSONLAMBDA"), {"name": name}, headers)

        return r
    except Exception as e:
        print(e)
        raise Exception("Something happened")