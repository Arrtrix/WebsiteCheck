# Name: Jose Barut
#print("Hello, World") #test 

# This script is used to check if a website goes down
# AI prompt: what can I do with the libraries smtplib and email?

#!/usr/bin/env python3

#import libraries
import socket, requests, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Variables:
# Email setup
sender = "sender@mail.com"
receiver = "reciever@mail.com"
password = "app_password" #use app password to allow access to email without giving the real password. Check reflection to see how to get app password

# Build the email
msg = MIMEMultipart() #container for the email which holds the txt, attachments, and HTML content
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Hello from Python!"

#get the url and strip the url to get the doamin
url = "https://www.google.com/"
domain = url.split("//")[-1].split("/")[0]

#DNS lookup to check if the domain exists or is reachable
try:
    ip = socket.gethostbyname(domain) #if successful, show the resolved IP addresss
    body = f"Resolved {domain} → {ip}"
except socket.gaierror as e:
    body = f"DNS lookup failed: {e}" #failed to reach the domain
    ip = None

#Check if the ip is valid
if ip:
    try:
        r = requests.get(url, timeout=3) #make a request to the url
        body = f"Server is up and running"
    except requests.exceptions.Timeout: #check for timeout
        body = f"Server may be down or slow."
    except requests.exceptions.ConnectionError: #check for connection
        body = f"Server appears to be down"
    except Exception as e: #unknown error caught
        body = f"Unexpected error: {e}"

# Add message body
msg.attach(MIMEText(body, "plain")) #add the body and "plain" indicates normal text

# Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server: #connect the to the Gmail SMTP server
        server.starttls()  # Encrypt the connection
        server.login(sender, password) #Login to the email server
        server.send_message(msg) #send the email
        print("Email sent successfully!") #Notify of success
except Exception as e:
    print("Error sending email:", e) #notify of failure

