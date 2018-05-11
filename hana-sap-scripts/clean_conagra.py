'''
Created on 4 Oct 2013

@author: i057588
'''
import subprocess

def run_command(cmd,directory):
    subprocess.check_call(cmd,cwd=directory)
    
def undeploy_deliveryunit():
    #regi undeploy deliveryUnit HCO_MSP_CORE sap.com --key=KEYTDMA
    contractDU = ['regi','undeploy','deliveryUnit','HCO_TDMA_CONTRCT','sap.com','--key=KEYTDMA']
    customerDU = ['regi','undeploy','deliveryUnit','HCO_TDMA_CUST','sap.com','--key=KEYTDMA']
    mainDU = ['regi','undeploy','deliveryUnit','HCO_TDMA_MAIN','sap.com','--key=KEYTDMA']
    testDU = ['regi','undeploy','deliveryUnit','HCO_TDMA_TEST','sap.com','--key=KEYTDMA']
    directory='/home/SAP_ALL/i057588'
    run_command(testDU,directory)
    run_command(customerDU,directory)
    run_command(mainDU,directory)
    run_command(contractDU,directory)
     
if __name__ == '__main__':
    undeploy_deliveryunit()