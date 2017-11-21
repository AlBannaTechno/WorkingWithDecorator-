from time import sleep
import time
#decorator

def test_deco(func):
    def first():
        print("Function exceuted at : %s"%time.time())
        func()
        print("Function Finished at : %s"%time.time())
    return first

# fo(fa)
#   fa=fo(fa)
#   My_func=test_deco(My_func)
@test_deco
def My_func():
    print("I My_Function ")
    te=[]
    for a in range(1,200000):
        te.append(a)

# instead of say
# My_func=test_deco(My_func)
My_func()