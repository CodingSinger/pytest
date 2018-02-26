#coding=utf-8



s = set([1, 1, 2, 2, 3, 3])
#重复元素在set中自动被过滤：
print s

#增加元素

s.add("4")

print s

print s.pop() #移除最左边的元素
print s
s.remove(3)


print s
s.pop()
print s



