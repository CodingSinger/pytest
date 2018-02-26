
#coding=utf-8
#类变量和实例变量


class Student:
    count = 0


    def __init__(self,name,age):
        self.name = name
        self.__age = age


    def p(self,h):
        self.h = h

    def __private_method(self):
        #以 __双下划线开头的变量和方法都是对象私有的，无法再对象外部访问 并且不同于java，在实例方法中不能直接调用其他实例方法，只能用self去调用
        print "private method"

    def call_privateMethod(self):
        # __private_method()
        self.__private_method()





if __name__ == '__main__':
    s = Student("zs",100)
    s.p(10)
    print s.h
    print s.count

    s2 = Student("ls",88)
    s2.p(11)
    print s2.h
    print s2.count
    print s2.count

    print Student.count
    # print Student.h

    s2.call_privateMethod()

    # s2.__private_method__()
    # print s2.__age

