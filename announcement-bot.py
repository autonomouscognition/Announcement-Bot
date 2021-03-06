import urllib
import re
import smtplib
import datetime
now = datetime.datetime.now()
from email.mime.text import MIMEText

# Parses Ehgp for any words found in the proporties file.
# Use README for other questions

def readPage():
    #open page and copy code to htmlSource
    sock = urllib.urlopen("http://electronichgp.holyghostprep.org/readannouncements_2.php")
    src = sock.read()
    sock.close()
    return src.lower() #returns lowercase version of code

def insNames():
    #inserts the values from "properties.txt" into array 'values'
    values = []
    file = open('properties.txt', 'r')
    for word in file:
        word = " " + word
        values.append(word.rstrip('\n')) #removes "\n" from the end of each line
    return values

def checkIfInText(values, htmlSource):
    #checks for above names in htmlSource
    srcsplit = re.split("<hr>", htmlSource)
    finalList = "Todays Announcements: \n"
    for value in values:
        for i in range(0,len(srcsplit)):
            if value in srcsplit[i]:
                finalList += (srcsplit[i] + "\n") # compiles announcements into one string, separated by new lines
    return finalList

def sendEmail(announce):
    #sends email
    fromaddr = 'announcementbot@autonomouscognition.com' #email to send FROM
    toaddr = '[PUT AN EMAIL HERE]' #email to send TO
    msg = MIMEText(announce)
    month = now.month
    day = now.day
    year = now.year
    msg['Subject'] = "Announcements for " + str(month) + "/" + str(day) + "/" + str(year)
    msg['From'] = fromaddr
    msg['To'] = toaddr
    server = smtplib.SMTP('[WEB ADDRESS]', [PORT]) #Replace "Web address" and "port" with corresponding values
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("[USERNAME]", "[PASSWORD]") #login info from SMTP provider
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

htmlSource = readPage()
values = insNames()
announce = checkIfInText(values, htmlSource)
sendEmail(announce)
