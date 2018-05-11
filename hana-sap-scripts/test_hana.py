'''
Created on 14 Nov 2012

@author: i057588
'''
from hdbcli import dbapi

def execute_stored_proc():
    try:
        con = dbapi.connect('dubl60244901a.dhcp.dub.sap.corp',30015,'SYSTEM','Manager00')
        cur = con.cursor() 
        cur.callproc("\"EXPENSE_XAVI\".\"EPMIM_EXP_SP_GET_SEARCH_HELP\"", ('KTOPL','*Chart of accounts - United States','E','100',''))
        ret = cur.fetchall()
        for row in ret:
            print row
        cur.close()
        con.close()
    except dbapi.Error,err:
        print err

def execute_sql(sql=None):
    con = dbapi.connect('dubl60244901a.dhcp.dub.sap.corp',30115,'SYSTEM','Manager01')
    cur = con.cursor() 
    try:
        ret = cur.execute("SELECT CURRENT_TIMESTAMP FROM DUMMY")
        ret = cur.fetchall()
        for row in ret:
            print row
    except dbapi.Error, err:
        print err
    cur.close()
    con.close()

def execute_stored_proc_as_sql():
    try:
        con = dbapi.connect('dubl60244901a.dhcp.dub.sap.corp',30015,'SYSTEM','Manager00')
        cur = con.cursor() 
        cur.execute("CALL \"EXPENSE_XAVI\".\"EPMIM_EXP_SP_GET_SEARCH_HELP\"(?,?,?,?,?)", ('KTOPL','*Chart of accounts - United','E','100',''))
        ret = cur.fetchall()
        for row in ret:
            print row
        cur.close()
        con.close()
    except dbapi.Error,err:
        print err
        
def execute_test():
    con = None
    try:
        con = dbapi.connect('dubl60244901a.dhcp.dub.sap.corp',30115,'SYSTEM','Manager01')
        con.setautocommit(auto=True) 
        if(con != None):
            print 'I got the connection'
            sql = 'INSERT INTO "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST" \
                  (QUALIFIER, MEASURE,AT_SCENARIO, AT_PERIOD,AT_LOCATION, AT_COST_CENTER, AT_CURRENCY,RATE_DELTA,PERCENTAGE_DELTA,OVERRIDE_RATE) \
                   VALUES (?,?,?,?,?,?,?,?,?,?)'
            cur = con.cursor();
            res = cur.execute('TRUNCATE TABLE "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST"')
            #res = cur.execute('DELETE FROM "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::LABOR_RATES_ADJUST"')
            print res
            res = cur.execute(sql, ('Qualifier1', 'OVERRIDE_RATE', 'SFG FG Adjustment Scenario', '2013001','PLANT A','COST CENTER A','USD',0,0,-0.06))
            print res
            res = cur.execute('SELECT * FROM "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST"')
            ret = cur.fetchall()
            for row in ret:
                print row
            #CALL "_SYS_BIC"."sap.tdma.main.adjustments/SP_UPDATE_LABOR_RATES_ADJUST" ( "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST", ?)    
            #ret = cur.callproc('"_SYS_BIC"."sap.tdma.main.adjustments/SP_UPDATE_LABOR_RATES_ADJUST"',( '"SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST"', ''))
            ret = cur.execute('CALL "_SYS_BIC"."sap.tdma.main.adjustments/SP_UPDATE_LABOR_RATES_ADJUST" ( "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST", ?)')
            ret = cur.fetchall()
            for row in ret:
                print row
            res = cur.execute('TRUNCATE TABLE "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST"')    
            res = cur.execute('DELETE FROM "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::LABOR_RATES_ADJUST"')
    except dbapi.Error, err:
        print err
    finally:
        con.close()    

if __name__ == '__main__':
    execute_test()
