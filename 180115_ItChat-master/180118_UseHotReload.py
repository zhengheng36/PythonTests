## The Correct way of using it is:
##      use auto_login for the first time, without hotReload
##      for the rest of times, use hotReload, without auto_login

import itchat

if False:
    itchat.auto_login(enableCmdQR=2)    # Exectue for the first time 
else: 
    itchat.auto_login(hotReload=True)   # Exectue for the rest of times

itchat.run()


## The way of logging and starting itchat machine have been added into 000000_BasicStrcut