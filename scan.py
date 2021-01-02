from PIL import Image
import numpy

img = Image.open("test.jpg")
w,h = img.size ##顯示像素大小 寬和高
outfile = open("outfile.txt","w")

blackwhiteImg =img.convert("1") ##轉換成黑白照片
#blackwhiteImg .save(''blackwhiteImg .jpg'') ##保存黑白照片
###通過設置閥值，生成一個查找表（lut）
threshold = 80
lut= []

for i in range( 256 ): ## 範圍：0-255
    if i < threshold:
        lut.append(0)
    else :
        lut.append( 1 )

binaryImg = blackwhiteImg.convert(lut,"1") ## 根據查找表，將黑白照片轉換為二進位照片
binaryImg.save("binary.jpg")

### 獲取每個像素點的像素值

pixels = [ (x,y) for x in range(w) for y in range(h) ] ##獲取每一個像素點的坐標
pixelVal = [] ##每個像素點對應的值

for point in pixels:
    value = binaryImg.getpixel(point)
    pixelVal.append(value)

### 將以為數組轉化為二維數組，便於分析

biArray = numpy.array(pixelVal).reshape(w,h) 

for x in range(w):
    for y in range(h):
        if biArray[w][h] == 1:
            outfile.write("do Screen.Drawpixel","(",(w,h),")")

