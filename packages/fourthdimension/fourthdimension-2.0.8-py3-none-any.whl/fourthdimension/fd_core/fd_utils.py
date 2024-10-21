import os
import threading
import time


def get_all_file_paths(directory):
    # 存储所有文件的绝对路径
    file_paths = []

    # 遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 获取文件的绝对路径
            file_path = os.path.abspath(os.path.join(root, file))
            if (file_path.endswith(".docx") or file_path.endswith(".pdf") or file_path.endswith(".pptx")) and ".~" not in file_path:
                file_paths.append(file_path)

    return file_paths
def create_dict_from_kwargs(**kwargs):
    """
    将关键字参数包装成一个字典并返回。

    :param kwargs: 关键字参数
    :return: 包含所有关键字参数的字典
    """
    return {key: value for key, value in kwargs.items()}

class spin:
    """
    用于显示等待的转圈
    """
    def start_spinner(self):
        # self.spinner_thread = threading.Thread(target=self.spinner)
        # self.spinner_thread.start()
        pass

    def stop_spinner(self):
        # if self.spinner_thread:
        #     self.spinner_thread.join()
        #     # 清除指示器文本
        #     print('\r' + ' ' * 30 , end='')
        #     print("\n")
        #     self.spinner_thread = None
        pass

    def spinner(self):
        """显示不断转圈的斜杠指示器"""
        while True:
            for cursor in '|/-\\':
                print(f'\r{cursor} 操作进行中...', end='')
                time.sleep(0.2)

def get_absolute_path(path):
    # Check if the path is absolute or relative
    if os.path.isabs(path):
        return path
    else:
        # Get the current working directory and join it with the relative path
        current_directory = os.getcwd()
        return os.path.join(current_directory, path)

def get_sourcename_path(path):
    # Check if the path is absolute or relative
    if os.path.isabs(path):
        return path
    else:
        # Get the current working directory and join it with the relative path
        current_directory = os.getcwd()
        return os.path.join(current_directory, path)


def get_relative_path(absolute_path):
    # 获取当前工作目录
    current_dir = os.getcwd()

    # 使用os.path.relpath计算相对路径
    relative_path = os.path.relpath(absolute_path, current_dir)

    # 返回相对路径，不包括最后的文件夹名
    return relative_path[:-len(os.path.basename(absolute_path))]

def convert_seconds_to_time(seconds):
    if seconds <= 0:
        return "--:--:--"
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"