from hdbcli import dbapi

if __name__ == '__main__':
    try:
        con = dbapi.connect('dubl60244901a.dhcp.dub.sap.corp',30215,'SYSTEM','Manager02')
        con.setautocommit(False);
        cur = con.cursor() #Open a cursor  
        filecontent = open('/home/SAP_ALL/i057588/docs/newdb/HANA1_DEV_sql_en.pdf', 'rb') #Open file in read-only and binary   
        content = filecontent.read() #Save the content of the file in a variable  
        cur.execute("INSERT INTO \"SAP_HANA_XSDB\".\"xstextapp.db::CONTENT_SOURCE\" VALUES(?,?,?)", ('1234567','HANA1_DEV_sql_en.pdf',content)) #Save the content to the table  
        filecontent.close() #Close the file  
        cur.close() #Close the cursor  
        con.commit();
        con.close() #Close the connection  
    except dbapi.Error,err:
        print err