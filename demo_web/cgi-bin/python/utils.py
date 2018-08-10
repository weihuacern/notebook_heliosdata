#!/usr/bin/python3.6
import random
import sys
sys.path.append('/home/helios/hua/lib/python3.6/site-packages')
sys.path.append('/usr/lib/cgi-bin')
import pymysql
import pymssql

CONN_FUNC = {'mysql': pymysql.connect, 'mssql': pymssql.connect}

SERVER = {'mysql': {'ip': '192.168.8.74',
                    'username': 'root',
                    'pwd': 'Helios123',
                    'port': 3306},
          'mssql': {'ip': '192.168.8.155',
                    'username': 'SA',
                    'pwd': 'Helios123',
                    'port': 1433}
          }

def fakesql(tablename, colnames, cutopt):
    selcol = ", ".join(set([colnames[random.randint(0, len(colnames)-1)] for i in range(3)]))
    if cutopt:
        cutstr = " where " + cutopt[random.randint(0, len(cutopt)-1)]
    else:
        cutstr = ""
    sqlstr = "select " + selcol + " from " + tablename + cutstr
    #print(sqlstr)
    return sqlstr

def insert_entry(sql, dbname, table, value):
    conn = CONN_FUNC.get(sql)(SERVER[sql]['ip'], SERVER[sql]['username'], SERVER[sql]['pwd'], dbname)
    c = conn.cursor()
    try:
        print('inserting %s to %s<br />' % (value, dbname))
        c.execute('INSERT INTO %s VALUES %s' % (table, value))
        print('insert succeed<br />')
    except Exception:
        print('failed to insert to %s.%s<br />' % (dbname, table))
    conn.commit()
    conn.close()


def get_query(sql, dbname, table, value, index='eid'):
    conn = CONN_FUNC.get(sql)(SERVER[sql]['ip'], SERVER[sql]['username'], SERVER[sql]['pwd'], dbname)
    c = conn.cursor()
    try:
        print('querying info from %s<br />' % dbname)
        c.execute('SELECT * FROM %s WHERE %s = %s;'% (table, index, value))
        print('info query succeed<br />')
        print(c.fetchall())
    except Exception:
        print('failed to get info from %s<br />' % dbname)

    conn.commit()
    conn.close()

def execute_query(sql, dbname, query):
    conn = CONN_FUNC.get(sql)(SERVER[sql]['ip'], SERVER[sql]['username'], SERVER[sql]['pwd'], dbname)
    c = conn.cursor()
    c.execute(query)
    try:
        print(c.fetchall())
    except Exception:
        pass

    conn.commit()
    conn.close()


if __name__ == "__main__":
    ms_ip = "192.168.7.155"
    ms_usrname = "SA"
    ms_pwd = "Helios123"
    ms_port = 1433
    ms_dbname = "hr_pii"
    value = "('" + '54321' + "', '" + 'Harry' + "', '" + '110' + "');"
    #insert_entry('mssql', ms_dbname, 'employee', value)
    #print('-----------------------<br />')
    #get_query('mssql', ms_dbname, 'employee', '54321')
    query = fakesql('payment', ['ssn', 'name', 'job', 'zipcode', 'city', 'state'], ["state = 'CA'", "state = 'WA'"])
    execute_query('mssql', 'hr_pii', query)
