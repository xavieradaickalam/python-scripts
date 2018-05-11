'''
Created on 24 Jul 2013

@author: i057588
@note: genetate_data_csv.py
'''
import csv

def generate_data(): 
    try:
        f = open('data.csv', 'wb')
        data_set = []
        data_props = ['ID','NAME','FIRST_NAME','LAST_NAME','MIDDLE_NAME','NICK_NAME','PROFILE','PICTURE',\
                    'WEBSITE','EMAIL', 'EMAIL_VERIFIED', 'GENDER', 'DATE_OF_BIRTH', 'ZONEINFO', \
                    'LOCALE','PHONE_NUMBER','STREET_ADDRESS','CITY','REGION','COUNTRY','POSTAL_CODE',\
                    'MARITAL_STATUS']
        try :
            contentwriter = csv.writer(f,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(100):
                for a in data_props:
                    data_set.append(a + '-'  + str(i))
                contentwriter.writerow(data_set)
                data_set=[]
        finally:
            f.flush()
            f.close();
    except IOError:
        pass
if __name__ == '__main__':
    generate_data()