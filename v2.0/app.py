# v2.0
# Author - PokczampDev

import requests
import platform
import json
from colorama import Fore, Back, Style
import os
from datetime import datetime
import time
import socket

#Variables
now = datetime.now()
curtime = now.strftime("%H:%M")
author = "Джейкоб;#0320"
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
def back():
    input(f"{Fore.YELLOW}Press enter to go back.")
def underdev():
    print(f"{Fore.RED}{curtime}{Fore.LIGHTWHITE_EX} Hey! this is currently under development. (version 2.0)")
    back()
    clearcmd()
def autorek():
    print(f"{Fore.LIGHTWHITE_EX}Made by: {Fore.GREEN}PokczampDev\n{Fore.RESET}{Fore.LIGHTWHITE_EX}Discord: {Fore.GREEN}{author}\n{Fore.RESET}{Fore.LIGHTWHITE_EX}Github: {Fore.GREEN}github.com/pokczampDev")
def options():
    print("""
    v. 2.0 (November 17th 2022)
    ░█████╗░██████╗░████████╗██╗░█████╗░███╗░░██╗  ░░███╗░░
    ██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║  ░████║░░
    ██║░░██║██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║  ██╔██║░░
    ██║░░██║██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║  ╚═╝██║░░
    ╚█████╔╝██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║  ███████╗
    ░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝
                                                                          """)
    print(f'''{Fore.LIGHTWHITE_EX}            [ Made by {Fore.YELLOW}PokczampDev({author}) {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print("""
    [1] Option 2
    [2] Settings [Soon, it is currently disabled]
    [3] Author
    [4] Quit


    """)
    USER_OPTION = input(f"Option\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        options2()
    elif USER_OPTION == "2":
        pass
    elif USER_OPTION == "4":
        clearcmd()
        quit()
    elif USER_OPTION == "3":
        autorek()
        back()
        clearcmd()
        options()
    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not reckognize input {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        options()

def options2():
    print(f"""
    v. 2.0 (November 17th 2022)
    ░█████╗░██████╗░████████╗██╗░█████╗░███╗░░██╗  ██████╗░
    ██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║  ╚════██╗
    ██║░░██║██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║  ░░███╔═╝
    ██║░░██║██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║  ██╔══╝░░
    ╚█████╔╝██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║  ███████╗
    ░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝
                                                                          """)
    print(f'''{Fore.LIGHTWHITE_EX}            [ Made by {Fore.YELLOW}PokczampDev({author}) {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  ''')
    print("""
    [1] Your IP
    [2] Write another ip
    [3] Info
    [4] Go back


    """)
    USER_OPTION = input(f"Option\n{Fore.RED}>")
    if USER_OPTION == "1":
        clearcmd()
        checkmyip()
    elif USER_OPTION == "2":
        clearcmd()
        checkipmore()
    elif USER_OPTION == "3":
        underdev()
        options2()
    elif USER_OPTION == "4":
        clearcmd()
        options()
    else:
        print(f"\n{Fore.RED}[-]{Fore.LIGHTWHITE_EX} Did not reckognize input {Fore.YELLOW}{USER_OPTION}{Fore.LIGHTWHITE_EX}, Try again.")
        time.sleep(1)
        back()
        clearcmd()
        options2()

def checkmyip():
    print("""
     Ip checker (v.2.0)
    ██╗██████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
    ██║██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ██║██████╔╝  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ██║██╔═══╝░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ██║██║░░░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
    ╚═╝╚═╝░░░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """)
    print(f"""{Fore.LIGHTWHITE_EX}     [ Made by {Fore.YELLOW}PokczampDev({author}) {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  """)
    print('Wait second...')
    time.sleep(1)
    resp = requests.get("http://ipwho.is/").json()
#MAIN
    print(Fore.YELLOW+'Success?'+Fore.RESET,resp['success'])
    print(Fore.BLUE+'[Main info]'+Fore.RESET)
    print(' $ Country: {0} {1}\n $ Borders: {8}\n $ IP: {2}\n $ Region: {3}\n $ Postal: {5}\n $ City: {6}\n $ Continent: {7}\n $ Type: {4}'.format(resp['country'],resp['flag']['emoji'],resp['ip'],resp['region'],resp['type'], resp['postal'], resp['city'], resp['continent'], resp['borders']).replace('$', Fore.BLUE+'$'+Fore.RESET))
#CONNECTION
    print(Fore.BLUE+'[CONNECTION]'+Fore.RESET)
    print(' $ DOMAIN: {0}\n $ ASN: {1}\n $ ISP: {2}'.format(resp['connection']['domain'], resp['connection']['asn'], resp['connection']['isp']).replace('$', Fore.BLUE+'$'+Fore.RESET))
    print(Fore.BLUE+'[OS]'+Fore.RESET)
#OS
    print(' $ OS:'.replace('$', Fore.BLUE+'$'+Fore.RESET), platform.system(), platform.release())
    print(' $ Hostname: {0}\n $ IP PC: {1}'.format(hostname, IPAddr).replace('$', Fore.BLUE+'$'+Fore.RESET))
    back()
    clearcmd()
    options2()


def checkipmore():
    print("""
     Ip checker (v.2.0)
    ██╗██████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
    ██║██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ██║██████╔╝  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ██║██╔═══╝░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ██║██║░░░░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
    ╚═╝╚═╝░░░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """)
    print(f"""{Fore.LIGHTWHITE_EX}     [ Made by {Fore.YELLOW}PokczampDev({author}) {Fore.LIGHTWHITE_EX}]
  {Fore.LIGHTWHITE_EX}
  """)

    try:
        d = input("IP(ex. 8.8.8.8):")

        if d == '' :
            print ('You cannot enter an empty IP address.')
            time.sleep(2)
            clearcmd()
            options2()
        else:
                print('Wait second...')
                time.sleep(1)


        resp = requests.get("http://ipwho.is/"+d).json()
#MAIN
        print(Fore.YELLOW+'Success?'+Fore.RESET,resp['success'])
        print(Fore.BLUE+'[Main info]'+Fore.RESET)
        print(' $ Country: {0} {1}\n $ Borders: {8}\n $ IP: {2}\n $ Region: {3}\n $ Postal: {5}\n $ City: {6}\n $ Continent: {7}\n $ Type: {4}'.format(resp['country'],resp['flag']['emoji'],resp['ip'],resp['region'],resp['type'], resp['postal'], resp['city'], resp['continent'], resp['borders']).replace('$', Fore.BLUE+'$'+Fore.RESET))
#CONNECTION
        print(Fore.BLUE+'[CONNECTION]'+Fore.RESET)
        print(' $ DOMAIN: {0}\n $ ASN: {1}\n $ ISP: {2}'.format(resp['connection']['domain'], resp['connection']['asn'], resp['connection']['isp']).replace('$', Fore.BLUE+'$'+Fore.RESET))
        back()
        clearcmd()
        options2()

    except (IndexError, KeyError):
        clearcmd()
        print (f"{Fore.RED}{curtime}{Fore.RESET} Please enter an IP address to continue. (Invalid IP address)")
        time.sleep(3.5)
        clearcmd()
        options2()


def main():
    try:
        clearcmd()
        options()
    except KeyboardInterrupt:
        print(f"{Fore.RED}{curtime} CTRL + C detected, Going back to the main menu!")
        time.sleep(1)
        options()
main()