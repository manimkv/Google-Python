import re
import urllib
import os
sort=[]
url=[]
m=[]
f=open('place_code.google.com','r')
texts=re.findall('GET\s[/\w-]+.jpg',f.read())
for text in texts:
  text=text[4:]
  text='http://code.google.com'+text
  sort.append(text)
def d(s):
  match=re.search('\w+.jpg',s)
  m=match.group()
  m=m[:-4]
  return m
sort=sorted(sort,key=d)
for item in sort:
  if len(url)==0 or item!=url[-1]:
    url.append(item)
i=0
index=open('indexx.html','w')
index.write('<verbatim><html><body>')
for t in url:
  img='img%d'%i
  print 'retrieving...',t
  u=urllib.urlretrieve(t,os.path.join(os.path.basename(os.path.abspath('place')),img))
  index.write('<img src="%s">'%(os.path.join(os.path.abspath('place'),img)))
  i+=1
index.write('</body></html>')
index.close()
  

