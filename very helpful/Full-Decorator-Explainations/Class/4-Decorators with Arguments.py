class decoratorWithArguments(object):

    def __init__(self,*args,**kwargs):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("insied __init__")
        print(args)
        print(kwargs)
    def __call__(self,func):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        """
        All operation that's write here before RecArg function
        Will calling once
            at writing @ operatore "@ClassName(....)"
            or at calling the function
        but the operations which writen
            inside RecArg Function Will execute
            whenever the test() function is called
        So when We calling test() function more once
        "Inside __call__" : statement will shown
            once (1)
        because it's out of RecArg() function
        """
        print("Inside __call__")
        self.fun=func# we can ignore this line with remove self from
                        # self.fun()
        def RecArg(*args,**kwargs):
            print("RecArg")
            self.fun(args,kwargs)
        return RecArg


@decoratorWithArguments(65,67,56,he="Hello",We="Welcome")
def test(args,kwargs):
    print("inside test")
    print(args)
    print(kwargs)

# Warn When We use decorator with class by __init__ and __call__
# our class will initialize automatic
# even if we didn't call our decorated function like test()
# it's mean that __call__  and __init__ will auto calling once when we do @classname
# but when we actualy calling the function test(....)
# the __call__ will called another once .....
# to notes this thing please comment the next  two lines
    """
    Warn :
        if we not calling the test function at any place
        in our program"Like commenting if __name_..... lines"
        : the class will calling __init__ and __call__ once
        --But :
            if we call test function once or more at our program
            the class will calling __init__ only once
            at decoration defenition @className(...)
            but __call__ will not call after __init__
            but will call when we call the function "test"
    We say this to prevent a mix of thinking about dublicated
    operation 'calling __call_ twice '
        once with @className(...)
            and another once with calling function -test()-
    but __call__
    will calling once with calling test() function
    or with the number of calling operations for test() function
    """
if __name__=="__main__":
    test(23,34,54,os="osama",no="Nor")# we can pass paras or nots
    print("Seond once __Call__ caling")
    test(54, 78, "bvbnfg", os="osama", no="Nor")