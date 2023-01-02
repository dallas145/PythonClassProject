# import sqlite3

# conn = sqlite3.connect('ids.db')
# coursor = conn.execute('SELECT * FROM members')
# ids = coursor.fetchall()
# ids1 = dict((str(x), y) for x, y in ids)
# conn.close()

# print(ids1[str(2)])

f=open('member.txt','r')
names = f.readline().split(',')
print(names)