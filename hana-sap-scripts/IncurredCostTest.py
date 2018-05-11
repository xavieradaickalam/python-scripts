'''
Created on 10 Dec 2013

@author: i057588
'''
import unittest
from hdbcli import dbapi
from decimal import Decimal

class IncurredCostTest(unittest.TestCase):
    
    def __init__(self,*args, **kwargs):
        self.connection = None
        self.sql1 = 'SELECT * FROM "_SYS_BIC"."sap.tdca.main.outputs/CV_INCURRED_COST" (' \
                    +'\'PLACEHOLDER\' = (\'$$SCENARIO_HINT$$\', \'SFGBalance Adjustments\'),' \
                    +'\'PLACEHOLDER\' = (\'$$FIRST_PERIOD_HINT$$\', \'2013001\'),' \
                    +'\'PLACEHOLDER\' = (\'$$LAST_PERIOD_HINT$$\', \'2013001\')' \
                    +')' \
                    +'WHERE COST_COMPONENT_ID = \'Inbound Freight\' AND MOVEMENT_TYPE_ID = \'STO IN\' AND TRANS_ORIGIN_ID = \'PLANT SFG\''
        self.sql2 = 'SELECT * FROM "_SYS_BIC"."sap.tdca.main.outputs/CV_INCURRED_COST" (' \
                    +'\'PLACEHOLDER\' = (\'$$SCENARIO_HINT$$\', \'SFGBalance Adjustments\'),' \
                    +'\'PLACEHOLDER\' = (\'$$FIRST_PERIOD_HINT$$\', \'2013001\'),' \
                    +'\'PLACEHOLDER\' = (\'$$LAST_PERIOD_HINT$$\', \'2013001\')' \
                    +')' \
                    +'WHERE COST_COMPONENT_ID = \'Inbound Freight\' AND MOVEMENT_TYPE_ID = \'STO IN\' AND TRANS_ORIGIN_ID = \'PLANT B\''
                    
        self.sql3 = 'SELECT * FROM "_SYS_BIC"."sap.tdca.main.outputs/CV_INCURRED_COST" (' \
                    +'\'PLACEHOLDER\' = (\'$$SCENARIO_HINT$$\', \'SFGBalance Adjustments\'),' \
                    +'\'PLACEHOLDER\' = (\'$$FIRST_PERIOD_HINT$$\', \'2013001\'),' \
                    +'\'PLACEHOLDER\' = (\'$$LAST_PERIOD_HINT$$\', \'2013001\')' \
                    +')' \
                    +'WHERE COST_COMPONENT_ID = \'Inbound Freight\''            
        
        super(IncurredCostTest, self).__init__(*args, **kwargs)
        
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
'''
    def testIncurredCost1(self):
        print '-------------------test 1----------------------------'
        try:
            cursor = self.connection.cursor()
            res = cursor.execute(self.sql1);
            ret = cursor.fetchall()
            rows = 0
            for row in ret:
                print len(row)
                print row
                print row[0]
                print row[8]
                #HEAD_MATERIAL_ID
                self.assertEqual('SFG AB',row[8])
                print row[16]
                #LOCATION_ID
                self.assertEqual('PLANT B',row[16])
                print row[18]
                #COST_ORIGIN_ID
                self.assertEqual('PLANT B',row[18])
                print row[20]
                #TRANS_ORIGIN_ID
                self.assertEqual('PLANT SFG',row[20])
                print row[48]
                #HEADER_VOLUME
                self.assertEqual(Decimal('1722.5'),row[48])
                print row[49]
                #COST
                self.assertEqual(344500,row[49])
                print row[50]
                #HEADER_RATE
                self.assertEqual(200,row[50])
                print row[52]
                #INPUT_RATE
                self.assertEqual(200,row[52])
                rows=rows+1     
            cursor.close()
        except dbapi.DatabaseError, error:
            print error
        finally:
            pass

    def testIncurredCost2(self):
        print '--------------test 2-----------------------'
        try:
            cursor = self.connection.cursor()
            cursor.execute(self.sql2);
            ret = cursor.fetchall()
            rows = 0
            for row in ret:
                print len(row)
                print row
                rows=rows+1     
            cursor.close()
        except dbapi.DatabaseError, error:
            print error
        finally:
            pass
'''
    def testIncurredCost3(self):
        sql = 'SELECT SCENARIO_ID,HEAD_MATERIAL_ID,COMP_MATERIAL_ID,IP_MATERIAL_ID,INPUT_MATERIAL_ID,LOCATION_ID,COST_ORIGIN_ID,' \
              +'TRANS_ORIGIN_ID, MOVEMENT_TYPE_ID, HEADER_VOLUME,INPUT_VOLUME,COST,HEADER_RATE,INPUT_RATE FROM' \        
              + '\"_SYS_BIC\"."sap.tdca.main.outputs/CV_INCURRED_COST\"' \
              +'(' \
              + '\'PLACEHOLDER\' = (\'$$SCENARIO_HINT$$\', \'SFGBalance Adjustments\'),' \
              + '\'PLACEHOLDER\' = (\'$$FIRST_PERIOD_HINT$$\', \'2013001\'),' \
              + '\'PLACEHOLDER\' = (\'$$LAST_PERIOD_HINT$$\', \'2013001\')' \
              + ')' \
              +'WHERE COST_COMPONENT_ID = \'Inbound Freight\' ORDER BY HEAD_MATERIAL_ID,TRANS_ORIGIN_ID' \;
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql);
            ret = cursor.fetchall()
            rows = 0
            for row in ret:
                print len(row)
                print row
                rows=rows+1     
            cursor.close()
        except dbapi.DatabaseError, error:
            print error
        finally:
            pass        
        
if __name__ == '__main__':
    unittest.main()