from Package1.Package1Sub1 import PackageSub1,PackageSub1v2
from Package2 import Package2

def p1f1 ():
    print("Package 1 Function 1")
    PackageSub1.p1s1f2()
def p1f2 ():
    print("Package 1 Function 2")
    Package2.p2f2()
def p1f3 ():
    print("Package 1 Function 3")
    