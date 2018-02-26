
#coding=utf-8

def throwException():
    raise Exception("异常啦")



if __name__ == '__main__':

    print "异常启动"

    try:

        throwException()
    except Exception as e:
        print "我是异常信息:"+ e.message #打印异常信息
    finally:
        print "无论如何都执行"





    #如果不用try catch遇到异常 则程序直接崩溃 不会继续执行
    print "正常结束"

