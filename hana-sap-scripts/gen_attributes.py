'''
Created on 26 Jun 2013

@author: i057588
'''
import json

def generate_data(): 
    data_set = []
    data_columns = [50,100,200,500,1000,3000,5000]
    #data_columns = [1]
    data_colunm_names = []
    data_record = {}
    previous_col=0
    try :
        for j in data_columns:
           column_names = [] 
           #for k in range(previous_col,j):
           for k in range(j):
              column_names.append('ATTRIBUTE_T1_' + str(k))
           data_colunm_names.append(column_names)
           #previous_col=j
        count=0;   
        for columns in data_colunm_names:   
            data_record = {}
            data_record['ID'] = 'ID-0001'
            for a in columns:
                data_record[a] = a + '-DATA'
            data_set.append(data_record)
            f = open('data_'+ str(data_columns[count])+'.json','w')
            f.write(json.dumps(data_record, separators=(',',':')))
            f.close()
            count = count +1
    except IOError:
        pass
if __name__ == '__main__':
    generate_data()