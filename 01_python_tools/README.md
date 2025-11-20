# Python Vision Tools (Week 1)

这是我开始学习工业视觉算法的第一周练习代码。
主要包含了一些常用的数据预处理脚本，用于解决工业质检中常见的数据杂乱问题。

## 📂 功能列表

| 脚本名称 | 功能描述 |
| :--- | :--- |
| **main_menu.py** | **[主程序]** 整合了以下所有功能的控制台菜单 |
| `batch_rename.py` | **批量重命名**：将杂乱的文件名统一修改为 `image_01.jpg` 格式 |
| `dataset_stats.py` | **数据统计**：自动统计文件夹下 .jpg/.png 的数量分布 |
| `remove_corrupt_images.py` | **坏图清洗**：利用 OpenCV 自动检测并删除损坏的图片 |
| `folder_info.py` | **空间统计**：快速计算文件夹占用的磁盘大小 |

## 🚀 如何使用

1. 确保已安装必要的库：
   ```bash
   pip install opencv-python numpy
