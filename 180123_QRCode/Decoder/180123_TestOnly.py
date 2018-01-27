## Ref: https://github.com/ewino/qreader

####################################################################################
## IMAGW --> WEBSITE
####################################################################################

picPath = 'C:\\Users\\Aaron.Zheng\\Desktop\\Reading PDF\\BackUpSpace\\Self-Learning\\ProgramCode\\Python\\InstallsPackage\\QRPic.jpg'

## KEY: open img from path
from PIL import Image
import qreader

img2 = Image.open(picPath)
##img2.show()

data = qreader.read(img2)

### Can NOT work



