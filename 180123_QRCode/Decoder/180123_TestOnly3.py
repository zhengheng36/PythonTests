## REf: https://github.com/primetang/qrtools

import qrtools
from qrtools.qrtools import QR

picPath = 'C:\\Users\\Aaron.Zheng\\Desktop\\Reading PDF\\BackUpSpace\\Self-Learning\\ProgramCode\\Python\\InstallsPackage\\QRPic.jpg'

qr = qrtools.QR()
qr.decode(picPath)
print(qr.data)

### Can NOT work because of it ned Zbar bar code reader from http://zbar.sourceforge.net/download.html, which can not be used after downlaoding
###