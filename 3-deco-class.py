from time import sleep
import time
#decorator

class Cdeco(object):
    def __init__(self,func):# we must not forget that is as constructore
        print("Storing Function Into Class")
        self.f=func
    def __call__(self, *args):
        self.f(args)

@Cdeco
def My_func(*args):
    print("I My_Function "+str(args))

My_func(23,5645,"osama")




