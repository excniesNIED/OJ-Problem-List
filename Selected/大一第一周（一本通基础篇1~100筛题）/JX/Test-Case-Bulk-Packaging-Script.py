import os
import shutil

# 定义根目录
root_dir = '/media/excnies/Data/LERNAS/BOT211/OJ/Selected/大一第一周/JX'

# 遍历根目录下的所有文件夹
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)

    # 检查是否是文件夹
    if os.path.isdir(folder_path):
        # 查找名为data的子文件夹
        data_folder_path = os.path.join(folder_path, 'data')

        # 检查data文件夹是否存在
        if os.path.exists(data_folder_path):
            # 定义zip文件的路径
            zip_file_path = os.path.join(root_dir, f"{folder_name}.zip")

            # 打包data文件夹中的所有文件
            shutil.make_archive(os.path.splitext(zip_file_path)[0], 'zip', data_folder_path)

            print(f"已打包文件夹: {folder_name} 到 {zip_file_path}")
        else:
            print(f"文件夹 {folder_name} 中没有找到 data 文件夹")