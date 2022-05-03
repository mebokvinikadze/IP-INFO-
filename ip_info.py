import requests
from time import sleep
from os import *
from re import match
import sys
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'ipinfo'
)


def ipinfo(local): #define printing out ip info
    if len(request) == 1: #if length returned is 1
        print("Invalid IP Address!"'\n')
    else:
        if local:
            print("Displaying your ip info...")
        if not local:
            print("Displaying ip info...")
        print("Success!\n")
        print("ip: " + request["query"])
        print("city: " + request["city"])
        print("regionName: " + request["regionName"])
        print("Country: " + request["country"])
        print("isp: " + request["isp"])
        print("org: " + request["org"])
        print("proxy: " + str(request["proxy"]))


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
             request = requests.get("http://ip-api.com/json/?fields=140825").json() #requests with no input (defaults to your ip)
             ipinfo(True) #print ip info
        elif not match(ipv4, command): #if ipv4 regex doesn't match input
                print("Error: Invalid IP")
        else:
            request = requests.get(f"http://ip-api.com/json/{command}?fields=140825").json() #requests with your input
            ipinfo(False) #print ip info

            #############################################################################################################################

            cursor = mydb.cursor()

            mysql = "INSERT INTO ipinformation (query, city, regionName, country, isp, org, proxy_) VALUES(%s, %s, %s, %s, %s, %s, %s)"

            val1 = (request['query'], 
                    request['city'], 
                    request['regionName'], 
                    request['country'], 
                    request['isp'],
                    request['org'],
                    request['proxy'])

            cursor.execute(mysql, val1) 
            mydb.commit()

            print('\n'"Data sent succesfully"'\n')
       