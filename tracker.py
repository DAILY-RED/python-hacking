import requests 
import argparse
import json

if __name__ == "__main__":

    # Parse the argument (converting data from one format to another.)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ipaddress", help="IP address to track")
    
    # This will parse the parse argument into args
    args = parser.parse_args()
    ip = args.ipaddress

    # The url will give information related to that IP
    url = "http://ip-api.com/json/"
    response = requests.get(url)

    # Get data in json Format
    data = json.loads(response.content)
    print(data)

    print("\t[+] IP\t\t\t", data["query"])
    print("\t[+] CITY\t\t\t", data["city"])
    print("\t[+] ISP\t\t\t", data["isp"])
    print("\t[+] LOC\t\t\t", data["country"])
    print("\t[+] REG\t\t\t", data["regionName"])
    print("\t[+] TIME\t\t\t", data["timezone"])
    print("\t[+] ZIP\t\t\t", data["zip"])
    print("\t[+] LAT\t\t\t", data["lat"])
    print("\t[+] LON\t\t\t", data["lon"])