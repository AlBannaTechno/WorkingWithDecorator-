class DecodetWithoutArguments(object):
    def __init__(self,func):
        print("insied __init__")
        self.fun=func
        self.fun()

    # if we not defined __call__ special function
    # this program will start automaticly 
@DecodetWithoutArguments
def test():
    print("inside test")
