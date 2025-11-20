import glob
import os

def count_image_classes(data_dir, formats=['.jpg', '.png', '.bmp', '.gif']):
    """
    统计数据集每个类别（文件夹）的图片数量
    :param data_dir: 数据集根目录
    :param formats: 要统计的图片格式（默认支持jpg、png、bmp、gif）
    :return: 字典{类别名: 图片数量}
    """
    # 检查路径是否存在且为文件夹
    if not os.path.exists(data_dir):
        raise ValueError(f"错误：路径 '{data_dir}' 不存在，请检查")
    if not os.path.isdir(data_dir):
        raise ValueError(f"错误：'{data_dir}' 不是文件夹，请传入目录")

    # 收集所有指定格式的图片路径（递归遍历子目录，不区分大小写）
    img_paths = []
    for fmt in formats:
        fmt_lower = fmt.lower()
        # 匹配小写格式
        pattern = os.path.join(data_dir, "**", f"*{fmt_lower}")
        img_paths.extend(glob.glob(pattern, recursive=True))
        # 匹配大写格式（避免遗漏）
        pattern_upper = os.path.join(data_dir, "**", f"*{fmt.upper()}")
        img_paths.extend(glob.glob(pattern_upper, recursive=True))

    # 没找到符合格式的图片时提示
    if not img_paths:
        print(f"警告：在 '{data_dir}' 中未找到{formats}格式的图片")
        return {}

    # 统计每个类别的图片数（类别为图片所在文件夹名，根目录下的图片归为“根目录”）
    class_count = {}
    for path in img_paths:
        class_dir = os.path.dirname(path)
        class_name = os.path.basename(class_dir)
        if not class_name:  # 处理根目录下的图片
            class_name = "根目录"
        class_count[class_name] = class_count.get(class_name, 0) + 1

    return class_count


if __name__ == "__main__":
    # 替换为你的数据集路径（例如："./dataset" 或 "D:/images"）
    dataset_path = r"D:\pycharm\stuady\images"

    try:
        result = count_image_classes(dataset_path)
        if result:
            print("图片类别数量统计结果：")
            # 按类别名排序输出
            for class_name in sorted(result.keys()):
                print(f"类别 '{class_name}'：{result[class_name]} 张图片")
    except Exception as e:
        print(f"程序执行出错：{e}")