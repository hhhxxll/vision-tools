import os #管理电脑环境
import sys #管python

def show_menu():
    while True: # 死循环，一直显示菜单
        print("\n" + "=" * 40)
        print("工业视觉工具箱")
        print("=" * 40)
        print("1. [重命名] 批量修改文件名")
        print("2. [统计] 查看数据集分布")
        print("3. [清理] 删除损坏的图片")
        print("4. [信息] 统计文件夹大小")
        print("q. 退出")
        print("-" * 40)

        choice = input("👉 请输入功能序号: ").strip()

        if choice == '1':
            print("\n 正在启动重命名工具...")
            # 这里的 python batch1_rename.py 就是在调用你刚才改名后的文件
            os.system("python batch1_rename.py")

        elif choice == '2':
            print("\n 正在启动数据统计...")
            os.system("python dataset2_stats.py")

        elif choice == '3':
            print("\n🧹 正在启动坏图清理...")
            os.system("python remove3_corrupt_images.py")

        elif choice == '4':
            print("\nℹ 正在统计文件夹信息...")
            os.system("python folder4_info.py")

        elif choice == 'q':
            print(" 再见！")
            break # 退出循环
        else:
            print(" 输入无效，请重试")

if __name__ == "__main__":
    # 这行代码保证了无论你在哪运行，都能找到旁边的脚本
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    show_menu()