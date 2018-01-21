# DomoWeatherAlert

Script Prerequisites:
Google Chromecast device(s)
Python 3.x installed
Python modules: sys, datetime, pychromecast, smtplib, email and requests  

The schedule.py script reads in data from a schedule.txt file located in the /scripts/python directory.  
The schedule file is set up with each line containing the information for a timed event with the information formated as follows:

<spen style="color:blue;">time|title|function|param1|param2|param3</span>


time - is the time of the event formated as YYYY-MM-DD HH:MM
title - is the title of the event
function - currently there are only three functions - birthday, send_text and timed_device

birthday - plays a random song located in the www/media/birthday songs directory. The songs are named 1.mp3,2.mp3,3.mp3,etc...
sent_text - sends a text message 
timed_device - turned on/off a device using the device's idx number

Params1,2,3 are used to pass parameters according to the functions parameters - see the comments in the schedule.py script for more information about the parameters for the functions
 
To get this up and running:

1) Place the schedule.py file in the /scripts/python directory 
2) Place the lua script in the /scripts/lua directory
3) Create a birthday songs directory in the www/media directory
4) Copy birthday songs into the birthday songs directory
5) Rename songs 1.mp2, 2.mp3 and so on untill all song names are a number
6) Edit the second number in the randint function to match the number of mp3 files you have in your www/media/birthday songs directory  
7) Edit the fromaddr to the desire from email address
8) Edit line 60 to reflect your smtp sever and port
9) Edit line 62 to reflect your user and password information used to connect to your smtp server
10) Modify the schedule.txt file as desire - each line needs 5 pipe characters - "|" - regardless of the function being called  

More functions can easily be added by creating more def's 

As well for testing purposes there is a testing parameter that can be used to bypass the time = use 'TEST' in the time field.   

Running on Windows 10 | Domoticz Version: 3.8153 | Nest/z-wave/milights/Kodi/LMS/Google Home
