import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

try:
    with open(fname) as fh:
        for line in fh:
            if not line.startswith('From: '):
                continue
            pieces = line.split()
            email = pieces[1]
            parts = email.split('@')
            org = parts[-1]

            cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
            row = cur.fetchone()
            if row is None:
                cur.execute('''INSERT INTO Counts (org, count)
                        VALUES (?, 1)''', (org,))
            else:
                cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

    conn.commit()

except FileNotFoundError:
    print('File not found:', fname)

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
