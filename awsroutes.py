#! /usr/local/bin/python

import json
import requests


url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
a = requests.get(url=url)
b = a.json()

svc = input("\r\nWhat service are you looking for? (S3,amazon,ec2):  ")
svc = svc.upper()

region = input("Which region? (us,eu,ap,ca,sa):  ")
region = region.lower()

#reads dictionary from each index iteration in JSON file
for awsnetworks in b["prefixes"]:
	if svc in awsnetworks["service"] and region in awsnetworks["region"]:
		print(awsnetworks["ip_prefix"] + " # " + awsnetworks["region"] + " " + awsnetworks["service"] + "\r")
		
