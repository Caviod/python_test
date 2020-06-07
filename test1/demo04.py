# 函数的作用域
var = 1
def func():
    global var
    var = 2  #global表示使用全局变量 否则只对函数内定义的同名局部变量产生操作
    print(var)

func()
print(var)

# 函数的迭代器
list = [1,2,3]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 函数生成器
def frange(start,stop,step):
    x = start
    while x < stop:
        yield x
        x = x + step

for i in frange(10,20,0.5):
    print(i)