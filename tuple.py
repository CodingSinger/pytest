#coding=utf-8

# tuple简单的说就是不可变的list

t = ('a', 'b', ['A', 'B'])


print len(t)

# t[1] = 'A' 不能修改tuple的元素
t[2][1] = 'X'
# 但这里是修改tuple元素的List元素的值
print t
