####################################################################################
## 180118_Ad4_IsGroupChat
## Ref: http://www.cnblogs.com/yanjingnan/p/6831464.html
####################################################################################

import itchat

####################################################################################

####################################################################################
## Main Entry
####################################################################################

from itchat.content import TEXT

## KEY: all the members are used only when 'isGroupChat=True' 
@itchat.msg_register(TEXT, isGroupChat=True)
def print_content(msg):
    print(msg.isAt)
    print(msg.actualNickName)
    print(msg.text)


# Log in
if False:
    itchat.auto_login(enableCmdQR=2)    # Exectue for the first time 
else: 
    itchat.auto_login(hotReload=True)   # Exectue for the rest of times


# Start itchat machine: Keep the machine runing whitout stop
itchat.run()

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
############END#####################################################################


