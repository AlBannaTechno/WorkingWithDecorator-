def func(*mn):# also we can use predefine object *args
    for a in mn:
        print(a)
        try:
            for s in a:
                print(s)
        except:
            print("No Child")
a =range(10,20)

# func(2,(a for a in range(10,20)))

func() # we also can no passing any thing