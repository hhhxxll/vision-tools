from PIL import Image
import os

def get_image_info(img_path):
    with Image.open(img_path) as img:
        print(f"图像路径：{img_path}")
        print(f"尺寸：{img.width}×{img.height}")
        print(f"像素格式：{img.mode}")
        print(f"文件格式：{img.format}")


def image_generator(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(('.jpg', '.png')):
            yield os.path.join(folder_path, file)

# 调用：逐个处理图像
for img_path in image_generator("images"):
    print("当前图像：", img_path)
    get_image_info(img_path)  # 调用上面的信息函数