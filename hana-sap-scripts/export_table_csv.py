#!/usr/bin/python
'''
Created on Apr 8, 2015

@author: I057588
'''
from hdbcli import dbapi

def execute_sql():
    print 'this is test'
    con = dbapi.connect('dubl60244901a.dhcp.dub.sap.corp',30115,'SYSTEM','Manager01')
    cur = con.cursor() 
    try:
        ret = cur.execute('SELECT TYPE_ID FROM "I4AA"."i4aa.db.schema::i4aadatamodel.READINGS"')
        #ret = cur.execute('SELECT CURRENT_UTCTIMESTAMP FROM DUMMY')
        ret = cur.fetchall()
        for row in ret:
            print row
    except dbapi.Error, err:
        print err
    cur.close()
    con.close()
    
def execute_sql1():
    con = dbapi.connect('10.78,113.19',30015,'I057588','Jan2015#')
    cur = con.cursor() 
    try:
        ret = cur.execute('SELECT TOP 1000 * FROM "I4AA"."MEASUREMENT_READING"')
        ret = cur.fetchall()
        for row in ret:
            print row
    except dbapi.Error, err:
        print err
    cur.close()
    con.close()
    

if __name__ == '__main__':
    execute_sql()