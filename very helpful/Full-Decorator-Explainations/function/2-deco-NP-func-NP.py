def function(func):
    print("Start function")
    def test():
        print("Start Test")
        func()
        print("End Test")
    return test

@function
def tfunc():
    print("Inside tfunc")

if __name__=="__main__":
    tfunc()