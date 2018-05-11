'''
Created on 7 Oct 2013

@author: i057588
'''
import unittest
from hdbcli import dbapi

class LaborRatesTest(unittest.TestCase):
    
    def __init__(self,*args, **kwargs):
        self.connection = None
        self.insertGtmpSql = 'INSERT INTO "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST" \
                  (QUALIFIER, MEASURE,AT_SCENARIO, AT_PERIOD,AT_LOCATION, AT_COST_CENTER, AT_CURRENCY,RATE_DELTA,PERCENTAGE_DELTA,OVERRIDE_RATE) \
                   VALUES (?,?,?,?,?,?,?,?,?,?)'
        self.truncateSql = 'TRUNCATE TABLE "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST"'
        self.storedProc = 'CALL "_SYS_BIC"."sap.tdma.main.adjustments/SP_UPDATE_LABOR_RATES_ADJUST" ( "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::GTMP_LABOR_RATES_ADJUST", ?)'
        self.deleteSql = 'DELETE FROM "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::LABOR_RATES_ADJUST"'
        super(LaborRatesTest, self).__init__(*args, **kwargs)
        
    def setUp(self):
        try:
            self.connection = dbapi.connect('dubl60244901a.dhcp.dub.sap.corp',30115,'SYSTEM','Manager01')
            self.connection.setautocommit(auto=True) 
        except dbapi.Error, error:
            print error
        finally:
            pass

    def tearDown(self):
        if self.connection <> None:
            cursor = self.connection.cursor()
            cursor.execute(self.deleteSql)
            cursor.close()
            self.connection.close()

    def testOverrideAdjustment(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.truncateSql)
            cursor.execute(self.insertGtmpSql,('0', 'OVERRIDE_RATE', 'SFGBalance Adjustments', '2013001','PLANT A','COST CENTER A','USD',0,0,0.06))
            res = cursor.execute(self.storedProc);
            print res
            ret = ret = cursor.fetchall()
            errorrows = 0
            for row in ret:
                print row
                errorrows=errorrows+1     
            self.assertEqual(0, errorrows)
            cursor.close()
        except dbapi.DatabaseError, error:
            print error
        finally:
            pass

    def testOverrideAdjustmentMinus(self):
            try:
                cursor = self.connection.cursor()
                cursor.execute(self.truncateSql)
                cursor.execute(self.insertGtmpSql,('1', 'OVERRIDE_RATE', 'SFGBalance Adjustments', '2013001','PLANT A','COST CENTER A','USD',0,0,-0.06))
                res = cursor.execute(self.storedProc);
                print res
                ret = ret = cursor.fetchall()
                errorrows = 0
                for row in ret:
                    print row
                    errorrows=errorrows+1     
                self.assertEqual(1, errorrows)
                cursor.close()
            except dbapi.DatabaseError, error:
                print error
            finally:
                pass
        
if __name__ == "__main__":
    unittest.main()
    