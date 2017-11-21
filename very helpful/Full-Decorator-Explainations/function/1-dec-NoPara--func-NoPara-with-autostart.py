def function(func):
    print("Start")
    func()
    print("End")

@function
def fun():
    print("Inside fun")

# this program will start automaticly

# if __name__=="__main__":
#     fun()