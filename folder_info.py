import os

def count_images(folder_path):
    total_size = 0
    count = 0
    # 遍历文件夹
    for file in os.listdir(folder_path):
        if file.endswith(('.jpg', '.png', '.bmp')):
            count += 1
            total_size += os.path.getsize(os.path.join(folder_path, file))
    print(f"图像数量：{count}")
    print(f"总大小：{total_size/1048576:.2f}MB")

# 调用：替换为你的图像文件夹路径
count_images("images")
