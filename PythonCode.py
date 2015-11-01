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
try:
    data = response.read() 
    print callback + "(" + json.dumps(data)+ ")"
finally:
    response.close()
