import re
regex = "\?"
url = "http://sdf.jj.edu/22-calendar-32/sdflkj"
match = re.search(regex, url)
print match
print url[-1]