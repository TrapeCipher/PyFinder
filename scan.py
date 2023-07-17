import scapy.all as scapy
import re
import os
import colorama
import fade
from colorama import Fore
from os import name

def cls():
    os.system("cls" if name == "nt" else "clear")

design1 = """\n
\t\t ▄▄▄▄▄▄▄ ▄▄   ▄▄    ▄▄▄▄▄▄▄ ▄▄▄ ▄▄    ▄ ▄▄▄▄▄▄  ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   
\t\t█       █  █ █  █  █       █   █  █  █ █      ██       █   ▄  █  
\t\t█    ▄  █  █▄█  █  █    ▄▄▄█   █   █▄█ █  ▄    █    ▄▄▄█  █ █ █  
\t\t█   █▄█ █       █  █   █▄▄▄█   █       █ █ █   █   █▄▄▄█   █▄▄█▄ 
\t\t█    ▄▄▄█▄     ▄█  █    ▄▄▄█   █  ▄    █ █▄█   █    ▄▄▄█    ▄▄  █
\t\t█   █     █   █    █   █   █   █ █ █   █       █   █▄▄▄█   █  █ █
\t\t█▄▄▄█     █▄▄▄█    █▄▄▄█   █▄▄▄█▄█  █▄▄█▄▄▄▄▄▄██▄▄▄▄▄▄▄█▄▄▄█  █▄█
\t\t╔══════╦═══════════════════════╦═══════════════════════╦════════╗
\t\t       ║ Made By: trape_cipher ║ Network Device Finder ║ 
\t\t╚══════╩═══════════════════════╩═══════════════════════╩════════╝\n
"""

while True:
    cls()
    print(fade.water(design1))
    ip_range = input(f"{Fore.BLUE}[{Fore.WHITE} ? {Fore.BLUE}] {Fore.WHITE}Input Router IP Address {Fore.LIGHTRED_EX}192.168.1.0/24 {Fore.LIGHTBLUE_EX}>>> {Fore.WHITE}")
    if (ip_range := re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})", ip_range)):
        result = scapy.arping(ip_range.group(1))
        input()
    else:
        print(f"{Fore.RED}[{Fore.WHITE} ! {Fore.RED}] {Fore.WHITE}Invalid IP address format. Please try again.")
        input()
