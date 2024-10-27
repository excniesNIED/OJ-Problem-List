import os
import shutil
import re

# 定义根目录
root_dir = 'D:\\LERNAS\\BOT211\\OJ\\Selected\\大一第二周考试'

# 遍历根目录下的所有文件夹
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)

    # 检查是否是文件夹
    if os.path.isdir(folder_path):
        # 使用正则表达式检查文件夹名称是否为数字
        if re.match(r'^\d+$', folder_name):
            # 定义zip文件的路径
            zip_file_path = os.path.join(root_dir, f"{folder_name}.zip")

            # 打包数字命名的文件夹中的所有文件
            shutil.make_archive(os.path.splitext(zip_file_path)[0], 'zip', folder_path)

            print(f"已打包文件夹: {folder_name} 到 {zip_file_path}")
        else:
            print(f"文件夹 {folder_name} 不是数字命名的文件夹")