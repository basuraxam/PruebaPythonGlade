import urllib2

url = 'http://www.google.es'

response = urllib2.urlopen(url)
webContent = response.read()

with open('./datos/diffcompgooglehtml.txt', 'w') as file_out:
    file_out.write(webContent)

#print(webContent[0:300000])
