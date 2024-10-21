from fourthdimension import FDClient

fd = FDClient("http://192.168.21.215:9090")
fd.createKB("test1018")

# fd.importDocument("test1018", "/mnt/user/csy_project/work/RAG_fd/fd_python_client/data/52文档/50文档/1. 高级分布式系统.docx")
# fd.ruminate("test1018", 1)
print(fd.query("test1018", "什么叫分布式系统？"))
