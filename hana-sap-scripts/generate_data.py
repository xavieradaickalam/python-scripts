'''
Created on 28 Jun 2013

@author: i057588
'''
import json

def generate_columns(noCol):
    columns = []
    for i in range(noCol):
        columns.append('USER_ATTRIBUTE_' + str(i))
    return columns

def generate_row(noRows,columns,filename):
    #row_data_= []
    try:
        f = open(filename, 'w')
        for i in range(noRows):
            row = {}
            row['ID'] = 'ROW_ID-C5-0000' + str(i)
            for col in columns:
                row[col] = col + '_DATA_ROW_' + str(i)
            #row_data.append(row)
            f.write(json.dumps(row, separators=(',',':')))
            f.write('\n')
    except IOError as e:
        print 'I/O error({0}): {1}'.format(e.errno, e.strerror)    
    finally:
        f.close()

if __name__ == '__main__':
    columns = generate_columns(10)
    generate_row(500,columns, 'test_data_row_500_colum_10_client_5.json')