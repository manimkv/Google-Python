import re
d={}
w=[]
i=0
f=open('alice.txt','r')
l=re.findall(r'[\w\d]+',f.read())
for word in l:
  d[word]=0
for word in l:
  if word in d:
    d[word]+=1
sort=sorted(d.keys())
for wrd in sort:
  print sort[i],  d[wrd]
  i+=1  
