def function(*args):# receive tfunc
    print("Start function")
    print(args)
    def tfuncReciver(func): # receive func
        print("Start tfuncReciver")
        def tfuncParaRec():# receive func arguments
            # we can't remove tfuncPararec evenif func
            # haven't any argument
            # because we must have three steps functions
            # if we need to pass  a parameters to the main function'function'
            print("start tfuncParaRec")
            func()
            print("end tfuncParaRec")
        return tfuncParaRec
    return tfuncReciver

@function("start from here",2016)
def tfunc():
    print("inside tfunc")

if __name__=="__main__":
    tfunc() # we can not passing any argument

# last programm wil start auto maticly













#
# def function(*args):# receive tfunc
#     print("Start function")
#     print(args)
#     def tfuncReciver(func):
#         print("Start tfuncReciver")
#         func()
#     return tfuncReciver
#
# @function("start from here",2016)
# def tfunc():
#     print()
#
# if __name__=="__main__":
#     tfunc()
#
# # last programm wil start auto maticly