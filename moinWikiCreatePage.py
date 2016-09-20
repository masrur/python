#source http://stackoverflow.com/questions/5275856/moinmoin-1-9-programmatically-creating-page-error-moinmoin-pageeditor-accessden
#       and https://moinmo.in/MoinAPI/Examples#PageEditor.saveText.28.29



from MoinMoin.web.contexts import ScriptContext
from MoinMoin.PageEditor import PageEditor


import MoinMoin.user


request = ScriptContext('http://localhost:8080')

user = MoinMoin.user.get_by_email_address(request,'user@example.com')
request.user = user

pe = PageEditor(request, 'MyNewTestPageGroup')


memberlist =['Tom','Harry','Steph','Rama']
mystring = ' * '
mynewlist = ['#acl ItGroup:read,write,delete,revert,admin Known: All:'] + [ mystring + x for x in memberlist]

mynewlist = '\n'.join(mynewlist)


try:
    pe.saveText(mynewlist, 0)

except pe.Unchanged:
    print "You did not change the page content, not saved!"


