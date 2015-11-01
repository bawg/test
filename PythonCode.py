#!/usr/bin/python 

# Import modules for CGI handling 
import cgi, cgitb 
import urllib2 
import json

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

#download data from request parameter 'url' 
print "Content-type:text/javascript\r\n\r\n" 
url = form.getvalue("url") 
callback = form.getvalue("callback")
req = urllib2.Request(url) 
response = urllib2.urlopen(req) 
import ctypes  # An included library with Python install.
ctypes.windll.user32.MessageBoxA(0, "Your text", "Your title", 1)

try:
    data = response.read() 
    print callback + "(" + json.dumps(data)+ ")"
finally:
    response.close()
