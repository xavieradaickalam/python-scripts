#!/usr/bin/env python
'''
Created on 11 Feb 2013

@author: i057588
'''
import glob
import os
import shutil
import subprocess
import sys

def delete_folder_content(dir_name):
    files = glob.glob(dir_name)
    for f in files:
        if os.path.isdir(f):
            shutil.rmtree(f)
            print('Deleted Directory :'+f)
        else:
            os.remove(f)
            print('Deleted File :'+f)
            
def run_command(cmd,directory):
    subprocess.check_call(cmd,cwd=directory)
             
if __name__ == '__main__':
    sap_dir = '/usr/sap'
    hana_instance = 'XA1'
    home_dir =  '/home/SAP_ALL/i057588' 
    db_inst_cmd = [ './hdbuninst']
    run_command(db_inst_cmd,sap_dir+'/'+hana_instance +'/SYS/global/hdb/install/bin')
    run_command(db_inst_cmd,sap_dir+'/hdbstudio/install')
    run_command(db_inst_cmd,sap_dir+'/hdbclient/install')
    delete_folder_content('/usr/sap/*')
    delete_folder_content(home_dir +'/*.log')
    run_command(['rm','-rf', 'hdbstudio'],home_dir)
    exit(1) 
    