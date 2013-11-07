import sys
import re
import shutil
import commands
import os
z=' '
files=os.listdir('items')
for file in files:
  match=re.search('\w+_\w+_.\w+',file)
  p=os.path.join('items',match.group())
  q=os.path.abspath(p)
  r=os.path.abspath('copy')
  shutil.copy(q,r)
  m=' '+q
  z=z+m
cmd='zip -j zipfile'+z
print'command iam going to do:'+cmd
(status,output)=commands.getstatusoutput(cmd)
if status:
  sys.stderr.write(output)
  sys.exit(1)
else:
   print output
