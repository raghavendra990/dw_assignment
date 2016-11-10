#URl Shortner like bitly

Basic idea is to store all url in Mysql database with unique primary key id and convert base 10 id value to base 62 value, and redirect url with that(eg. bit.ly/hGtM4M).

for this you have to install MySQLdb python client.

create any database with table name "url_table" and follwing fields.
id integer autoincrement 
urls text
created_on timestamp
<br>
or find url_table.sql file in the same folder and import in your database.

need to install "MySQLdb" mysql python client:

```
pip install MySQL-python
```

python code:

```python
import shortener
short = shortener.Shortener(host='localhost',user = 'root',password='098SJPrd&',database = 'textly')
short.shorten("www.facebook.com")  ## will store url in database and return primary_key in base 62.
short.real_url('cv')   ## will take base 62 key and convert in to base 10 and return the url where id = base 10 value.
```
