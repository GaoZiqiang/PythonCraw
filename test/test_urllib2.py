
from M2Crypto import urllib2
import cookielib


url = "http://www.baidu.com"

print '------the first method------'    
response =  urllib2.urlopen(url)

print response.getcode()
print len(response.read())

print '------the second method------'
#request = urllib2.Request(url)
reponse2 = urllib2.urlopen(url)

print '------the third method------'
cj = cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2)
