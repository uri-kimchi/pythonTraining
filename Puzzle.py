import os
import shutil
from zipfile import ZipFile
from colorama import Fore
import re

def check_re(pathName, fileName, searchRE):
    search_file = root+'/'+fileName
    fl = open (search_file,'r')
    tx = fl.read()
    fl.close()
    if len (re.findall( searchRE,tx))>0:
        return True
    else:
        return False




dir = os.getcwd()
dir = '/home/urik/Python38/Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/'
file_name = dir+'unzip_me_for_instructions.zip'
xdir = os.getcwd()+'/temp' 

shutil.unpack_archive(file_name,xdir)
print ('________________________________________________________________________________')
print("{}Archive file unpacked successfully. Extract directory {}".format(Fore.RED,xdir)) 
print ('________________________________________________________________________________')

i = 0
'''
for root,dirs,files in os.walk(xdir): 
    print ('{}\t ROOT:{}'.format(Fore.WHITE,root) )
    for d in dirs:
        print ('\t\t DIR:{}'.format(d))
    for f in files:
        print ('\t\t\t FILE:{}'.format(f))
print ('________________________________________________________________________________')
'''
for root,dirs,files in os.walk(xdir): 
    for f in files:
        i += 1
#        print ('\t\t\t {} ) PATH: {} FILE:{}'.format(i,root,f))
        if (check_re(root, f, r'\d\d\d-\d\d\d-\d{4}')):
            print ('Found in {} - {}'.format(root,f))
        else:
            pass

