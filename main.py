import os
from readDir import readFileName
from addWaterMark import get_folder
'''
#执行主函数
picPath 需要批量加水印的图片文件夹，文件夹内包含了子文件夹，本次处理的是各个子文件夹内的图片
例如 E:/pic/1/a.png picPath="pic"
savePath 需要保存的路径
'''
def go(picPath, savePath):
    #得到文件夹名字数组
    fileNames = readFileName(picPath)
    #创建文件夹
    for i in range(40):
        os.mkdir(savePath + fileNames[i])
    #向已经创建的文件夹内保存修改的图片
    for i in range(40):
        filePath = picPath + "\\"
        get_folder(filePath + fileNames[i], "水印\水印.png", "水印\白块2.png", savePath + fileNames[i])

if __name__ == '__main__':
    go("pic", "done")