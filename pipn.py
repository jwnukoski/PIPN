import smtplib, ssl, time
from json import load
from urllib.request import urlopen

def getPublicIp():
    # Uses ipify
    try:
        return load(urlopen('https://api.ipify.org/?format=json'))['ip']
    except Exception as e:
        print("Error getting public IP. " + str(e))
        return "0.0.0.0"

def sendEmail(_smtpServer, _smtpPort, _senderEmail, _password, _receiverEmail, _msg):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(_smtpServer, _smtpPort) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(_senderEmail, _password)
            server.sendmail(_senderEmail, _receiverEmail, _msg)
        print("Email sent for updated IP: " + _msg)
    except Exception as e:
        print("Error sending email. " + str(e))

# Change your settings here if you dont want to use google SMTP, or
# dont want to input your settings each time. DONT save your password in here.
smtpPort = int(input("Enter the SMTP port (Google: 587): "))  # For starttls
smtpServer = input("Enter the SMTP server (Google: smtp.gmail.com): ")
senderEmail = input("Sender email address: ")
if (senderEmail.__contains__("@gmail.com")):
    # Tip for gmail users.
    print("\nLooks like you are using Gmail. Make sure Less secure app access is on.\nRead more here: https://myaccount.google.com/lesssecureapps\n")
receiverEmail = input("Receiver email address: ")
password = input("Type your password and press enter: ")

# Time in seconds you want to grab your public IP
checkInterval = int(input("Enter the public IP query interval in minutes: ")) * 60

# Doesnt need changed.
cachedIp = ''

while(True):
    ip = getPublicIp()
    if (cachedIp != ip):
        cachedIp = ip
        sendEmail(smtpServer, smtpPort, senderEmail, password, receiverEmail, cachedIp)
    time.sleep(checkInterval)




