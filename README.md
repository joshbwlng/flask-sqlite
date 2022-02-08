# flask-mongo

Example app for adding/viewing/deleting users stored in an SQLite database.  
Python + Flask, runs on Balena.

Backend service listens on port 3001, while frontend service listens on port 80.  
The frontend service, when accessed with `http://<DEVICE-IP>/` should display `Hello from backend`, a message retrieved from the backend service.

**Add user to database**
```
curl -d '{"name":"foo","email":"bar@example.com"}' -H "Content-Type: application/json" -X POST http://<YOUR-IP>:3001/api/users
```

**Query for users by name**
```
curl http://<YOUR-IP>:3001/api/users\?name\=foo
```

**Delete stored user by name**
```
curl -X DELETE http://<YOUR-IP>:3001/api/users\?name\=foo
```
