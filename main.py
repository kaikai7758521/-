import os

from readDir import readFileName
from addWaterMark import get_folder

def go(picPath, dataPath, savePath):
    #得到文件夹名字数组
    fileNames = readFileName(picPath)

    for i in range(40):
        os.mkdir(savePath + str(i + 1))
    for i in range(40):
        filePath = picPath + "\\"
        get_folder(filePath + fileNames[i], "水印\水印.png", "水印\白块2.png", savePath + fileNames[i])


if __name__ == '__main__':
    go("pic", "location\地点经纬度.txt", "done\\")