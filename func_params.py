#coding=utf-8


# *为可变参数

def param(name,age,*phone):
    print "name",name," age",age

    for p in phone:
        print p





param("hl",88,"15822324323","12723921233")


# **为关键字参数 在函数内部自动组装成dict

def param2(*p,**other):
    print p
    print other




param2("2","3",city="beijing",sex="男")


# 默认参数
#
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
#
# 二是如何设置默认参数。
#
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def param3(name,age,city="beijing",sex="男"):
    print "name",name,"age",age,"city",city,"sex",sex


param3("hd",99,sex="女")
param3("hf",98)