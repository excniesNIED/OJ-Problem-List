import os
import re

def rename_files_in_directory(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以 .ans 结尾
        if filename.endswith('.ans'):
            # 构建新的文件名，将 .ans 替换为 .out
            new_filename = filename.replace('.ans', '.out')
            # 构建完整的文件路径
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')
        # 检查文件是否包含数字前缀
        elif re.match(r'problem\d+\.in', filename) or re.match(r'problem\d+\.out', filename):
            # 构建新的文件名，删除前缀 "problem"
            new_filename = re.sub(r'problem(\d+)\.', r'\1.', filename)
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
root_directory = '/media/excnies/Data/LERNAS/BOT211/OJ/Selected/大一第一周/JX'
process_directories(root_directory)