import os

def batch_rename_images(folder_path, prefix="image_"):
    # 定义常见图片格式的后缀
    image_ext = ('.jpg', '.png', '.bmp')
    # 筛选出文件夹中后缀符合的图片文件
    image_files = [
        f for f in os.listdir(folder_path)
        if f.endswith(image_ext)]

    # 遍历图片文件，按序号重命名
    for idx, old_name in enumerate(image_files, start=1):
        # 拆分文件名和后缀
        name_part, ext_part = os.path.splitext(old_name)
        # 构造新文件名，格式为“前缀+序号+后缀”
        new_name = f"{prefix}{idx}{ext_part}"
        # 拼接旧文件和新文件的完整路径
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        # 执行重命名操作
        os.rename(old_path, new_path)
        print(f"重命名完成：{old_name} → {new_name}")

# 调用函数，替换为你的图片文件夹路径，可自定义前缀
if __name__ == "__main__":
    target_folder = "images"
    batch_rename_images(target_folder, prefix="cat")