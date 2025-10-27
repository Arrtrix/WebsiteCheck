For this assignmnet, I used ChatGPT to help me create my program in which sends an email about the status of a server whether it be running, unable to connect to the domain, timout error, or the server is down. I learned that when using the smtplib and email to send an email, I must use an app password from the send in order for the app to temporarily access an email account, and use the limited functions. The app password is like a temporary password that stays valid until it is revoked which also has limited access to the account as compared to using a regular password to login. If you have a g-mail account, you can acquire the app password by turning on 2-factor authentication, go to app passwords, create an app name, and then it should give you an app password. I used help from ChatGPT to help teach me how to send an email, and then used the modules to check whether if a server is up and running.

How to use: replace the app sender,reciever, and password your variables
 - Sender is the person sending the email
 - Reciever is the one who recieves the email
 - password is an app password, for the sender, which the app will gain limited access to the senders account and send the email.

prompts: 
 - what can I do with the libraries smtplib and email?
 - what is an app password?
 - so do I have to change the app password everytime I run the program?
 - Difference between an app password and a regular password?
 - is there any way to send emails without using an app password?
 - can you break down the code?