#coding=utf-8


#java中类方法和静态方法可以理解为同一种类型 但python中不一样 https://zhuanlan.zhihu.com/p/21101992
class Student:


    def __init__(self,name):

        self.name = name
    def printname(self): #实例方法
        print self.name

    @staticmethod #静态方法  参数没有要求
    def static_method():
        print "static method"

    @classmethod  #类方法 第一个参数默认为类
    def class_method(cls):
        print "classmethod"

if __name__ == '__main__':
    s = Student("ll")
    s.static_method()
    Student.static_method()
    Student.class_method()
    s.class_method()



