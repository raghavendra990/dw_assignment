#key value data store server

I have built flask application and stroing key value pair in redis database using crud operation. Later we can host it anywhere.

Install redis in your machine using http://redis.io/topics/quickstart .

install some python dependacies:

```
pip install Flask
pip install redis
```
now run app.py file.

```
python app.py
```

if everything is fine then your application succefully start running on http://127.0.0.1:5000 .

Now python code for ADD, GET, DELETE key from server.

```python
import dataStorer

m = dataStorer.manage(host='http://127.0.0.1:5000') ## host in our case will be "http://127.0.0.1:5000", incase you have deployed on the server than host will change.

m.ADD(key= "student" , value = "raghav")     ##  m.ADD("student" , "raghav")
m.GET("student")
m.DELETE("student")
```
