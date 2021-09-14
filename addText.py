
from PIL import Image,ImageDraw
from PIL import ImageFont

#添加水印文字，根据需求修改和添加内容
def add(text, fileName, savePath):
    font1 = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc', 72)
    font1 = ImageFont.truetype(font1, 72)
    text = '经纬度143.1546°E  56.1667°N'

    watermark = Image.open(fileName)
    img_size = watermark.size
    drawObj = ImageDraw.Draw(watermark)
    # 　设置 文字位置 文字内容 颜色 文字大小
    wm_position = (335,img_size[1]-600)
    drawObj.text(wm_position, text, 'black', font=font1)
    i = 0
    watermark.save(savePath + "new_" +fileName)