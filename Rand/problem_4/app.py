from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    c.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('Tenuous', 'redwings')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('login.html')




@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[DEBUG SQL]", query)

    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        result = c.execute(query)
        user = result.fetchone()
        conn.close()

        if user:
            return jsonify(success=True, message=f"Welcome, {user[1]}!", sql=query)
        else:
            return jsonify(success=False, message="Login failed. Invalid credentials.", sql=query)

    except Exception as e:
        return jsonify(success=False, message=f"SQL Error: {e}", sql=query)
    
    
@app.route('/login2.html')
def login_success():
    return render_template('login2.html')
    
@app.route('/login2', methods=['POST'])
def login2():
    username = request.form['username']
    password = request.form['password']

    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute(query, (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            return jsonify(success=True, message=f"Welcome, {user[1]}!")
        else:
            return jsonify(success=False, message="Login failed. Invalid credentials.")

    except Exception as e:
        return jsonify(success=False, message=f"SQL Error: {e}")
    
@app.route('/login3.html')
def login3():
    return render_template('login3.html')

@app.route('/login3', methods=['POST'])
def login3_post():
    username = request.form['username']
    password = request.form['password']

    query = "SELECT * FROM users WHERE username = ? AND password = ?"

    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute(query, (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            return jsonify(success=True, message=f"Welcome, {user[1]}!")
        else:
            return jsonify(success=False, message="Login failed. Invalid credentials.")

    except Exception as e:
        return jsonify(success=False, message=f"SQL Error: {e}")


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
