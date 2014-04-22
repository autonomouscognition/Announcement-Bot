Announcement-Bot
================

A simple Pyhton script. It parses the Holy Ghost Prep announcements and emails the user if a string from a "properties" file is found.

How to use
==========

Put the python script and the properties file in a location that will run the script once a day (through windows task scheduler or otherwise).
- The properties file is *REQUIRED*
- The properties file is *NOT* case sensitive
- The properties file should have one entry to look for per line
	- There should be no other punctuation/text
