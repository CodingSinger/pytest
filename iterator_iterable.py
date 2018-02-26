#!coding=utf-8
# 可迭代对象：Iterable ，迭代器：Iterator
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list / tuple / dict / set / str /等;
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象


# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
#
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#
# 可以使用isinstance()判断一个对象是否是Iterator对象：




from collections import Iterable, Iterator

import sys

l = [1,2,3,5]
s = "3df"


print(isinstance(l,Iterable))
print(isinstance(s,Iterable))

print(isinstance(l,Iterator))

print(isinstance(s,Iterator))

l_r = iter(l)
print(isinstance(l_r,Iterable))
print(isinstance(l_r,Iterator))


#遍历Itertor对象
while True:
    try:
        print (next(l_r))
    except StopIteration:
        print("end")
        break


# 小结
#
# 凡是可作用于for循环的对象都是Iterable（可迭代对象）类型;
#
# 凡是可以作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列;
#
# 集合数据类型如 list / dict / str / 等是Iterable可迭代对象但不是Iterator迭代器，不过可以通过iter()函数可以获得一个Iterator对象。但Iterator对象一定是Iterable可迭代对象
