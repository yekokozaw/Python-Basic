import re

my_str = "fool23bar"

print("Search ",re.search('[abc]',"helloa"))

print("Search ",re.search('1.3',"1S3")) 
print("Search ",re.search('1.3',"13AA")) 
#dot means any character

print("Search ",re.search('^Java',"JavaScript")) 
# ^ means start point of string

print("Search ",re.search('Java$',"CoffeeJava")) 
# $ means end of string

print("Search ",re.search('[a-z]*[1-5]*',"javascript22")) 
