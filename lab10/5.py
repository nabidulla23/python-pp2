import psycopg2


config = psycopg2.connect(
    host='localhost',
    database='postgres',
    port=5432,
    user='postgres',
    password='jaily6'
)

current = config.cursor()
sql1 = '''
 DELETE FROM phonebook WHERE username=' Papa';
'''

current.execute(sql1)

current.close()
config.commit()
config.close()