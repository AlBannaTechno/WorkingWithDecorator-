class DecodetWithoutArguments(object):
    def __init__(self,func):# rec : test'function'
        print("insied __init__")
        self.fun=func
    # __call__ : rec func'test' parameters 
    def __call__(self,*args,**kwargs):# we can pass args kwargs to fun or not
        print("Inside __call__")# down
        self.fun(args,kwargs)# here what we mean

    # if we not defined __call__ special function
    # this program will start automaticly
@DecodetWithoutArguments
def test(args,kwargs):
    print("inside test")
    print(args)
    print(kwargs)

if __name__=="__main__":
    test(23,34,54,os="osama",no="Nor")# we can pass paras or nots
