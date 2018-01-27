import itchat

itchat.auto_login()

itchat.send('This message send by Aaron.Zheng', toUserName='filehelper')

print()
itchat.auto_login(enableCmdQR=True)
print()