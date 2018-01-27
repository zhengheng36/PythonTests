### Ref: https://github.com/oostendo/python-zxing


import zxing

picPath = 'C:\\Users\\Aaron.Zheng\\Desktop\\Reading PDF\\BackUpSpace\\Self-Learning\\ProgramCode\\Python\\InstallsPackage\\QRPic.jpg'

reader = zxing.BarCodeReader("/var/opt/zxing")

barcode = reader.decode("C:\\Users\\Aaron.Zheng\\Desktop\\Reading PDF\\BackUpSpace\\Self-Learning\\ProgramCode\\Python\\InstallsPackage\\QRPic.jpg")
# (barcode1, barcode2) = reader.decode(["/tmp/1.png", "/tmp/2.png"])
# code_list = reader.decode("/tmp/barcodes", True)

## Failed



