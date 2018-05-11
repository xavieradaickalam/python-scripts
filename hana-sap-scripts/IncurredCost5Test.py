'''
Created on 12 Dec 2013

@author: i057588
'''
'''
Created on 10 Dec 2013

@author: i057588
'''
import unittest
from hdbcli import dbapi

class IncurredCost5Test(unittest.TestCase):
    
    def __init__(self,*args, **kwargs):
        self.connection = None
        super(IncurredCost5Test, self).__init__(*args, **kwargs)
        
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

    def testIncurredCost3(self):
        sql = 'SELECT SCENARIO_ID,HEAD_MATERIAL_ID,COMP_MATERIAL_ID,IP_MATERIAL_ID,INPUT_MATERIAL_ID,LOCATION_ID,COST_ORIGIN_ID,' \
        +'TRANS_ORIGIN_ID,MOVEMENT_TYPE_ID,HEADER_VOLUME,INPUT_VOLUME,COST,HEADER_RATE,INPUT_RATE FROM ' \
        + '"_SYS_BIC"."sap.tdca.main.outputs/CV_INCURRED_COST"' \
        +'(' \
        + '\'PLACEHOLDER\' = (\'$$SCENARIO_HINT$$\', \'SFGBalance Adjustments\'),' \
        + '\'PLACEHOLDER\' = (\'$$FIRST_PERIOD_HINT$$\', \'2013001\'),' \
        + '\'PLACEHOLDER\' = (\'$$LAST_PERIOD_HINT$$\', \'2013001\')' \
        + ') ' \
        +' WHERE COST_COMPONENT_ID = \'Inbound Freight\' ORDER BY HEAD_MATERIAL_ID,TRANS_ORIGIN_ID '\
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql);
            ret = cursor.fetchall()
            rows = 0
            results = []            
            for row in ret:
                #print row
                rowDict = {}
                rowDict['SCENARIO_ID'] = row[0]
                rowDict['HEAD_MATERIAL_ID'] = row[1]
                rowDict['COMP_MATERIAL_ID'] = row[2]
                rowDict['IP_MATERIAL_ID'] = row[3]
                rowDict['INPUT_MATERIAL_ID'] = row[4]
                rowDict['LOCATION_ID'] = row[5]
                rowDict['COST_ORIGIN_ID'] = row[6]
                rowDict['TRANS_ORIGIN_ID'] = row[7]
                rowDict['MOVEMENT_TYPE_ID'] = row[8]
                rowDict['HEADER_VOLUME'] = row[9]
                rowDict['INPUT_VOLUME'] = row[10]
                rowDict['COST'] = row[11]
                rowDict['HEADER_RATE'] = row[12]
                rowDict['INPUT_RATE'] = row[13]
                print rowDict
                results.append(rowDict)
                rows = rows+1   
            cursor.close()
        except dbapi.DatabaseError, error:
            print error
        finally:
            pass        
        
if __name__ == '__main__':
    unittest.main()