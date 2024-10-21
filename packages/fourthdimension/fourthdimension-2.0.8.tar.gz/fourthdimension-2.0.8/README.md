
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 使用示例
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FourthDimension支持批量导入一个文件目录下的所有文档，“path/”是存放文档的文件目录名称。
```python
from fourthdimension import FDClient

fdClient = FDClient()
fdClient.setServeUrl("http://192.168.21.105:9090")
# answer = fdClient.query("test0731", "s6的前十是谁呢？")
# print(answer)
fdClient.deleteKB("test0731")
fdClient.createKB("test0731")
fdClient.importDocuments("test0731", "/media/ytkj/5207915e-0f68-4eae-9219-2f89014a6ae1/user/csy_project/work/RAG_fd/data_for_test", 0)
fdClient.ruminate("test0731", fdClient.CHUNK_EMBEDDING)
fdClient.ruminate("test0731", fdClient.CHUNK_SUMMARIZING)
fdClient.ruminate("test0731", fdClient.CHUNK_SELF_ASKING)
fdClient.ruminate("test0731", fdClient.SUMMARIZING)
fdClient.ruminate("test0731", fdClient.SELF_ASKING)
datas = fdClient.recallDocuments("test0731", "原神是不是抄袭")["data"]
for data in datas[:10]:
    print(data)
fdClient.getKBInfo("test0731")
fdClient.deleteKB("test0731")