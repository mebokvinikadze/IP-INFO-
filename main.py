import requests
from time import sleep
from os import *
from re import match
import sys

def ipinfo(local): #define printing out ip info
        if len(request) == 1: #if length returned is 1
           print("Lookup failed.")
        else:
            if local:
                print("Displaying your ip info...")
            if not local:
                print("Displaying ip info...")
            print("Success!\n")
            print("IP: " + request["ip"])
            print("City: " + request["city"])
            print("Region: " + request["region"])
            print("Country: " + request["country"])
            print("Loc: " + request["loc"])
            print("Org: " + request["org"])
            print("Timezone: " + request["timezone"])

ipv4 = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$" #simple regex for an ipv4 address
print('Type "help" for a list of commands')
while True: 
        command = input("IP Lookup: ")
        if command == "help":
            print('\n"exit" - Exit the application')
            print('"myip" - See your own ip info')
            print('"clear" - Clear the window\n')
        elif command == "":
            pass
        elif command == "clear":
            if name == "nt": #if on windows
                system("cls")
            else: #if on anything but windows
                system("clear")
        elif command == "exit":
            print("Exiting...")
            sleep(1)
            sys.exit()
        elif command == "myip":
            request = requests.get("https://ipinfo.io/geo").json() #requests with no input (defaults to your ip)
            ipinfo(True) #print ip info
        elif not match(ipv4, command): #if ipv4 regex doesn't match input
            print("Error: Invalid IP")
        else:
            request = requests.get(f"https://ipinfo.io/{command}/geo").json() #requests with your input
            ipinfo(False) #print ip info
