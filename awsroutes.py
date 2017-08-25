#! /usr/local/bin/python

import json
import requests
import ipaddress

url = "https://ip-ranges.amazonaws.com/ip-ranges.json"
a = requests.get(url=url)
b = a.json()


def iplist():
	try:
		ip_addr = input("ip address or network? ")
		ip_addr = ipaddress.ip_address(ip_addr)
		for awsnetworks in b["prefixes"]:
			prefix = awsnetworks["ip_prefix"]
			net = ipaddress.ip_network(prefix)
			if ip_addr in net:
				print(awsnetworks["ip_prefix"] + " # " + awsnetworks["region"] + " " + awsnetworks["service"] + "\r")
		print("End of results.")
	except ValueError:
		ip_addr = ipaddress.ip_network(ip_addr)
		for awsnetworks in b["prefixes"]:
			prefix = awsnetworks["ip_prefix"]
			net = ipaddress.ip_network(prefix)
			if ipaddress.IPv4Network.overlaps(ip_addr,net):
				print(awsnetworks["ip_prefix"] + " # " + awsnetworks["region"] + " " + awsnetworks["service"] + "\r")
		print("End of results.")	
				

def service():
	svc = input("\r\nWhat service are you looking for? (S3,amazon,ec2):  ")
	svc = svc.upper()

	region = input("Which region? (us,eu,ap,ca,sa):  ")
	region = region.lower()
	for awsnetworks in b["prefixes"]:
		prefix = awsnetworks["ip_prefix"]
		net = ipaddress.ip_network(prefix)
		if svc in awsnetworks["service"] and region in awsnetworks["region"]:
			print(awsnetworks["ip_prefix"] + " # " + awsnetworks["region"] + " " + awsnetworks["service"] + "\r")
	print("End of results.")

def main():
	serv_def = input("\nWould you like to look up an AWS service's IP block or IP's attached service?\n a) AWS service's IP block (ie s3,ec3,etc)\n b) IP's attached service\n")
	serv_def = serv_def.lower()
	if serv_def == "a":
		service()
	elif serv_def == "b":
		iplist()
	else:
		print("please choose \"a\" or \"b\"")
		main()

if __name__ == '__main__':
	main()

		
