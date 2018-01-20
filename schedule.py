import sys
import datetime
import pychromecast
import smtplib
import email
from email.mime.text import MIMEText
import requests
from random import *

# Domoticz IP and port settings
#URL_DOMOTICZ = 'http://192.168.1.5:8080/'
URL_DOMOTICZ = 'http://127.0.0.1:8080/'

# Grab current time
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print (time)

# Path to schedule file
file = 'schedule.txt'

# Funtions section

# birthday
# The birthday function plays a definded mp3 file to a definded Chromecast device 
# The function requires to parameters to be passed in order to work:
# The Chromecast_device is the name of the the Chromcast device or group - this is cast sensitive
# The media_path parameter is the location of the media file located in the www/media directory  
def birthday(Chromecast_device, media_path):
	track = str(randint(1, 4))
	device_name = Chromecast_device
	chromecasts = pychromecast.get_chromecasts()
	cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_name)
	cast.wait()
	#print(cast.device)
	#print(cast.status)
	mc = cast.media_controller
	mc.play_media(URL_DOMOTICZ + media_path + track + ".mp3", 'audio/mp3')
	mc.block_until_active()
	#print(mc.status)
	mc.play()
	log = "Sending " + media_path + track + ".mp3 to " + Chromecast_device
	print(log) 
	req = requests.get(URL_DOMOTICZ + 'json.htm?type=command&param=addlogmessage&message=' + log)

# send_text
# The send_text function sends a defined text message with a defined subject to a definded email address
# The send_text function requires three parameters - Send_to, Text_subject and Text_body  
def send_text(Send_to, Text_subject, Text_body):
	fromaddr = "automated_message@domain.com"
	toaddr = Send_to # mailbox@domain.com"
	subject = Text_subject
	body = Text_body
	msg = MIMEText(body) 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = subject
	msg['Orig-date'] = time
	# smtp server setting
	# server = smtplib.SMTP("smtp.mail.myprovider.com", 587)
	server = smtplib.SMTP("smtp.com", 587)
	# User name add password to authenticate to smtp server
	server.login("user", "pass")
	server.send_message(msg)
	server.quit()
	log = "Sending text message to " + toaddr
	print(log)
	req = requests.get(URL_DOMOTICZ + 'json.htm?type=command&param=addlogmessage&message=' + log)

# 	
def timed_device(idx, On_or_Off):
	#json.htm?type=command&param=switchlight&idx=99&switchcmd=Off
	url = URL_DOMOTICZ + "json.htm?type=command&param=switchlight&idx=" + idx + "&switchcmd=" + On_or_Off
	req = requests.get(URL_DOMOTICZ + "json.htm?type=command&param=switchlight&idx=" + idx + "&switchcmd=" + On_or_Off)
	log = "Sending " + On_or_Off + " command to idx: " + idx
	req = requests.get(URL_DOMOTICZ + 'json.htm?type=command&param=addlogmessage&message=' + log)
	

#Loop through the schedule file	

with open(file) as s:
	line = s.readline()
	cnt = 1
	while line:
		stuff = line.split("|")
		event_time = stuff[0]
		event_title = stuff[1]
		triggered_function = stuff[2]
		param1 = stuff[3]
		param2 = stuff[4]
		param3 = stuff[5]
	
		if event_time == time:
			f=triggered_function
			# Change number of parameters depending on the function being called - locals()[f](param1,param2,param[X],...)
			if f == "birthday":
				print("Calling: " + triggered_function + "(" + param1 + "," + param2 + ")") 
				locals()[f](param1,param2)
			elif f == "send_text":
				print("Calling: " + triggered_function + "(" + param1 + "," + param2 + "," + param3 + ")") 
				locals()[f](param1,param2,param3)
			elif f == "timed_device":
				print("Calling: " + triggered_function + "(" + param1 + "," + param2 + ")") 
				locals()[f](param1,param2)
			

		if event_time == "TEST":
			f=triggered_function
			# Change number of parameters depending on the function being called - locals()[f](param1,param2,param[X],...)
			if f == "birthday":
				print("Calling: " + triggered_function + "(" + param1 + "," + param2 + ")") 
				locals()[f](param1,param2)
			elif f == "send_text":
				print("Calling: " + triggered_function + "(" + param1 + "," + param2 + "," + param3 + ")") 
				locals()[f](param1,param2,param3)
			elif f == "timed_device":
				print("Calling: " + triggered_function + "(" + param1 + "," + param2 + ")") 
				locals()[f](param1,param2)
			
		line = s.readline()
		cnt += 1
exit()