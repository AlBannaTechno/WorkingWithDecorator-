from time import sleep
import time
#decorator
# if we use this method
# we just consider that our function inside class
# like any decoder function
# we also can compare decoder class with func-class decoder
# with __init__ and __call__
class Cdeco(object):
    def __init__(self,*args,**kwargs):# will calling once at start of @className
        print("__init__ Will Ex:Once")
        print(args)
        print(kwargs)
    def __call__(self,func):#receive function
        # __call__ will calling once agter __init__
        # but it's will called whenever we calling the function my()
        print("__call__ Will Ex:Once")
        def RecVar(*args,**kwargs):
            print("RecVar")
            func(args,kwargs)
        return RecVar

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


@Cdeco.second_test_deco(100,240,os="osama",no="noor")
def Fu(*args,**kwargs):
    print("Fu")
    print(args)
    print(kwargs)



print("##################ClassDEcoder#################")
@Cdeco(54,"opa",osa="osama")
def my(*args,**kwargs):
    print("My")
    print(args)
    print(kwargs)

if __name__=="__main__":
    My_func()
    Fu(57, "hello", vc="Vocablary", no="No Peacea")
    my(56,"asd",op="operation",os="Operation System")
    my(76767, 8555, osp="opefgration", obf="Osdfn System")
