import smtplib, time
from json import load

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def getPublicIp():
    try:
        return load(urlopen('https://api.ipify.org/?format=json'))['ip']
    except Exception as e:
        print("Error getting public IP. " + str(e))
        return "0.0.0.0"

def sendEmail(_smtpServer, _smtpPort, _senderEmail, _password, _receiverEmail, _msg):
    print("Trying to send email notification about IP being: " + _msg)
    try:
        # ???

        print("Email sent for updated IP: " + _msg)
    except Exception as e:
        print("Error sending email: " + str(e))

smtpPort = int(raw_input("Enter the SMTP port (Google: 587): "))
smtpServer = raw_input("Enter the SMTP server (Google: smtp.gmail.com): ")
senderEmail = raw_input("Sender email address: ")
password = raw_input("Type your password and press enter: ")

# Tip for gmail users.
if (senderEmail.__contains__("@gmail.com")):
    print("\nLooks like you are using Gmail. Make sure Less secure app access is on.\nRead more here: https://myaccount.google.com/lesssecureapps\n")

receiverEmail = raw_input("Receiver email address: ")

checkInterval = int(raw_input("Enter the public IP query interval in minutes: ")) * 60

cachedIp = ''

while(True):
    ip = getPublicIp()
    if (cachedIp != ip):
        cachedIp = ip
        sendEmail(smtpServer, smtpPort, senderEmail, password, receiverEmail, cachedIp)
    time.sleep(checkInterval)




