import os

#遍历文件夹得到文件夹数组
def readFileName(path):
    names = os.listdir(path + "\\")
    return names
    # print(names)

#测试用
if __name__ == '__main__':
    readFileName("pic")