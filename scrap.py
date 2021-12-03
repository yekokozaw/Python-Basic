import re,urllib
from typing import Text
import urllib.request

web_url = "http://www.google.com"

u = urllib.request.urlopen(web_url)
text = str(u.read())
#print(text) 

title = re.findall("<title>.*</title>", text)
print("Title",title)