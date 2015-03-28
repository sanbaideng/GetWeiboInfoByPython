from bs4 import BeautifulSoup
import json
import ConfigParser
import urllib2

from util import get_content

link_id = 18

cf = ConfigParser.ConfigParser()
cf.read("config.ini")

weiyinUrl = 'http://wb.weiyin.cc/Book/BookView/W440164363452#' + str(link_id)

content = urllib2.urlopen(weiyinUrl)
html = content.read()

soup = BeautifulSoup(html)

weibo = soup.find("div",attrs="head_title").find("p").text
print html
print weibo
