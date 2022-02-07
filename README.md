# flask-mongo

Example app for adding/viewing/deleting users stored in an SQLite database.  
Python + Flask, runs on Balena.

**Add user to database**
```
curl -d '{"name":"foo","email":"bar@example.com"}' -H "Content-Type: application/json" -X POST http://<YOUR-IP>
```

**Query for users by name**
```
curl http://<YOUR-IP>\?name\=foo
```

**Delete stored user by name**
```
curl -X DELETE http://<YOUR-IP>\?name\=foo
```
