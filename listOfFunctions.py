def fo():
    print("fo")
def foo(p):
    print("foo "+str(p))
def retf(f1,f2):
    v=[]
    v.append(f1)
    v.append(f2)
    return v
st=retf(fo,foo)
st[0]()
st[1](" Hi")


def clsav(*args):
    save=[]
    for c in args:
        save.append(c)
    return save

class os(object):
    def bs(self,var):
        print("os bs %s "%var)
    def bbs(var):
        print("os bbs %s"%var)

class cs(object):
    def bs(self,var):
        print("cs bs %s "%var)
    def bbs(self,var):
        print("cs bbs %s"%var)
res=clsav(os,cs)
res[0].bs(None,"ff")# we put None instead of self because we haven't variable
# contain our calss
# as next
os.bs("asdasdsa","23")
# so the first argument will ignored always
res[0].bbs("ff")# also we can remove self as bbs from os
res[1].bs(None,"ff")
res[1].bbs(None,"ff")

