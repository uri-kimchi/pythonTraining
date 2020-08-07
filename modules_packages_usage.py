import module1
import module2

from Package1 import Package1
from Package2 import Package2
from Package1.Package1Sub1 import PackageSub1,PackageSub1v2


if __name__ == "__main__":
    module1.m1f1()
    module2.m2f2()
    Package1.p1f1()
    Package1.p1f2()
    Package1.p1f3()
    Package2.p2f2()
    PackageSub1.p1s1f1()
    PackageSub1v2.p1s1f1v2()

