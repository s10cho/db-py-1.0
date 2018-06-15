import cx_Oracle
import os
import yaml

conf_file = open('../conf/config.yml', 'r')
conf = yaml.load(conf_file)
conf_file.close()

'''
한글 깨짐
os.putenv('NLS_LANG', '.UTF8')
os.putenv('NLS_LANG', 'KOREAN_KOREA.KO16KSC5601')
'''
os.putenv('NLS_LANG', '.UTF8')

dsn = cx_Oracle.makedsn(conf['database']['ip'], conf['database']['port'], conf['database']['sid'])
db = cx_Oracle.connect(conf['database']['id'], conf['database']['pw'], dsn)
cursor = db.cursor()

cursor.execute('select * from test')
row = cursor.fetchone()
while row:
    data = [
        str(row[0]),
        str(row[1]),
        str(row[2]),
        str(row[3]),
        str(row[4])
    ]
    print(row)
    row = cursor.fetchone()



