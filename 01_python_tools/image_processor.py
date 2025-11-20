from PIL import Image

class ImageProcessor:
    def __init__(self):
        self.img = None

    def load(self, img_path):
        self.img = Image.open(img_path)
        print("图像已加载")

    def display(self):
        if self.img:
            self.img.show()
        else:
            print("请先加载图像")

    def save(self, save_path):
        if self.img:
            self.img.save(save_path)
            print(f"已保存到：{save_path}")
        else:
            print("请先加载图像")

# 调用
processor = ImageProcessor()
processor.load("test.jpg")
processor.display()
processor.save("new_test.png")
