
#encoding=utf-8

# 函数作为参数
def func1(func,list):
    for e in list:
        func(e)
        print(e)

def add_1(num):
    num = num+1
    print(num)

func1(add_1,[2,4,5])

#匿名参数
func1(lambda x:)
