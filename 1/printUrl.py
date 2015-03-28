import urllib2  
response = urllib2.urlopen('http://wb.weiyin.cc/Book/BookView/W440164363452#18')  
html = response.read()  
print html
