'''
Created on 27 Oct 2011

@author: i057588
'''
import glob
import shutil
import os

def delete_files():
    print('Deleting Files...')
    ljs_dir='/home/SAP_ALL/i057588/software/ljs'
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
    
if __name__ == '__main__':
    delete_files()