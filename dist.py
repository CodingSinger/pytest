#coding=utf-8

# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。



map = {"1":"one","2":"two","3":"three",4:"what"}


print map["1"]

print map[4]

print map.get(4)

print map.get("5")
print map.get("5","five") #不存在则返回five

map["1"] = ["1"]

print map["1"]

map[5] = "five"
print map


# 判断map中是否存在key

print "1" in map
print "4" in map

