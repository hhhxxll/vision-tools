from PIL import Image

def get_image_info(img_path):
    with Image.open(img_path) as img:
        print(f"图像路径：{img_path}")
        print(f"尺寸：{img.width}×{img.height}")
        print(f"像素格式：{img.mode}")
        print(f"文件格式：{img.format}")

# 调用
get_image_info("test.jpg")