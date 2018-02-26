#coding=utf-8
print([1,3])
print(iter([1,3]))
l = [x for x in range(10)] #x为l中的元素
print(l)
l1 = [d not in '234' for d in '23d45'] # d not in '234'为l1中的元素
print(l1)
print(all(d not in '234' for d in '23d45'))

print(d not in '234' for d in '23d45')

