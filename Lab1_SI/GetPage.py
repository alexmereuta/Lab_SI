#plss dont read this
import urllib2
import urllib

# Specify the url
url = 'http://www.999.md'

# This packages the request (it doesn't make it)
request = urllib2.Request(url)

# Sends the request and catches the response
response = urllib2.urlopen(request)

# Extracts the response
html = response.read()

# Print it out
print html
