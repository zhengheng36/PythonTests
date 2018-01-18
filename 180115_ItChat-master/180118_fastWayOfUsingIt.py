import itchat

####################################################################################
## Example 1: Send msg to myself by FileHelper
####################################################################################

# itchat.auto_login()

# itchat.send('This message send by Aaron.Zheng itchat Testing', toUserName='filehelper')

####################################################################################
## Example 2: Auto replay msg settings
####################################################################################

# @itchat.msg_register(itchat.content.TEXT)
# def text_reply(msg):
#     return '抱歉，我现在有事不在，我回尽快答复，谢谢...'

# itchat.auto_login()
# itchat.run()

####################################################################################
## Example 3: show QR in cmd window instead of open a new pic 
####################################################################################

## no work for windows
#itchat.auto_login(enableCmdQR=True)
#itchat.auto_login(enableCmdQR=-1)

# woring version
itchat.auto_login(enableCmdQR=2)

####################################################################################
## Example 4: no need to re-log-in for a while after scaning QR
####################################################################################

## itchat.auto_login(hotReload=True)

####################################################################################
## Example 5: getting user info
####################################################################################

# 获取自己的用户信息，返回自己的属性字典
# dicSelfInfo = itchat.search_friends()
# print(dicSelfInfo)
# print()

# dicSpecialNameInfo = itchat.search_friends(name='\'\'真的')
# print(dicSpecialNameInfo)
# print()

# dicDeDaoInfo = itchat.search_friends(wechatAccount='得到')
# print(dicDeDaoInfo)
# print()

####################################################################################
## Example 6: getting all friends info at once: ref https://mp.weixin.qq.com/s?__biz=MzI0MzE5MTgzMw==&mid=503957331&idx=1&sn=6f40b888b7a06af7a2174a2dea0c7a9c&chksm=728dbe2545fa3733b4ff01b15b0b28ad40eeebba448e6e9ebd79152ce3756df4bc112dc4cc07&mpshare=1&scene=1&srcid=0111hiu56MncnJtG3m7TUoll&pass_ticket=Rsbpu0dLM3VSfIi8578YR4u2NNXlbHnOcWHetLUGvDnES3qgybcSu5G%2FTyYZ9eAy#rd
####################################################################################

friends = itchat.get_friends(update=True)[0:]

#friends[0] is my personal info, should begin with friends[1]
male = 0
female = 0
unknowSex = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male = male + 1
    elif sex == 2:
        female = female + 1
    else:
        unknowSex = unknowSex + 1

totalFrinds = len(friends[1:])
print(male)
print(female)
print(unknowSex)
print("Male: %.2f%%" % (float(male)/totalFrinds*100)) # KEY: we will never know the crash until we execute this line
print("Female: %.2f%%" % (float(female)/totalFrinds*100)) 
print("Unknow: %.2f%%" % (float(unknowSex)/totalFrinds*100))


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

### Info Referece as Dictionary: 
# {'MemberList': <ContactList: []>, 
# 'UserName': '@f131ffe51e38a97541984da4d11f1832', 
# 'City': '厦门', 'DisplayName': '', 
# 'PYQuanPin': 'Aaron', 
# 'RemarkPYInitial': '', 
# 'Province': '福建', 
# 'KeyWord': 'zhe', 
# 'RemarkName': '', 
# 'PYInitial': 'AARON', 
# 'EncryChatRoomId': '', 
# 'Alias': '', 
# 'Signature': '长脖脖小胖', 
# 'NickName': 'Aaron', 
# 'RemarkPYQuanPin': '', 
# 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=674736448&username=@f131ffe51e38a97541984da4d11f1832&skey=@crypt_f5c4783e_f97e06e57a5475ba714d735ecaa27a6f', 
# 'UniFriend': 0, 
# 'Sex': 1, 
# 'AppAccountFlag': 0, 
# 'VerifyFlag': 0, 
# 'ChatRoomId': 0, 
# 'HideInputBarFlag': 0, 
# 'AttrStatus': 33914915, 
# 'SnsFlag': 49, 
# 'MemberCount': 0, 
# 'OwnerUin': 0, 
# 'ContactFlag': 1, 
# 'Uin': 274688315, 
# 'StarFriend': 0, 
# 'Statues': 0, 
# 'WebWxPluginSwitch': 0, 
# 'HeadImgFlag': 1, 
# 'IsOwner': 0}


