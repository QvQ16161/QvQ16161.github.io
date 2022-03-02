import os

日志path="日志"
日志索引=r"日志索引.md"

日志list=os.listdir(日志path)

print(日志list)


f=open(日志索引,"w+",encoding="utf-8")



for i in 日志list:
    filename=i.split(".")[0]
    f.write("["+filename+"]"+"(日志/"+i+")")


