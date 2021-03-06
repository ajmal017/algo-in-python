import sqlite3 as sql

def showalldata(dbname,tblname):
    conn = sql.connect(dbname)
    cur = conn.cursor()
    cur.execute('select * from '+ tblname)
    data = cur.fetchall()
    cur.close()
    conn.close()
    print(data)

def insertsingledata(dbname,tblname,rows):
    conn = sql.connect(dbname)
    cur = conn.cursor()
    values =' , '.join(map(str,rows))
    sqlsmt = "insert into {} (dates, price) values {}".format(tblname,values)
    print(sqlsmt)
    cur.execute(sqlsmt)
    cur.close()
    conn.commit()
    conn.close()
    print('Data inserted successfully')

# insert only new data and bypass already exists data
def insertAndUdateData(dbname,tblname,rows):
    i = 0
    for data in rows:
        i +=1 
        try:
            conn = sql.connect(dbname)
            cur = conn.cursor()
            # values =' , '.join(map(str,rows))
            sqlsmt = "insert into {} (dates, price) values {}".format(tblname,data)
            print(sqlsmt)
            cur.execute(sqlsmt)
            cur.close()
            conn.commit()
            conn.close()
            print(i,' -> Data inserted successfully')
        except:
            cur.close()
            conn.commit()
            conn.close()
            print(i,' -> Data already exists !')


# showalldata('test.db','price')
data = [(190114,266),(190113,256),(190114,243),(190115,256),(190103,259)]
# insertsingledata('test.db','price',data)



insertAndUdateData('test.db','price',data)