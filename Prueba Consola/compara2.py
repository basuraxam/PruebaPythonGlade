
import urllib2

url = 'http://www.google.es'

response = urllib2.urlopen(url)
webContent = response.read()

#print(webContent[0:10000000])

with open('./datos/googlecom.txt', 'r') as file1:
        difference = set(file1).difference(webContent)

with open('./datos/diffgoogle.txt', 'w') as file_out:
    for line in difference:
        file_out.write(line)

