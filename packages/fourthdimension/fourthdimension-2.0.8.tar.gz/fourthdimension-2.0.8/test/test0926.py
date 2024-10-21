# encoding: utf-8
import time

from fourthdimension import FDClient
from vutils import io

fd_client=FDClient("http://127.0.0.1:9091")
your_kbName = "dlzts1000_100"
# fd_client.deleteKB(your_kbName)
# fd_client.createKB(your_kbName)
# fd_client.importDocuments(your_kbName,"/mnt/user/csy_project/work/RAG_fd/fd_python_client/data/dlzts",fd_client.NO_OPERATION)
# time.sleep(10)
# fd_client.ruminate(your_kbName,fd_client.SENTENCE_EMBEDDING)
# time.sleep(10)
# fd_client.ruminate(your_kbName,fd_client.CHUNK_EMBEDDING)
# time.sleep(10)

datas = io.jsonload("original_data.json")


for data in datas:
    result = fd_client.recallDocuments2(your_kbName, data["question"])  # 根据问题"your_question"，召回相关文件片段
    contexts = []
    context = {}
    if result["code"] == 0:  # 打印召回结果
    #     print("以下为召回文件：\n")
    #     for i in result["data"]:
    #         del i["vector"]
    #         contexts.append(i)
        for i in range(10):
            if result["data"][i]["origin_content"] is not None  and result["data"][i]["origin_content"] != "":
                context["文档-" + str(i + 1)] = result["data"][i]["origin_content"]
            else:
                context["文档-" + str(i + 1)] = result["data"][i]["content"]

        data["contexts"] = context
        # data["answer"] = ""
        # data["answer_contexts"] = []
io.jsondump(datas,"original_data0929_all_new_fix.json" )


# for data in datas:
#     result = fd_client.recallDocuments(your_kbName, data["question"])  # 根据问题"your_question"，召回相关文件片段
#     contexts = []
#     context = {}
#     if result["code"] == 0:  # 打印召回结果
#         print("以下为召回文件：\n")
#         for i in result["data"]:
#             del i["vector"]
#             contexts.append(i)
#         # for i in range(10):
#         #     if result["data"][i]["origin_content"] is not None  and result["data"][i]["origin_content"] != "":
#         #         context["文档-" + str(i + 1)] = result["data"][i]["origin_content"]
#         #     else:
#         #         context["文档-" + str(i + 1)] = result["data"][i]["content"]
#
#         data["contexts"] = contexts
#         # data["answer"] = ""
#         data["answer_contexts"] = []
# io.jsondump(datas,"original_data0927_all_old.json" )