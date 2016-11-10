import string
import MySQLdb
letters = string.lowercase + string.uppercase+ string.digits

import shortener as s



# class shortener:
#     def __init__(self, host, user , password , database):
#         self.conn  =MySQLdb.connect(host=host,user = user,passwd=password,db = database)
#         self.c = self.conn.cursor()

#     def shorten(self, url):
#         print url
#         self.c.execute('INSERT into url_table ( urls ) VALUES ( "%s")'%(url) )
#         n = self.conn.insert_id()
#         self.conn.commit()
#         String = ""
#         while n > 0:
#             remainder = n%62
#             String  =  letters[remainder] + String
#             n = n/62
#         return String

#     def real_url(self ,String):
#         n = 0
#         String  = String[::-1]
#         length = len(String)

#         for i in range(length):
#             n = n + (62**i)*letters.index(String[i])
#         self.c.execute('select urls from url_table where id = %s'%(n))
#         url  = self.c.fetchone() 
#         url = None if url is None else url[0]
#         return url

