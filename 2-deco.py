from time import sleep
import time
#decorator

class Cdeco(object):
    def test_deco(func):# if we but self we will case many problem
        def first():
            print("Function exceuted at : %s" % time.time())
            func()
            print("Function Finished at : %s" % time.time())

        # return first

        def second():
            print("Function2 exceuted at : %s" % time.time())
            func()
            print("Function2 Finished at : %s" % time.time())

        return second


@Cdeco.test_deco
def My_func():
    print("I My_Function ")
    te=[]
    for a in range(1,200000):
        te.append(a)

My_func()




