
import urllib2

url = 'http://www.google.es'

response = urllib2.urlopen(url)
webContent = response.read()

#print(webContent[0:10000000])

contenido = webContent[0:10000000]
print(contenido)

with open('./datos/googlecom.txt', 'r') as file1:
        #print(file1.read())    
        if file1.read() == contenido:
            print ("iguales")
        else:
            print ("diferente")

#with open('./datos/diffgoogle.txt', 'w') as file_out:
#    for line in difference:
#        file_out.write(line)





