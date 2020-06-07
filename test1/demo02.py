# 文件操作
# 第一次写入 w 会自动覆盖
file1 = open(r'C:\Users\A\Desktop\文件测试.txt','w')
file1.write('测试')
file1.close()

# 读取文档内容
file2 = open(r'C:\Users\A\Desktop\文件测试.txt')
print(file2.read())
file2.close()

# 添加新的东西
file3 = open(r'C:\Users\A\Desktop\文件测试.txt','a')
file3.write('测试')
file3.close()

# 读取单行
file4 = open(r'C:\Users\A\Desktop\文件测试.txt')
print(file4.readline(1))

# 读取多行
file5 = open(r'C:\Users\A\Desktop\文件测试.txt')
for line in file5.readlines():
    print(line)
print(file5.tell()) #tell读取文件目前指针位置
file5.seek(0，0) #seek第一个参数代表偏移位置 第二个参数 0 从开头进行偏移 1 从当前位置进行偏移 2 从结尾进行偏移