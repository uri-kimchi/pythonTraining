import os
import shutil # shell utilities 
import datetime
import time
import flask # rest APIs
from collections import Counter
from collections import defaultdict
from numpy import broadcast_to # ML numbrr processing
import random
import re #regular expressions
import timeit # timing the code that is runing
import zipfile  #zipping files


if 'dog' in 'this is a dog og type...':
    print('dog it is')
else:
    print ('no dog here')

help (datetime.time.dst)
d = datetime.datetime( 2021,1,1,1,1,1,1)
print(d.ctime())
d = datetime.date.today()
print(d.ctime())

dir_name = 'c:\\temp\\root'

for p,d,f in os.walk(dir_name, topdown=True, 
):
    print (p)
    print (d)
    print (f)


#    for dd in d:
#        print ('  ',  dd)
#        for ff in f:
#           print('     ',ff)