def function(func):# receive tfunc
    print("Start function")
    def test(*args):# receive parameters of tfunc
        print("Start Test")
        func(*args)# exceute of tfunc
        print("End Test")
    return test

@function
def tfunc(*args):
    print(args)

if __name__=="__main__":
    tfunc("asdas",234)