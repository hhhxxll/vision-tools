import os   #系统交互功能模块
import glob #模块用于文件路径匹配，可以一次性查找符合特定模式的文件
from PIL import Image #PIL库中的Image模块用于处理图像文件

def delete_broken_images(folder_path):  # 定义函数，用于删除损坏的图像文件,参数folder_path为文件夹路径
    image_paths = glob.glob(os.path.join(folder_path, "*.jpg")) + glob.glob(os.path.join(folder_path, "*.png"))
    ''' 1.glob.glob函数搜索文件夹中所有jpg和png格式的图片文件
        2.os.path.join函数生成文件路径
        3.image_paths是一个包含所有图片文件路径的列表
    '''
    for path in image_paths:  # 遍历所有图片文件路径
        try:  # 尝试打开每个图片文件
            with Image.open(path) as img:
                img.verify()  # 检查图片完整性
            print(f"✅ {path} 是正常图片")
        except Exception as e:  # 捕获异常
            ''' with是上下文管理器，可以自动关闭文件，避免资源泄露
            Image.open函数打开图片文件，并返回一个Image对象,as img表示将img对象赋值给变量img
            img.verify()函数用于检查图片完整性
            '''
            os.remove(path)  # 删除损坏的图片文件
            print(f"❌ 已删除损坏图片：{path}（错误原因：{e}）")


# 调用函数：把这里改成你的图片文件夹路径
delete_broken_images(r"D:\pycharm\stuady\images")