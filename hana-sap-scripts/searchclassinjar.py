#!/usr/bin/env python
'''
Created on 30 Nov 2011

@author: Xavier Adaickalam
'''
import sys
import os
import zipfile

resultlist = []
def find_class(jar_file,class_name):
    zf = zipfile.ZipFile(jar_file, 'r')
    try:
        lst = zf.infolist()
        for zi in lst:
            fn = zi.filename
            if fn.find(class_name) != -1:
                resultlist.append(fn + ' found in jar : '+jar_file);                               
    finally:
        zf.close()

def walk(dir_name,class_name):
    basedir = dir_name
    subdirlist = []
    for f in os.listdir(dir_name):        
        if os.path.isfile(os.path.join(basedir,f)):
            if f.endswith('.jar'):
                find_class(os.path.join(basedir,f),class_name)    
        else:
            tempdir=os.path.join(basedir,f)
            if os.path.isdir(tempdir):
                subdirlist.append(tempdir)
    for subdir in subdirlist:
        walk(subdir,class_name)

def main(dir_name,class_name):
    walk(dir_name,class_name)
    if(len(resultlist) > 0) : 
        for result in resultlist:
            print(result + '\n')
    else:
        print(class_name + ' does not found in ' + dir_name + ' and its sub directories.\n')
            
if __name__ == '__main__':
    if(len(sys.argv) > 2):
        dir_name =  sys.argv[1] 
        class_name = sys.argv[2]
        main(dir_name,class_name)
    else:
        print('Usage   : python searchclassinjar.py <dir> <classname>')
        print('Example : python searchclassinjar.py /home/xavier/temp Abc.class')
        sys.exit(1)         