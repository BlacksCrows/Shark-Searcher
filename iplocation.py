#!/usr/bin/python3
#Title: ipgeoloc.py
#Author: ApexPredator
#License: MIT
#Github: https://github.com/ApexPredator-InfoSec/IP-Geolocation
#Description: This script take an IP or list of IPs and run them thru the ipgeolocation.io API to return owner and locaton
import requests
import argparse
from netaddr import IPNetwork
from urllib3.exceptions import InsecureRequestWarning

parser = argparse.ArgumentParser(prog='ipgeoloc.py', usage='python3 -t <target> -f <file contianing target list> -d\npython3 ipgeoloc.py -t 8.8.8.8 -d\npython3 ipgeoloc.py -f ips.txt') #build argument list
parser.add_argument('-t', '--target', help='Target IP', required=False)
parser.add_argument('-f', '--file', help='File Containing Target URLs', required=False)
parser.add_argument('-c', '--cidr', help='Target IP block in CIDR notation', required=False)
parser.add_argument('-cf', '--cfile', help='File Containing Target IP Block in CIDR notation', required=False)
parser.add_argument('-d','--debug', help='Debug with proxy', required=False, action = 'store_const', const = True)
args = parser.parse_args()

s = requests.session()
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning) #disable SSL verification warning to cleanup output

http_proxy = 'http://127.0.0.1:8080' #define proxy address to enable using BURP or ZAP
proxyDict = { #define proxy dictionary to enable using BURP or ZAP
            "http" : http_proxy,
            "https" : http_proxy
}

if args.debug:
    proxy = proxyDict #enable proxy if -d or --debug is present
else:
    proxy = False #disable proxy is -d or --debug is not present

def test_ip(target):

    res = s.get('https://api.ipgeolocation.io/ipgeo?apiKey=<API KEY>&ip=%s' %target, verify=False, proxies=proxy)
    jres = res.json() #pull JSON values from response
    print("[+]IP: " + jres["ip"]) #beging parsing and displaying individual JSON values
    print("[+]Owner: " + jres["organization"])
    print("[+]Country: " + jres["country_code2"])
    print("[+]State/Province: " + jres["state_prov"])
    print("[+]City: " + jres["city"])
    print("[+]Zipcode: " + jres["zipcode"])
    print("[+]Lat/Long: " + jres["latitude"] + ',' + jres["longitude"])
    print("[+]ISP: " + jres["isp"])
    print("[+]Timezone: " + jres["time_zone"]["name"])
    print("[+]Current time at target: standard " + jres["time_zone"]["current_time"] + ', epoch ' + str(jres["time_zone"]["current_time_unix"]))

def main():

    if args.target: #test it -t or --target were passed and set target with value passed
        target = args.target
        test_ip(target)

    elif args.file: #test if -f or --file were passed and set target with file named passed
        file = args.file
        with open(file, 'r') as target_list: #open file passed
            for line in target_list.readlines(): #read the lines in
                target = line.strip() #set target
                print("\n[+]Fetching IP from file.......\n")
                test_ip(target) #test the IP currently set in target

    elif args.cidr:
        for ip in IPNetwork(args.cidr): #read in CIDR notation and break them in to individual IPs
            target = ip #set target to current IP from CIDR block
            print("\n[+]Fetching IP from CIDR notation....\n")
            test_ip(target) #test current IP from CIDR block

    elif args.cfile:
        cfile = args.cfile #set cfile to file passed with -cf or --cfile argument
        with open(cfile, 'r') as target_list: #open the file for reading
            for line in target_list.readlines(): #read each line
                target = line.strip() #set target to current line CIDR notation IP block
                print("\n[+]Fetching IP from CIDR notation....\n")
                for ip in IPNetwork(target): #break CIDR notation down to individual IPs
                    targetc = ip #set target to current IP from CIDR block
                    print("\n[+]Fetching IP from CIDR notation....\n")
                    test_ip(targetc) #test current IP from CIDR block
    else:
        print("[-]Either -t, -f, -c, or -cf arguments are required\nusage: python3 ipgeoloc.py -t <target> -f <file contianing target list> -d\npython3 ipgeoloc.py -t 8.8.8.8 -d\npython3 ipgeoloc.py -f ips.txt\npython3 ipgeoloc.py -c 8.8.8.0/24\npython3 ipgeoloc.py -cf cips.txt") #print help message if neither -t or -f is passed

if __name__ == '__main__':

    main()
