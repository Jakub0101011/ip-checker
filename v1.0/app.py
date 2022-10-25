# v1.0

#1 - https://ipwhois.io/documentation
#2 - https://ip-api.com/docs/api

import requests
import platform
import json
from colorama import Fore, Back, Style
import os

def center(let:str, space:int=None):
    if not space:
        space = (os.get_terminal_size().columns - len(let.splitlines()[int(len(let.splitlines())/2)])) / 2

    return "\n".join((' ' * int(space)) + let for let in let.splitlines())
os.system(f'cls && title APP - IP CHECKER v1.0' if os.name == "nt" else "clear")
print(center(f"""\n\n
~     IP CHECKER V1.0    ~
~ github.com/pokczampDev ~
        HeLLo;]\n\n
              """).replace('~', Fore.MAGENTA+"~"+Fore.RESET).replace('-', Fore.MAGENTA+"-"+Fore.RESET))

resp = requests.get("http://ipwho.is/").json()
#MAIN
print(Fore.YELLOW+'Success?'+Fore.RESET,resp['success'])
print(Fore.BLUE+'[Main info]'+Fore.RESET)
print(' $ Country: {0} {1}\n $ IP: {2}\n $ Region: {3}\n $ Postal: {5}\n $ City: {6}\n $ Continent: {7}\n $ Type: {4}'.format(resp['country'],resp['flag']['emoji'],resp['ip'],resp['region'],resp['type'], resp['postal'], resp['city'], resp['continent']).replace('$', Fore.BLUE+'$'+Fore.RESET))
#CONNECTION
print(Fore.BLUE+'[CONNECTION]'+Fore.RESET)
print(' $ DOMAIN: {0}\n $ ASN: {1}\n $ ISP: {2}'.format(resp['connection']['domain'], resp['connection']['asn'], resp['connection']['isp']).replace('$', Fore.BLUE+'$'+Fore.RESET))
print(Fore.BLUE+'[OS]'+Fore.RESET)
#OS
print(' $ OS:'.replace('$', Fore.BLUE+'$'+Fore.RESET), platform.system(), platform.release())

# Version 2.0 coming soon
