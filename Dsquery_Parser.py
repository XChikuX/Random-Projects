import subprocess
import re
'''WORKING LDAP, Just replace LDAP with your input
Proc = subprocess.Popen(["w32tm", "/ntte", LDAP], stdout=subprocess.PIPE )
out, err = Proc.communicate()
print (out) ############LDAP Stored in 'out'
'''
USERS = [["SAM_NORMAL_USER_ACCOUNT",	805306368],
["SAM_GROUP_OBJECT",	268435456],
["SAM_MACHINE_ACCOUNT",	805306369],
["SAM_ALIAS_OBJECT",	536870912],
["SAM_NON_SECURITY_GROUP_OBJECT",	268435457],
["SAM_NON_SECURITY_ALIAS_OBJECT",	536870913],
["SAM_TRUST_ACCOUNT",	805306370],
["SAM_APP_BASIC_GROUP",	1073741824],
["SAM_APP_QUERY_GROUP",	1073741825],
["SAM_ACCOUNT_TYPE_MAX",	2147483647]
]

##################PART1############################
B=[]
f1 = open("Attempt2.txt","w")
with open("Sample.txt","r") as f:
    for line in f:
        B.append(re.split(r' {4,}', line.strip()))
mylist = []
for i in range(len(B)):
  
    f1.write("\n"+ str(B[i]))
    mylist.append(B[i])
#################PART1#################################    
    

for obj in mylist:
  ct=0    
  for items in obj:
    ct+=1
    #if (ct==2):
    try:
      for stuff in USERS:
        print (stuff)
        for i in range(len(mylist)):
          if(float(mylist[i][1])==stuff[1]):
            mylist[i][1]=obj[0]
    except ValueError:
      pass#print ("Not a float")
            
######################################EXCEL IMPORT!! GO!##################################################
import csv

fl = open('DS_Query_SP.csv', 'w')

writer = csv.writer(fl)
#writer.writerow(['label1', 'label2', 'label3']) #if needed
for values in mylist:
    writer.writerow(values)
    
writer.writerow(["WARNING!!! Many of these Values Will have misplaced Entries. This is due to the fact Original Command Output has too many Spacing Errors.\n Tread Carefully While Using it for Auditing Purposes"])

fl.close()
#######################################EXCEL IMPORT!! STOP!###############################################
#print (max(mylist, key=len))
#print (mylist)