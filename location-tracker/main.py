import os
import requests
import json
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ipaddress", help="Ip address to track", required=True)
    args = parser.parse_args()
    ip = args.ipaddress

    url = "http://ip-api.com/json/" + ip

    response = requests.get(url)

    values = json.loads(response.content)
    
    print(values)


    print("\t[+] IP\t\t\t", values["query"])
    print("\t[+] CITY\t\t", values["city"])
    print("\t[+] ISP\t\t\t", values["isp"])
    print("\t[+] LOC\t\t\t", values["country"])
    print("\t[+] REG\t\t\t", values["regionName"])
    print("\t[+] TIME\t\t", values["timezone"])
    print("\t[+] ZIP\t\t\t", values["zip"])
    print("\t[+] LAT\t\t\t", values["lat"])
    print("\t[+] LON\t\t\t", values["lon"])
    
    
