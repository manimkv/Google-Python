import re
res=[]
f=open('baby1990.html','r')
ff=f.read()
match=re.search(r'Popularity\sin\s(\d\d\d\d)',ff)
yr=match.group(1)
res.append(yr)
table=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',ff)
d={}
for items in table:
  (rank,male,female)=items
  if male not in d:
    d[male]=rank
  if female not in d:
    d[female]=rank
s=sorted(d)
for p in s:
  res.append(p+" "+d[p])
print res    
