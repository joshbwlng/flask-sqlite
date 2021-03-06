import json
import os
from pathlib import Path
import sqlite3
from flask import Flask, request, g

DATABASE = os.path.join(os.getcwd(), 'database.db')
if not os.path.isfile(DATABASE):
    print('Touching db:', DATABASE)
    Path(DATABASE).touch()

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        cur = db.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS users (name text, email text)')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/api', methods=['GET'])
def hello_world():
    return json.dumps({'message': 'Hello from backend'})

@app.route('/api/users', methods=['GET'])
def query_records():
    cur = get_db().cursor()
    name = request.args.get('name')
    cur.execute("SELECT name,email FROM users WHERE name=:name", {"name": name})
    results = cur.fetchall()
    return json.dumps(results)

@app.route('/api/users', methods=['POST'])
def create_record():
    con = get_db()
    cur = con.cursor()
    data = json.loads(request.data)
    name = data['name']
    email = data['email']
    cur.execute("INSERT INTO users (name,email) VALUES (?, ?)", (name, email))
    con.commit()
    cur.execute("SELECT name,email FROM users WHERE name=:name", {"name": name})
    results = cur.fetchall()
    return json.dumps(results)

@app.route('/api/users', methods=['DELETE'])
def delete_record():
    con = get_db()
    cur = con.cursor()
    name = request.args.get('name')
    cur.execute("DELETE FROM users WHERE name=:name", {"name": name })
    con.commit()
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3001)
