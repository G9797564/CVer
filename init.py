#创建存储数据的文件，首次运行前单独运行生成存储数据的文件
import pickle as pk
fw=open("CVData","wb")
pk.dump((),fw)
fw.close()
