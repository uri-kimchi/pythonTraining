def args_test (n1,n2,*args, **kwargs):
    print ('n1 = {} n2 = {} together they are {}'.format(n1,n2,n1+n2))
    print(args*(n1+n2))
    print(sum(args)*(n1+n2))
    print(kwargs)
    print (xxx)
    #xxx = xxx *2 # this will generate an error as u cant assign out of scope variables, u can only iuse their data


def myfunc(*args):
    return( x for x in args if x%2 == 0)

def myfunc(st):
    rt = ""
    str(st).split()
    for i  in range (0,len(st)-1):
        if (i%2 == 0):
            rt  = rt + str(st[i].upper())
        else:
            rt = rt + str(st[i].lower())
    return (rt)


print (xx("qwertyuiop"))

xxx="qwerty"

args_test (1,2,100,200,300, shai = 1981, raz='1992', tal='1985')
print(xxx)

z = myfunc(1,2,3,4,5,6)

