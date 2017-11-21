class DecodetWithoutArguments(object):
    def __init__(self,func):# rec : test'function'
        print("insied __init__")
        self.fun=func

    def __call__(self):
        print("Inside __call__")
        self.fun()

    # if we not defined __call__ special function
    # this program will start automaticly
@DecodetWithoutArguments
def test():
    print("inside test")

if __name__=="__main__":
    test()
