import os
import json
import sys

import logging

from httpx._exceptions import ConnectError
from .fd_httpclient import FDHttpClient
from .chat._client import FourthDimensionAI
from .fd_utils import *

fdHttpClient = FDHttpClient()
package_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
resource_path = os.path.join(package_path, "resources")
config_path = os.path.join(resource_path, "fd_python_config.json")


class FDClient:
    def __init__(self, server_url=None):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

        # 如果提供了server_url参数，则使用它，否则从配置文件中读取
        if server_url is not None:
            self.Baseurl = server_url + "/"
        else:
            self.Baseurl = self.config["url"]["base_url"] + "/"
        self.NO_OPERATION = 0x00
        self.CHUNK_EMBEDDING = 0x01
        self.SENTENCE_EMBEDDING = 0x02
        self.SUMMARIZING = 0x08
        self.CHUNK_SUMMARIZING = 0x10
        self.SELF_ASKING = 0x04
        # self.CHUNK_SELF_ASKING = 0x20

    def setServeUrl(self, serve_url):
        """用于设置BaseUrl"""
        self.Baseurl = serve_url + "/"

    def getKBInfo(self, KBName):
        """用于获取知识库信息"""
        print(f"正在获取知识库 ‘{KBName}’ 的信息...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            requestdata = create_dict_from_kwargs(kbName=KBName)
            result = fdHttpClient.send_request(url=self.Baseurl + "getKBInfo", json_data=requestdata, method="POST")
            if result["code"] == 0:
                print("获取信息成功")
                return result["data"]
            else:
                # print("发生服务器内部错误：")
                # print(result["msg"])
                print('\033[31m' + result['msg'] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m连接服务端失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("获取客户端信息失败")
            return {"code": -10, "msg": "发生错误"}

    def getFDInfo(self):
        """用于获取服务器信息"""
        print("正在获取服务器信息...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            requestdata = create_dict_from_kwargs()
            result = fdHttpClient.send_request(url=self.Baseurl + "getFDInfo", json_data=requestdata, method="POST")
            if result["code"] == 0:
                print("获取信息成功")
                return result["data"]
            else:
                # print(result["msg"])
                print('\033[31m' + result['msg'] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m连接服务端失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("获取服务器信息失败")
            return {"code": -10, "msg": "发生错误"}

    def createKB(self, KBName):
        """用于创建知识库"""
        print(f"正在创建知识库：{KBName}...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            requestdata = create_dict_from_kwargs(kbName=KBName)
            result = fdHttpClient.send_request(url=self.Baseurl + "createKB", json_data=requestdata, method="POST")
            if result["code"] == 0:
                print(result["msg"])
                return result
            else:
                # print(result["msg"])
                print('\033[31m' + result['msg'] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误")
            return {"code": -10, "msg": "发生错误"}

    def deleteKB(self, KBName):
        """用于删除知识库"""
        print(f"正在删除知识库：{KBName}...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            requestdata = create_dict_from_kwargs(kbName=KBName)
            result = fdHttpClient.send_request(url=self.Baseurl + "deleteKB", json_data=requestdata, method="POST")
            if result["code"] == 0:
                print(result["msg"])
                return result
            else:
                # print("发生服务器内部错误：")
                print('\033[31m' + result['msg'] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，删除失败")
            return {"code": -10, "msg": "发生错误"}

    def importDocuments(self, KBName, targetFileName, rumination=0):
        """用于导入文件夹"""
        try:
            print(f"正在向知识库 ‘{KBName}’ 导入文件夹：{targetFileName}...")
            print(f"服务器地址：{self.Baseurl}")
            if not os.path.exists(targetFileName):
                print(f"\033[31m文件夹导入失败：导入路径 ‘{targetFileName}’ 不存在\033[0m")
                return {"code": -1, "msg": "导入路径错误"}
            if os.path.isfile(targetFileName):
                print("\033[31m文件夹导入失败：请确认文件夹路径\033[0m")
                return {"code": -1, "msg": "导入文件夹错误"}
            data_url = get_absolute_path(targetFileName).replace("//", "/").replace(".../", "").replace("../",
                                                                                                        "").replace(
                "./", "")
            data_file_name = os.path.basename(targetFileName)
            Document_list = get_all_file_paths(targetFileName)
            cout = 0
            if len(Document_list) == 0:
                print("\033[31m文件导入失败：文件夹内不包含支持格式的文件类型\033[0m")
                return {"code": -1, "msg": "文件夹内不包含支持格式的文件类型"}
            success_num = 0
            for Document_Path in Document_list:
                files = {"file": open(Document_Path, "rb")}
                url = Document_Path[len(data_url) - len(data_file_name) - 1:].replace("\\", "/")
                if url[0] != "/":
                    url = "/" + url
                requestdata = create_dict_from_kwargs(kbName=KBName, targetFileName=url, rumination=rumination)
                print(f"正在导入文件：{Document_Path}...")
                result = fdHttpClient.send_request_fromdata(url=self.Baseurl + "addDocument", data=requestdata,
                                                            files=files, method="POST")
                if result["code"] == 0:
                    print(f"导入文件完成：{Document_Path}")
                    cout = cout + result["data"]
                    success_num += 1
                else:
                    # print("发生服务器内部错误：")
                    # print(result["msg"])
                    print('\033[31m' + result['msg'] + '\033[0m')
                # print(Document_Path + " " + result["msg"])
            s = len(Document_list)
            print("文件夹导入成功，共导入" + str(success_num) + "个文件，被切分为" + str(cout) + "个chunk")
            result["msg"] = "文件夹导入成功"
            return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，导入失败")
            return {"code": -10, "msg": "发生错误"}

    def importDocument(self, KBName, sourceFileName, rumination=0):
        """用于导入文件"""
        print(f"正在向知识库 ‘{KBName}’ 导入文件：{sourceFileName}...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            if not os.path.exists(sourceFileName):
                print(f"\033[31m文件导入失败：文件路径 ‘{sourceFileName}’ 不存在\033[0m")
                return {"code": -1, "msg": "路径错误"}
            if os.path.isdir(sourceFileName):
                print("\033[31m文件导入失败：请传入文件路径\033[0m")
                return {"code": -1, "msg": "传入文件错误"}
            files = {"file": open(sourceFileName, "rb")}
            sourceFileName = os.path.basename(sourceFileName)
            requestdata = create_dict_from_kwargs(kbName=KBName, targetFileName="/" + sourceFileName,
                                                  rumination=rumination)

            result = fdHttpClient.send_request_fromdata(url=self.Baseurl + "addDocument", data=requestdata, files=files,
                                                        method="POST")
            if result["code"] == 0:
                print(f"‘{sourceFileName}’" + " " + result["msg"])
                print("文件成功导入到知识库，被切分为" + str(result["data"]) + "个chunk")
                return result
            else:
                # print("发生服务器内部错误：")
                print('\033[31m' + result['msg'] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，添加失败")
            return {"code": -10, "msg": "发生错误"}

    def deleteDocument(self, KBName, targetFileName):
        """用于删除文件"""
        # targetFileName = get_absolute_path(targetFileName)
        print(f"正在知识库 ‘{KBName}’ 中删除文件: {targetFileName}...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            if (targetFileName[0] != "/"):
                targetFileName = "/" + targetFileName
            targetFileName.replace("\\", "/")
            requestdata = create_dict_from_kwargs(kbName=KBName, targetFileName=targetFileName)
            result = fdHttpClient.send_request(url=self.Baseurl + "deleteDocument", json_data=requestdata,
                                               method="POST")
            if result["code"] == 0:
                print(result["msg"])
                return result
            else:
                # print("发生服务器内部错误：")
                # print(result["msg"])
                print('\033[31m' + result['msg'] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("删除失败")
            return {"code": -10, "msg": "发生错误"}

    def updateDocument(self, KBName, sourceFileName, targetFileName, rumination=0):
        """用于更新文件"""
        print(f"正在知识库 ‘{KBName}’ 中更新文件：{sourceFileName}...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            sourceFileName = get_absolute_path(sourceFileName)
            if (targetFileName[0] != "/"):
                targetFileName = "/" + targetFileName
            targetFileName.replace("\\", "/")
            files = {"file": open(sourceFileName, "rb")}
            requestdata = create_dict_from_kwargs(kbName=KBName, sourceFileName=sourceFileName,
                                                  targetFileName=targetFileName, rumination=rumination)
            result = fdHttpClient.send_request_fromdata(url=self.Baseurl + "updateDocument", data=requestdata,
                                                        files=files, method="POST")
            print("更新成功" + "\n")
            return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，更新失败")
            return {"code": -10, "msg": "发生错误"}

    def recallDocuments(self, KBName, question):
        """用于查询"""
        print(f"正在知识库 ‘{KBName}’ 中查询...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            requestdata = create_dict_from_kwargs(kbName=KBName, question=question)
            result = fdHttpClient.send_request(url=self.Baseurl + "recall", json_data=requestdata, method="POST")
            if result["code"] == 0:
                print(result["msg"])
                return result
            else:
                # print("发生服务器内部错误：")
                print('\033[31m' + result["msg"] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，查询失败")
            return {"code": -10, "msg": "发生错误"}

    def recallDocuments2(self, KBName, question):
        """用于查询"""
        print(f"正在知识库 ‘{KBName}’ 中查询...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            requestdata = create_dict_from_kwargs(kbName=KBName, question=question)
            result = fdHttpClient.send_request(url=self.Baseurl + "recall2", json_data=requestdata, method="POST")
            if result["code"] == 0:
                print(result["msg"])
                return result
            else:
                # print("发生服务器内部错误：")
                print('\033[31m' + result["msg"] + '\033[0m')
                return result
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，查询失败")
            return {"code": -10, "msg": "发生错误"}


    def test(self, KBName, question):
        """用于查询"""
        print(f"正在知识库 ‘{KBName}’ 中查询...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            requestdata = create_dict_from_kwargs(kbName=KBName, question=question,option="FD")
            result = fdHttpClient.send_request(url=self.Baseurl + KBName + "/_test", json_data=requestdata, method="POST")
            return result

        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，查询失败")
            return {"code": -1, "msg": "发生错误"}

    def query(self, KBName, question):
        """获取查询和生成回答"""
        print("正在生成回答...")
        print(f"服务器地址：{self.Baseurl}")
        try:
            client = FourthDimensionAI(base_url=self.Baseurl + "query")
            result = client.chat.completions.create(
                model="qwen",
                question=question,
                kbName=KBName,
                messages=[],
                stream=False,
                rumination=None
            )
            # print(result)
            if result.model_extra['code'] == 0:
                print("生成成功")
                return result.model_extra
            else:
                # print("发生服务器内部错误：")
                # print(result.msg)
                print('\033[31m' + result.model_extra['msg'] + '\033[0m')
                return result.model_extra
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，查询失败")
            return {"code": -10, "msg": "发生错误"}

    # 用流式来写反刍
    def ruminate(self, KBName, rumination):
        """流式获取反刍结果"""
        client = FourthDimensionAI(base_url=self.Baseurl + "ruminate_stream")
        try:
            result = client.chat.completions.create(
                model="qwen",
                question=None,
                kbName=KBName,
                rumination=rumination,
                messages=[],
                stream=True
            )

            start_time2 = time.time()
            start_time = time.time()
            print(f"正在对知识库 ‘{KBName}’ 进行反刍...")
            print(f"服务器地址：{self.Baseurl}")
            chunk_cout = 0
            documents = []
            for chunk in result:
                data = (chunk.choices[0].delta.content)
                if isinstance(data, str):
                    if data == "error":
                        return {"code": -1, "msg": "发生错误"}
                    else:
                        errMsg = data.split(";")
                        if len(errMsg) == 2:
                            print("\n\033[31m" + errMsg[1] + '\033[0m')
                            return {"code": int(errMsg[0]), "msg": errMsg[1]}
                        else:
                            print("\n\033[31m" + data + '\033[0m')
                            return {"code": -10, "msg": data}
                if isinstance(data, dict):
                    print("\r", end="")
                    if data["process_cout"]["total"] == 0:
                        print("知识库" + data["process"].replace("not_", "").replace("embedded",
                                                                                                            "embedding").replace(
                            "summarized", "summarizing").replace("asked", "asking") + "类型反刍已完成")
                        # print("\n")
                        continue
                    i = 100 * (data["process_cout"]["cout"] / data["process_cout"]["total"])
                    end_time = time.time()
                    if "document_name" in data:
                        documentname = data["document_name"]
                        if documentname not in documents:
                                documents.append(documentname)
                    if "chunk_num" in data:
                        chunk_cout = data["chunk_num"] if data["chunk_num"] > chunk_cout else chunk_cout
                    spendtime = convert_seconds_to_time(int(end_time - start_time))
                    if data["process_cout"]["cout"] == data["process_cout"]["total"]:
                        print("正在进行" + data["process"].replace("not_", "").replace("embedded", "embedding").replace(
                            "summarized", "summarizing").replace("asked", "asking") + "类型反刍，反刍进度：" + str(
                            data["process_cout"]["cout"]) + "/" + str(data["process_cout"][
                                                                           "total"]) + "，正在反刍的文件为：" + documentname + "，该类型反刍总用时：" + spendtime)
                    else:
                        print("正在进行" + data["process"].replace("not_", "").replace("embedded", "embedding").replace(
                            "summarized", "summarizing").replace("asked", "asking") + "类型反刍，反刍进度：" + str(
                            data["process_cout"]["cout"]) + "/" + str(data["process_cout"][
                                                                           "total"]) + "，正在反刍的文件为：" + documentname + "，该类型反刍已用时：" + spendtime,
                              end="")
                    sys.stdout.flush()
                    if i == 100:
                        start_time = time.time()
                        chunk_cout = data["chunk_num"]
                        # print("\n")
            end_time2= time.time()
            totaltime = convert_seconds_to_time(int(end_time2 - start_time2))
            print("反刍完成，用时：" + totaltime + "，"  + str(len(documents)) + "个文件，"+ str(chunk_cout) + "个chunk")
            return {"code": 0, "msg": "反刍完成"}
        except ConnectError:
            print("\033[31m服务端连接失败：请确认服务端网络是否可达以及服务端是否正常启动\033[0m")
            return {"code": -1, "msg": "连接失败"}
        except Exception as e:
            print(e)
            print("客户端发生错误，反刍发生错误")
            return {"code": -10, "msg": "发生错误"}

    # def ruminate(self, KBName, rumination):
    #     """用于创建反刍线程以及进行轮询"""
    #     starttime = time.time()
    #     try:
    #         requestdata = create_dict_from_kwargs(kbName=KBName, rumination=rumination)
    #         fdHttpClient.send_request(url=self.Baseurl + "ruminate_start", json_data=requestdata, method="POST")
    #         result = {}
    #         tmp = ""
    #         cout = 5
    #         while (True):
    #             response_data = \
    #                 fdHttpClient.send_request(url=self.Baseurl + "ruminate_polling", json_data=requestdata,
    #                                           method="POST")[
    #                     "data"]
    #
    #             if response_data["process_cout"] == None and response_data["process"] != None and response_data[
    #                 "process"] != "NO_OPERATION":
    #                 continue
    #             elif response_data["process"] == "NO_OPERATION":
    #                 cout = cout - 1
    #                 if cout == 0:
    #                     result["msg"] = "反刍完成"
    #                     result["data"] = None
    #                     result["code"] = 0
    #                     print("\n反刍完成")
    #                     break
    #
    #             process = response_data["process"]
    #             if response_data["process_cout"] == None:
    #                 process_cout = {
    #                     "cout": 0,
    #                     "total": 1
    #                 }
    #             else:
    #                 process_cout = response_data["process_cout"]
    #             nowtime = time.time()
    #             usedtime = nowtime - starttime
    #             print("\r", end="")
    #             if process == "NO_OPERATION" or process == "PREPARED":
    #                 print("\nwaiting")
    #                 # sys.stdout.flush()
    #                 # pass
    #             else:
    #                 if process_cout["cout"] == 0:
    #                     print("知识库 " + process.strip("not_") + "反刍进度: {}%, ".format(
    #                         int(process_cout["cout"] * 100 / process_cout["total"])),
    #                           "▓" * (int(process_cout["cout"] * 100 / process_cout["total"]) // 2), end="")
    #
    #                 else:
    #                     print("知识库 " + process.strip("not_") + "反刍进度: {}%, ".format(
    #                         int(process_cout["cout"] * 100 / process_cout["total"])),
    #                           "知识库 " + process.strip("not_") + "预计用时: {}s: ".format(
    #                               int(usedtime / (process_cout["cout"] / process_cout["total"]))),
    #                           "▓" * (int(process_cout["cout"] * 100 / process_cout["total"]) // 2), end="")
    #                 sys.stdout.flush()
    #             if int(process_cout["cout"] * 100 / process_cout["total"]) == 100:
    #                 if process != "NO_OPERATION" and tmp != process:
    #                     print("\n\n\n")
    #                     starttime = time.time()
    #             time.sleep(2)
    #             tmp = process
    #         return result
    #     except Exception as e:
    #         print(e)
    #         print("创建反刍失败")
    #         return {"code": -1, "msg": "发生错误"}
