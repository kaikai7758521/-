import os

def readFileName(path):
    names = os.listdir(path + "\\")
    return names
    # print(names)

if __name__ == '__main__':
    readFileName("pic")