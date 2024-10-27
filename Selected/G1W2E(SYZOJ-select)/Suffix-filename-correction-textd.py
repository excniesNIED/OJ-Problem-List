import os
import re

def rename_files_in_directory(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否匹配 input\d+\.txt 模式
        if re.match(r'input\d+\.txt', filename):
            # 构建新的文件名，将 input\d+\.txt 替换为 \d+\.in
            new_filename = re.sub(r'input(\d+)\.txt', r'\1.in', filename)
            # 构建完整的文件路径
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

        # 检查文件名是否匹配 output\d+\.txt 模式
        elif re.match(r'output\d+\.txt', filename):
            # 构建新的文件名，将 output\d+\.txt 替换为 \d+\.out
            new_filename = re.sub(r'output(\d+)\.txt', r'\1.out', filename)
            # 构建完整的文件路径
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

def process_directories(root_directory):
    # 遍历根目录下的所有文件夹
    for foldername in os.listdir(root_directory):
        folder_path = os.path.join(root_directory, foldername)
        # 检查是否是文件夹
        if os.path.isdir(folder_path):
            data_folder_path = os.path.join(folder_path, 'data')
            # 检查是否存在 data 文件夹
            if os.path.isdir(data_folder_path):
                rename_files_in_directory(data_folder_path)

# 指定根目录
root_directory = 'your_root_directory_path'
process_directories(root_directory)