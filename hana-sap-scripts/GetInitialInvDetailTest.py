'''
Created on 6 Nov 2013

@author: i057588
'''
'''
Created on 7 Oct 2013

@author: i057588
'''
import unittest
from hdbcli import dbapi

class GetInitialInvDetailTest(unittest.TestCase):
    
    def __init__(self,*args, **kwargs):
        self.connection = None
        self.storedProc = 'CALL "_SYS_BIC"."sap.tdma.main.adjustments/SP_UPDATE_LABOR_RATES_ADJUST" ( ?,?)'
        self.deleteSql = 'DELETE FROM "SAP_TDMA_SCENARIOS"."sap.tdma.main.adjustments::LABOR_RATES_ADJUST"'
        super(GetInitialInvDetailTest, self).__init__(*args, **kwargs)
        
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
            cursor.close()
            self.connection.close()

    def testOverrideAdjustment(self):
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(self.storedProc);
            print res
            ret = cursor.fetchall()
            errorrows = 0
            for row in ret:
                errorrows=errorrows+1     
            self.assertEqual(0, errorrows)
            cursor.close()
        except dbapi.DatabaseError, error:
            print error
        finally:
            pass
        
if __name__ == "__main__":
    unittest.main()
