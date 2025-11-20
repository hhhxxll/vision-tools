import os
from glob import glob #glob模块用于搜索目录中的文件

class ImageLoader: #class是定义类
    def __init__(self, root_dir): #__init__是类的构造函数，用于初始化类的实例,root_dir是图像文件的根目录,self是类的实例
        self.root_dir = root_dir
        # 将传入的根目录路径参数 root_dir，赋值给实例变量 self.root_dir。
        # 这样每个实例对象都能记住其对应的图像文件根目录路径，
        # 方便后续在类的其他方法中基于该路径进行操作，如搜索图像文件。
        self.image_paths = []
        # 创建并初始化一个空列表作为实例变量 self.image_paths。
        # 此列表用于存储在指定根目录及其子目录下找到的图像文件路径，
        # 后续类中的方法会基于这个列表进行操作，如筛选路径或获取所有路径。

    def load_all_images(self, extensions=['.jpg', '.png', '.jpeg']):#定义方法load_all_images，用于从指定根目录及其子目录下搜索所有图像文件。

        for ext in extensions:#遍历每个扩展名，搜索对应图像文件
            paths = glob(os.path.join(self.root_dir, '**', f'*{ext}'), recursive=True)#构建路径模式并搜索，recursive=True确保递归子目录
            self.image_paths.extend(paths)# 将找到的路径添加到存储列表
        print(f"已加载 {len(self.image_paths)} 张图像")

    def filter_by_keyword(self, keyword):
        filtered = [path for path in self.image_paths if keyword in path]# 筛选出路径含有关键词的图像路径
        print(f"包含关键词「{keyword}」的图像有 {len(filtered)} 张")
        return filtered# 返回筛选后的路径列表

    def get_image_paths(self):
        return self.image_paths

if __name__ == '__main__':
    loader = ImageLoader(root_dir=r'D:\pycharm\stuady\images')# 创建ImageLoader实例，指定图像根目录
    loader.load_all_images()# 加载目录下所有指定格式图像路径
    cat_images = loader.filter_by_keyword('cat')# 筛选路径含'cat'的图像路径
    all_paths = loader.get_image_paths()# 获取所有加载的图像路径
