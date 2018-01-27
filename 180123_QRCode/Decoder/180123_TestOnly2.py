# Ref: http://pyqrcode.sourceforge.net/


import sys, qrcode, pyqrcode

picPath = 'C:\\Users\\Aaron.Zheng\\Desktop\\Reading PDF\\BackUpSpace\\Self-Learning\\ProgramCode\\Python\\InstallsPackage\\QRPic.jpg'

d = qrcode.Decoder()

if d.decode(picPath):
    print('result\: ' + d.result)
else:
    print('error: ' + d.error)

# cc = pyqrcode.QRCode(picPath)

# print(cc)
# print(cc.data)



