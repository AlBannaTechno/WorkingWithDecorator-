from time import sleep
import time
#decorator

def test_deco(func):
    def first(var):
        print("Function exceuted at : %s"%time.time())
        func(var)
        print("Function Finished at : %s"%time.time())
    return first


@test_deco
def My_func(var):
    print("I My_Function "+str(var))
    te=[]
    for a in range(1,200000):
        te.append(a)

# instead of say
# My_func=test_deco(My_func)
My_func(45645)