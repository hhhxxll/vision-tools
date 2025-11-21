import argparse
import logging
import os
import cv2  # 引入 OpenCV

# 1. 日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)


def process_images(input_dir, output_dir, target_size):
    # 如果输出文件夹不存在，就自动创建一个
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logging.info(f"新建输出目录: {output_dir}")

    # 获取文件夹里所有的文件名
    # os.listdir 会返回一个列表，比如 ['a.jpg', 'b.png']
    file_list = os.listdir(input_dir)

    count = 0  # 计数器，用来给图片编号 (001, 002...)

    logging.info(f"找到 {len(file_list)} 个文件，开始处理...")

    for filename in file_list:
        # 1. 拼凑完整的图片路径 (例如: ../images/a.jpg)
        old_path = os.path.join(input_dir, filename)

        # 2. 读取图片
        img = cv2.imread(old_path)

        # 检查: 如果读出来是 None，说明这不是图片或者图片坏了，直接跳过
        if img is None:
            logging.warning(f"无法读取文件 (可能不是图片): {filename}")
            continue

        # 3. 缩放图片 (Resize)
        # 工业常用: 把图片统一缩放到 640x640，方便喂给 AI
        img_resized = cv2.resize(img, (target_size, target_size))

        # 4. 生成新名字 (关键点: 补零操作!)
        # :03d 表示: 变成3位数，不够补0 (例如 1 -> data_001.jpg)
        new_name = f"data_{count:03d}.jpg"
        new_path = os.path.join(output_dir, new_name)

        # 5. 保存图片
        cv2.imwrite(new_path, img_resized)

        logging.info(f"处理完成: {filename} -> {new_name}")

        count += 1  # 处理完一张，计数器加1

    logging.info("--------------------------------")
    logging.info(f"全部搞定！共处理了 {count} 张图片。")


def main():
    parser = argparse.ArgumentParser(description="图片预处理工具")
    parser.add_argument('--input', required=True, help=r'D:\pycharm\stuady\images')
    parser.add_argument('--output', default='./output', help='输出文件夹')
    parser.add_argument('--size', type=int, default=640, help='缩放尺寸')

    args = parser.parse_args()

    logging.info(">>> 任务开始")
    logging.info(f"输入: {args.input}")
    logging.info(f"输出: {args.output}")

    # 调用上面的干活函数
    process_images(args.input, args.output, args.size)


if __name__ == '__main__':
    main()