import os
import time

from fourthdimension import FDClient
from vutils import io
import pandas as pd


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



pd.read_excel("")
fd_client=FDClient("http://127.0.0.1:9091")
# fd_client.deleteKB("test")
# fd_client.createKB("test")
# fd_client.importDocuments("test","/mnt/user/csy_project/work/RAG_fd/fd_python_client/data/111", 0)
