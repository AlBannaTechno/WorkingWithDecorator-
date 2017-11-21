def kwArgs(**multikargs):# we can also use predefine object kwargs
    for key in multikargs:
        print(str(key) +" : " + str(multikargs[key]))

#kwArgs(a=23,b=343,c="3432")
kwArgs()# we also can no passing any thing