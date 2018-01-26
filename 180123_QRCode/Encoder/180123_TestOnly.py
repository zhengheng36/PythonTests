## Test how to use the install package
## Ref: https://github.com/lincolnloop/python-qrcode
## 需要安装 廖雪峰 说的 集成第三方库 Pillow： Ref： https://pypi.python.org/pypi/Pillow/. Pillow 已经安装到工作时候的计算机

picPath = 'C:\\Users\\Aaron.Zheng\\Desktop\\Reading PDF\\BackUpSpace\\Self-Learning\\ProgramCode\\Python\\InstallsPackage\\QRCode.jpg'

####################################################################################
## WEBSITE --> QRCode
####################################################################################

# KEY: 'qrcode' package
# import qrcode
# ####img = qrcode.make('www.baidu.com')
# img = qrcode.make('http://www.baidu.com') # KEY: must have 'http://' in the front, otherwise it will not dump to the website
# img.show()

## KEY: 'pyqrcode' packege
# import pyqrcode
# qr = pyqrcode.create("http://www.baidu.com")
# qr.png(picPath, scale=6)


