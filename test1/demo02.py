"""
high_score = {}  
low_score = {}
studentlist = ["一","二","三","四","五","六","七","八","九","十"]
a = 0
while a < len(studentlist):
    score = int(input("请输入"+studentlist[a]+"的成绩:"))
    if score >= 60:
        high_score[studentlist[a]] = score
    else:
        low_scmdcore[studentlist[a]] = score
    a = a + 1
print(high_score)
print(low_score)
"""



"""
high_score = {}  
low_score = {}
studentlist = ["一","二","三","四","五","六","七","八","九","十"]
for i in studentlist:
    score = int(input("请输入"+i+"的成绩:"))
    if score >= 60:
        high_score[i] = score
    else:
        low_score[i] = score
print(high_score)
print(low_score)
"""  


"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"x",j,"=",i*j,end = "  ")
    print()
"""
"""
while True:
    light =  {"红灯":30,"绿灯":35,"黄灯":3}
    for i in light:
        for j in range(light[i]):
            print(i,light[i] - j)
"""
"""
username = input("请输入账号：")
password = input("请输入密码：")
if len(username) >= 5 and len(username) <= 8:
    if username[0] in "abcdefghijklmnopqrstuvwxyz":
        if len(password) >= 8 and len(password) <= 12:
            print("注册成功",{username:password})
        else:
            print("密码不符合规范")
    else:
        print("不符合规范")
else:
    print("不符合规范")
"""
"""
import pymysql
db = pymysql.connect(host= "127.0.0.1",user="root",db="testdb")
cur = db.cursor()
cur.execute("select * from t_class;")
res = cur.fetchall()
print(res)
"""

class Test():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        print(self.a+self.b+self.c)

Use = Test(1,2,3)
Use.add()
