import re
import urllib
import os
sort=[]
url=[]
f=open('animal_code.google.com','r')
texts=re.findall('GET\s[/\w-]+.jpg',f.read())
for text in texts:
  text=text[4:]
  text='http://code.google.com'+text
  sort.append(text)
i=0
sort.sort()
for item in sort:
  if len(url)==0 or item!=url[-1]:
    url.append(item)
index=open('index.html','w')
index.write('<verbatim><html><body>')
for t in url:
  img='img%d'%i
  print 'retrieving...',t
  u=urllib.urlretrieve(t,os.path.join(os.path.basename(os.path.abspath('animal')),img))
  i+=1
  index.write('<img src="%s">'%(os.path.join(os.path.abspath('animal'),img)))
index.write('</body></html>')
index.close()
  

