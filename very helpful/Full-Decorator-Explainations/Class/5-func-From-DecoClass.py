from time import sleep
import time
#decorator
# if we use this method
# we just consider that our function inside class
# like any decoder function
# we also can compare decoder class with func-class decoder
# with __init__ and __call__
class Cdeco(object):
    def test_deco(func):# if we but self we will case many problem
        def first():
            print("Function exceuted at : %s" % time.time())
            func()
            print("Function Finished at : %s" % time.time())
        return first

    def second_test_deco(*args,**kwargs):
        print(args)
        print(kwargs)
        def GetFunc(func):
            print("GetFunc")
            def GetFuncParas(*args,**kwargs):
                print("Get Function Parameters")
                func(args,kwargs)
            return GetFuncParas
        return GetFunc


@Cdeco.test_deco
def My_func():
    print("I My_Function ")
    te=[]
    for a in range(1,200000):
        te.append(a)

My_func()

print("Second Test")

@Cdeco.second_test_deco(100,240,os="osama",no="noor")
def Fu(*args,**kwargs):
    print("Fu")
    print(args)
    print(kwargs)

Fu(57,"hello",vc="Vocablary",no="No Peacea")


