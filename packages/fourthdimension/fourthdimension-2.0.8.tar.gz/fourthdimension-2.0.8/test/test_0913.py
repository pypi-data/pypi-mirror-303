import time

from anyio import sleep

from fourthdimension import FDClient
from vutils import io
fdclient = FDClient()

fdclient.deleteKB("test")
exit(0)

kbname = "ai_tutor2"
# kbname = "test"
# exit(0)
fdclient.deleteKB(kbname)
fdclient.createKB(kbname)
fdclient.importDocuments(kbname,"/mnt/user/csy_project/work/RAG_fd/fd_python_client/data/ai_tutor")
time.sleep(5)
fdclient.ruminate(kbname,fdclient.CHUNK_EMBEDDING)
time.sleep(5)
fdclient.ruminate(kbname,fdclient.SENTENCE_EMBEDDING)
questions = [
    "江西航空，由于客户自己原因退票的手续是什么？",
    "那退票需要提前多久联系江西航空？",
    "我是经济舱的机票，提前多久退票不会扣钱",
    "退票时候，我需要提供哪些证明材料？",
    "经济舱退票可能因为不同仓位，有不同收费嘛？",
    "如果是不可抗拒力导致的退票，江西航空会收费嘛？",
    "如果因为台风等情况，航班取消，江西航空会提供什么补救措施",
    "江西航空的客服热线是多少，我该如何联系他们",
]
# exit(0)
# kbname = "ai_tutor2"
# data_list = []
# for question in questions:
#      answer = {}
#      data = fdclient.query(kbname, question)
#      answer["answer"] = data["answer"]
#      answer["recall"] = []
#      for i in range(10):
#          answer["recall"].append(data["recall"][i]["origin_content"] if data["recall"][i]["origin_content"]!= None or data["recall"][i]["origin_content"]!= "" else data["recall"][i]["content"])
#      data_list.append(answer)
# io.jsondump(data_list, "data_list_pdf_2.json")

# kbname = "ai_tutor3"
data_list = []
for question in questions:
     answer = {}
     data = fdclient.test(kbname, question)["data"]
     answer["question"] = question
     answer["answer"] = data["answer"]
     answer["recall"] = []
     for i in range(10):
         answer["recall"].append(data["recall"][i]["content"] if data["recall"][i]["origin_content"]==None or data["recall"][i]["origin_content"]=="" else data["recall"][i]["origin_content"])
     data_list.append(answer)
io.jsondump(data_list, "data_list_word_0924_2.json")