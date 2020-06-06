import time
now = time.strftime("%y-%m-%d %H:%M:%S")
text = input()
with open("F:\python_test\python_test\日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")

with open("F:\python_test\python_test\日记.txt","r",encoding="utf8") as f:
    test = f.readlines()

for i in test:
    print(i)