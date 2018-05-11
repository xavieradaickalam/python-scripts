#!/usr/bin/env python
'''
Created on 6 Dec 2011

@author: i057588
'''
import sys
import glob
import shutil
import os

def delete_files(ljs_dir):
    print('Deleting Files...')
    delete_directory(ljs_dir +'/pickup/*')
    delete_directory(ljs_dir +'/pickup/.*')
    delete_directory(ljs_dir +'/log/*')
    delete_directory(ljs_dir +'/webapps/*')
    delete_directory(ljs_dir +'/work/*')
    delete_directory(ljs_dir +'/configuration/*.log')
    print('Deleting Files...DONE')

def delete_directory(dir_name):
    files = glob.glob(dir_name)
    for f in files:
        if os.path.isdir(f):
            shutil.rmtree(f)
            print('Deleted Directory :'+f)
        else:
            os.remove(f)
            print('Deleted File :'+f)
    
def copy_file(from_dir,to_dir):
    files = glob.glob(from_dir + '/*.war')
    for f in files:
        print('Deploying file :' + f + ' to :' +to_dir)
        shutil.copy(f, to_dir)
         
if __name__ == '__main__':
    if(len(sys.argv) == 2):
        workspace_dir =  '/home/SAP_ALL/i057588/Perforce/XAVI_WORKSPACE/Projects/nova/dev' 
        ljs_dir       =  '/home/SAP_ALL/i057588/software/ljs'
        command       =  sys.argv[1]
        if(command == 'clean'):         
            delete_files(ljs_dir)
            exit(1)
        elif(command == 'deploy'):
            delete_files(ljs_dir)
            copy_file(workspace_dir+'/webapp/target',ljs_dir +'/pickup')
            exit(1)              
    elif(len(sys.argv) > 3):
        workspace_dir =  sys.argv[1] 
        ljs_dir       =  sys.argv[2] 
        command       =  sys.argv[3]
        if(command == 'clean'):         
            delete_files(ljs_dir)
            exit(1)
        elif(command == 'deploy'):
            delete_files(ljs_dir)
            copy_file(workspace_dir+'/webapp/target',ljs_dir +'/pickup')
            exit(1)       
    else:
        print('Usage   : python clean_deply.py <workspace_dir> <ljs_dir> <command>')
        print('Example : python clean_deply.py /home/SAP_ALL/i057588/Perforce/XAVI_WORKSPACE/Projects/nova/dev/ /home/SAP_ALL/i057588/software/ljs clean')
        sys.exit(1);        