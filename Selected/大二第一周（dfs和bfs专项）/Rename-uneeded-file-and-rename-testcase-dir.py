import os
import shutil

# 定义根目录
root_dir = r'your_root_directory_path'

# 遍历所有子目录
for subdir, dirs, files in os.walk(root_dir):
    # 检查是否存在data文件夹
    data_dir = os.path.join(subdir, 'data')
    if os.path.exists(data_dir):
        # 将data文件夹重命名为testcase
        testcase_dir = os.path.join(subdir, 'testcase')
        os.rename(data_dir, testcase_dir)

    # 删除除了problem.json以外的所有文件
    for file in files:
        if file != 'problem.json':
            file_path = os.path.join(subdir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

print("操作完成")