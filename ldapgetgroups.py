#!/usr/bin/env python

# Get ldap gropus and create group pages in MoinMoin wiki
import ldap,ldif, sys

#source https://www.packtpub.com/books/content/python-ldap-applications-part-1-installing-and-configuring-python-ldap-library-and-bin
server = 'ldaps://ldap.example.com/'
con = ldap.initialize(server)



bind_dn="somemail@example.com"
bind_pw="supersecretpassword"

base_dn="dc=ad,dc=example,dc=com"

con.simple_bind_s( bind_dn, bind_pw )

searchFilter = "(sAMAccountType=268435456)"
searchScope = ldap.SCOPE_SUBTREE


results = con.search_s(base_dn, ldap.SCOPE_SUBTREE, searchFilter)

#print type(results)





firstgroup = results[0][0].split(',')[0].split('=')[1]



grouplist = []
#print all groups

countere = 0
for grpelement in results:
   while countere < len(results) - 3 :
      reselement = results[countere][0].split(',')[0].split('=')[1]
      #print reselement
      grouplist.append(reselement)
      countere = countere + 1

#print grouplist


listofprohibiteddomains =  ['AdminsCreator Owners','Domain Computers',
                            'DnsUpdateProxy', 'Domain Admins','Domain Controllers','Enterprise Admins', 'Domain Users','JabberUsers']

#for prohibitedname in listofprohibiteddomains:
#   print prohibitedname
#   grouplist.remove(prohibitedname)

grouplistruncated = [x for x in grouplist if x not in listofprohibiteddomains]



# print the MEMBERS of first group of grouplistruncated



groupnameAndAlias = {}

#print len(grouplistruncated)

for memberindex in xrange(0, len(grouplistruncated)):

   memberetclist =  results[  grouplist.index( grouplistruncated[memberindex] )  ][1]


   memberlist = memberetclist['member']

   aliaslistofthisgroup = []

   for nameelement in memberlist:
       aliasname = nameelement.split(',')[0].split('=')[1].replace(" ", "")
       aliaslistofthisgroup.append(aliasname)

   #print aliaslistofthisgroup

   groupnameAndAlias.update({grouplistruncated[memberindex]:aliaslistofthisgroup })

#print groupnameAndAlias


#print len(groupnameAndAlias)
#
#print ; print groupnameAndAlias[grouplistruncated[0]]





#now create pages
# source pagecreate2.py

from MoinMoin.web.contexts import ScriptContext
from MoinMoin.PageEditor import PageEditor


import MoinMoin.user

def  createpage (groupname,groupmemberlist):

     request = ScriptContext('http://localhost:8080')

     user = MoinMoin.user.get_by_email_address(request,'someuser@example.com')
     request.user = user

     # Group name added at the end
     groupname = groupname + 'Group'
     pe = PageEditor(request, groupname)


     #memberlist =['Tom','Harry','Steph','Rama']
     memberlist = groupmemberlist
     mystring = ' * '
     mynewlist = ['#acl ItGroup:read,write,delete,revert,admin Known: All:'] + [ mystring + x for x in memberlist]

     mynewlist = '\n'.join(mynewlist)
     try:
         pe.saveText(mynewlist, 0)

     except pe.Unchanged:
         print "You did not change the page content, not saved!"


#Create ALL the group pages
for memberindex in xrange(0, len(grouplistruncated)):
   thisgroupname = grouplistruncated[memberindex]
   thisgroupmemberlist = groupnameAndAlias[grouplistruncated[memberindex]]
   createpage(thisgroupname,thisgroupmemberlist)
