'''
Created on 25 Oct 2012

@author: i057588
'''

import subprocess

def build_all():
    um_build_cmd = [ 'mvn', '-gs', 'settings-ldi.xml','-s','settings.local.xml','-Pdatabase-xavier,dbdeploy','clean','install']
    run_command(um_build_cmd,'/home/SAP_ALL/i057588/git-new/epmim.decapitator')
    exp_build_cmd = ['mvn','-gs','settings.xml','-s','settings.local.xml','clean','install','-Pdatabase-xavier']
    run_command(exp_build_cmd,'/home/SAP_ALL/i057588/git-new/epmim.expensinator')

def run_command(cmd,directory):
    subprocess.check_call(cmd,cwd=directory)

if __name__ == '__main__':
    build_all()