Announcement-Bot
================

A simple Pyhton script. It parses the Holy Ghost Prep announcements and emails the user if a string from a "properties" file is found.

How to use
==========

Put the python script and the properties file in a location that will run the script once a day (through windows task scheduler or otherwise).
- The properties file is *REQUIRED*
- The properties file is *NOT* case sensitive
- The properties file should have one entry per line
	- There should be no other punctuation/text
- Do not forget to replace the receiving email. (Line 38)
- The SMTP account areas (server, port, username, password) have been left blank, you need to update them in order to receive emails.
	- I used SMTPcorp.com as a free SMTP service (email server)

