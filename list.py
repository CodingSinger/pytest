
#coding=utf-8
list1 = [0] *5
list2 = [0 for i in range(5)]
print len(list2)
print len(list1)

list3 = ["z","k","d"]
list3.append("h")
print list3

list3.append("hello") #添加一个元素
print list3

print list3.pop()  #移除最后一个元素
print list3.pop(1) #移除指定的元素

print list3

print list3.insert(2,"p") #插入第2个位置处

print list3
print list3[2]


print list1[0]