#!/usr/bin/python
'''
Created on 15 Aug 2012

@author: i057588
'''
import os
import shutil
import tarfile
import sys
import glob
import subprocess

def delete_files(ljs_dir):
    print('Deleting Files...')
    delete_directory(ljs_dir +'/*')
    print('Deleting Files...DONE')

def delete_directory(dir_name):
    print_comment("Deleting " + dir_name)
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

def print_comment(comment):
    print("------------------------------------------------------------------------")
    print(comment)
    print("------------------------------------------------------------------------")
            
def deploy_artifacts(um_dir,exp_dir,ljs_dir):
    print_comment("Deploying artifacts...")    
    extract_tar(um_dir + '/Install/deliveries/target/capex-deliveries-12.2.0-MAKO-SNAPSHOT.tar',ljs_dir)
    print('Copying file : ' + exp_dir +'/core/target/expensinator-core-12.2.0-SNAPSHOT.jar' + '  to ' + ljs_dir +'/plugins')
    shutil.copy(exp_dir +'/core/target/expensinator-core-12.2.0-SNAPSHOT.jar', ljs_dir +'/plugins')
    print('Copying file : ' + exp_dir +'/web/target/expensinator-web-12.2.0-SNAPSHOT.war' + '  to ' + ljs_dir +'/pickup')
    shutil.copy(exp_dir +'/web/target/expensinator-web-12.2.0-SNAPSHOT.war', ljs_dir +'/pickup')
    print('Copying file : ' + '/home/SAP_ALL/i057588/workspace/scripts/props.ini' +' to ' + ljs_dir)
    shutil.copy('/home/SAP_ALL/i057588/workspace/scripts/props.ini', ljs_dir)
    print("Complete deploying artifacts...")

def build_all(um_dir,exp_dir):
    um_build_cmd = [ 'mvn', '-gs', 'settings-ldi.xml','-s','settings.local.xml','-Pdatabase-xavier,dbdeploy','clean','install']
    run_command(um_build_cmd,um_dir)
    exp_build_cmd = ['mvn','-gs','settings.xml','-s','settings.local.xml','clean','install','-Pdatabase-xavier']
    run_command(exp_build_cmd,exp_dir)
    
def build_nodb(um_dir,exp_dir):
    um_build_cmd = [ 'mvn', '-gs', 'settings-ldi.xml','-s','settings.local.xml','-Pdatabase-xavier,dbdeploy','clean','install','-pl','expensinator-admin-core,expensinator-admin-ui,java/sop-webapp,Install/deliveries','-am' ]
    run_command(um_build_cmd,um_dir)
    exp_build_cmd = ['mvn','-gs','settings.xml','-s','settings.local.xml','clean','install','-Pdatabase-xavier','-pl','core,web','-am']
    run_command(exp_build_cmd,exp_dir)
    
def build_nodb_notest(um_dir,exp_dir):
    um_build_cmd = [ 'mvn', '-gs', 'settings-ldi.xml','-s','settings.local.xml','-Pdatabase-xavier,dbdeploy','clean','install','-DskipTests','-pl','expensinator-admin-core,expensinator-admin-ui,java/sop-webapp,Install/deliveries','-am' ]
    run_command(um_build_cmd,um_dir)
    exp_build_cmd = ['mvn','-gs','settings.xml','-s','settings.local.xml','clean','install','-Pdatabase-xavier','-DskipTests','-pl','core,web','-am']
    run_command(exp_build_cmd,exp_dir)    

def run_command(cmd,directory):
    subprocess.check_call(cmd,cwd=directory)
    
if __name__ == '__main__':
    if(len(sys.argv) == 2):
        um_dir =  '/home/SAP_ALL/i057588/git-new/epmim.decapitator'
        exp_dir = '/home/SAP_ALL/i057588/git-new/epmim.expensinator' 
        ljs_dir = '/home/SAP_ALL/i057588/software/ljs'
        command = sys.argv[1]
        if(command == 'clean'):         
            delete_files(ljs_dir)
            exit(1)
        elif(command == 'deploy'):
            delete_files(ljs_dir)
            deploy_artifacts(um_dir,exp_dir,ljs_dir)            
            exit(1)  
        elif(command == 'all'):
            build_all(um_dir,exp_dir)
            delete_files(ljs_dir)
            deploy_artifacts(um_dir,exp_dir,ljs_dir)            
            exit(1)
        elif(command == 'nodb'):
            build_nodb(um_dir,exp_dir)
            delete_files(ljs_dir)
            deploy_artifacts(um_dir,exp_dir,ljs_dir)            
            exit(1)
        elif(command == 'nodbnotests'):
            build_nodb_notest(um_dir,exp_dir)
            delete_files(ljs_dir)
            deploy_artifacts(um_dir,exp_dir,ljs_dir)            
            exit(1)    
    elif(len(sys.argv) >= 4):
        um_dir  =  sys.argv[1] 
        exp_dir =  sys.argv[2] 
        ljs_dir =  sys.argv[3]
        command =  sys.argv[4]
        if(command == 'clean'):         
            delete_files(ljs_dir)
            exit(1)
        elif(command == 'deploy'):
            delete_files(ljs_dir)
            deploy_artifacts(um_dir,exp_dir,ljs_dir)
            exit(1)
        elif(command == 'all'):
            build_all(um_dir,exp_dir)
            delete_files(ljs_dir)
            deploy_artifacts(um_dir,exp_dir,ljs_dir)            
            exit(1)
        elif(command == 'nodb'):
            build_nodb(um_dir,exp_dir)
            delete_files(ljs_dir)
            deploy_artifacts(um_dir,exp_dir,ljs_dir)            
            exit(1)                                 
    else:
        print('Usage   : python build_deploy.py <um_dir> <exp_dir> <ljs_dir> [all|nodb|clean]')
        print('Example : python build_deploy.py  /home/SAP_ALL/i057588/git/epmim.decapitator /home/SAP_ALL/i057588/git/epmim.expensinator /home/SAP_ALL/i057588/software/ljs all')
        print('Example : python build_deploy.py  /home/SAP_ALL/i057588/git/epmim.decapitator /home/SAP_ALL/i057588/git/epmim.expensinator /home/SAP_ALL/i057588/software/ljs nodb')
        print('Example : python build_deploy.py  /home/SAP_ALL/i057588/git/epmim.decapitator /home/SAP_ALL/i057588/git/epmim.expensinator /home/SAP_ALL/i057588/software/ljs clean')
        sys.exit(1); 
