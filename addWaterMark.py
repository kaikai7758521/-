import os,traceback
from PIL import Image


# 获取文件夹图片,并给每个图片添加水印
def get_folder(fpath, wm_file, whiteBlock, save_path):
    try:
        img_suffix_list = ['png', 'jpg', 'bmp']
        for i in os.listdir(fpath):
            if i.split('.')[-1] in img_suffix_list:
                img_path = fpath + '/' + i
                img_water_mark(img_path,wm_file, whiteBlock,save_path)


    except Exception as e:
        print(traceback.print_exc())

# 图片添加水印
def img_water_mark(img_file, icon, save_path):
    try:
        img = Image.open(img_file)  # 打开图片
        watermarkIcon = Image.open(icon)  # 打开水印
        img_size = img.size
        wm_size_icon = watermarkIcon.size
        # 如果图片大小小于水印大小
        if img_size[0] < wm_size_icon[0]:
            watermarkIcon.resize(tuple(map(lambda x: int(x * 0.5), watermarkIcon.size)))
        print('图片大小：', img_size)
        wm_position_icon = (img_size[0]-wm_size_icon[0],img_size[1]-wm_size_icon[1]) # 默认设定水印位置为右下角
        layer = Image.new('RGBA', img.size)  # 新建一个图层
        layer.paste(watermarkIcon, wm_position_icon)  # 将水印图片添加到图层上
        mark_img = Image.composite(layer, img, layer)
        new_file_name = '/new_'+img_file.split('/')[-1]
        mark_img.save(save_path + new_file_name)
    except Exception as e:
        print(traceback.print_exc())

#测试用
if __name__ == '__main__':
    img_water_mark(r"test/test.jpg", r"waterMark/waterMark",  "test")