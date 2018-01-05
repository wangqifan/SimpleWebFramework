import sqlite3
from src.User import user
from src.utils import log
path='../Data/test.db'

#conn = sqlite3.connect('../Data/test.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE users
 #      (ID      INTEGER PRIMARY KEY   AUTOINCREMENT,
 #      NAME           TEXT    NOT NULL,
 #        EMAIL         Text     NOT NULL,
 #      PHONENUMBER      tEXT  NOT NULL);''')
#conn.commit()
#conn.close()


def insert(user):
  #  try:
        conn = sqlite3.connect(path)
        c = conn.cursor()
        cmd='insert into users(name,email,phonenumber) VALUES(\'{0}\',\'{1}\',\'{2}\')'.format(user.name,user.email,user.phonenumber)
        log(cmd)
        c.execute(cmd)
        conn.commit()
        conn.close()
        log("insert success {}".format(user.name))
       # return True
   # except:
      #  return False

def loadalluser():
    try:
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute('select *  from users')
        lines = c.fetchall()
        log(str(len(lines))+'-------------')
        conn.commit()
        conn.close()
        return lines
    except:
        return ()

def deletebyid(id):
 #  try:
        conn = sqlite3.connect(path)
        c = conn.cursor()
        c.execute('DELETE from users where id={}'.format(id))
        conn.commit()
        conn.close()
        return True
   # except:
    #    return  False