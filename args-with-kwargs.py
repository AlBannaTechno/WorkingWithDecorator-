def multifunc(*args,**kwargs):
    for arg in args:
        print("%s  is arg"%arg)
    for key in kwargs:
        print(str(key)+" : "+str(kwargs[key]))


# multifunc() # we also can no passing any thing

multifunc(23,45,345,345,a=343,c=3443,osama=543)
# multifunc(a=3432,c=343)
# multifunc(34,4234,345,345)
# multifunc(a=3423,34543) # it's forbidden because args must be before kwarg
# otherwise we need to edit this function to be

# def multifunc(**kwargs,*args): # but it's also forbidden  because * must be
# before **

