# if we have arguments with the main decorator function
# make a function inside function
# this function-f2- load the external function
# f2 function will contain function -f3-
# f3 function will load variables of the external function

def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        print ("Inside wrap()")
        def wrapped_f(*args):
            print ("Inside wrapped_f()")
            print ("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print ("After f(*args)")
        return wrapped_f
    return wrap

@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print ('sayHello arguments:', a1, a2, a3, a4)

print ("After decoration")

print ("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print ("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print ("after second sayHello() call")
