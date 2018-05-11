'''
Created on 24 Jan 2014

@author: Xavier Adaickalam
@note: execute_caommand.py
'''
import os
import shutil
import tarfile
import glob
import subprocess

def delete_files(ljs_dir):
    print('Deleting Files...')
    delete_directory(ljs_dir +'/*')
    print('Deleting Files...DONE')

def delete_directory(dir_name):
    print("Deleting " + dir_name)
    files = glob.glob(dir_name)
    for f in files:
        if os.path.isdir(f):
            shutil.rmtree(f)
            print('Deleted Directory :'+f)
        else:
            os.remove(f)
            print('Deleted File :'+f)

def extract_tar(filename,to_dir):
    print('Extracting :'+filename + ' to ' + to_dir)
    tfile = tarfile.open(filename,'r') 
    for tarinfo in tfile:
        #print(tarinfo.name)
        tfile.extract(tarinfo,to_dir)             
    #tfile.exctractall()    
    tfile.close()
    print('Completed Extraction :'+filename)
    
def copy_file(from_dir,to_dir):
    files = glob.glob(from_dir + '/*.war')
    for f in files:
        print('Copying file :' + f + ' to :' +to_dir)
        shutil.copy(f, to_dir)

def run_command(cmd,directory):
    subprocess.check_call(cmd,cwd=directory)
    
if __name__ == '__main__':
    cmd1 = [ 'ls', '-a']
    run_command(cmd1,'.')