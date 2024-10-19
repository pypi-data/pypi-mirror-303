class printer:
    def __init__(self):
        self.a = 1

    def socket_sql_injection(self):
        print('''
        #server.py
        import socket
        import sqlite3
        import threading
        
        
        # Server database connection function
        def get_db_connection():
            conn = sqlite3.connect('employee_data.db')
            conn.row_factory = sqlite3.Row
            return conn
        
        
        # Initialize the database (add this to create the DB)
        def init_db():
            conn = get_db_connection()
            conn.execute("""CREATE TABLE IF NOT EXISTS employee_data (
                employee_number INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                role TEXT NOT NULL,
                salary REAL NOT NULL,
                city TEXT NOT NULL
            )""")
        
            conn.execute("""CREATE TABLE IF NOT EXISTS employee_credentials (
                employee_number INTEGER,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                FOREIGN KEY (employee_number) REFERENCES employee_data(employee_number)
            )""")
        
            # Add initial data if necessary
            conn.execute(
                "INSERT INTO employee_data (employee_name, role, salary, city) VALUES ('John Doe', 'Manager', 70000, 'New York')")
            conn.execute(
                "INSERT INTO employee_credentials (employee_number, username, password) VALUES (1, 'admin', 'adminpass')")
        
            conn.commit()
            conn.close()
        
        
        # Handle client connections
        def handle_client(client_socket):
            try:
                # Receive username and password from the client
                data = client_socket.recv(1024).decode()
                username, password = data.split(',')
        
                # Query the database for user credentials
                conn = get_db_connection()
                query = f"SELECT * FROM employee_credentials WHERE username = '{username}' AND password = '{password}'"
                cur = conn.execute(query)
                user = cur.fetchone()
                conn.close()
        
                # Respond to client based on authentication result
                if user:
                    response = "Authentication successful"
                else:
                    response = "Authentication failed"
        
                client_socket.send(response.encode())
            except Exception as e:
                print(f"Error handling client: {e}")
                client_socket.send("Error during authentication".encode())
            finally:
                client_socket.close()
        
        
        def start_server():
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('localhost', 12345))
            server.listen(5)
            print("Server is listening on port 12345...")
        
            while True:
                client_socket, addr = server.accept()
                print(f"Accepted connection from {addr}")
                # Create a new thread for each client connection
                client_handler = threading.Thread(target=handle_client, args=(client_socket,))
                client_handler.start()
        
        
        if __name__ == "__main__":
            # Initialize the database before starting the server
            init_db()
            start_server()
        
        #client.py
        import socket
        def client_program():
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('localhost', 12345))
        
            # User inputs username and password
            username = input("Enter your username: ")
            password = input("Enter your password: ")
        
            # Send the username and password to the server
            client_socket.send(f"{username},{password}".encode())
        
            # Receive response from the server
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")
        
            client_socket.close()
        
        if __name__ == "__main__":
            client_program()
        ''')

    def ps_sql_injection(self):
        print('''
        #app.py
        from flask import Flask, render_template, request, redirect, url_for, session, flash
        import sqlite3
        
        app = Flask(__name__)
        app.secret_key = 'your_secret_key'
        
        # Database connection function
        def get_db_connection():
            conn = sqlite3.connect('employee_data.db')
            conn.row_factory = sqlite3.Row
            return conn
        
        # Initialize the database (add this to create the DB)
        def init_db():
            conn = get_db_connection()
            conn.execute("""CREATE TABLE IF NOT EXISTS employee_data (
                employee_number INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT NOT NULL,
                role TEXT NOT NULL,
                salary REAL NOT NULL,
                city TEXT NOT NULL
            )""")
        
            conn.execute("""CREATE TABLE IF NOT EXISTS employee_credentials (
                employee_number INTEGER,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                FOREIGN KEY (employee_number) REFERENCES employee_data(employee_number)
            )""")
        
            # Add initial data if necessary
            conn.execute("INSERT INTO employee_data (employee_name, role, salary, city) VALUES ('John Doe', 'Manager', 70000, 'New York')")
            conn.execute("INSERT INTO employee_credentials (employee_number, username, password) VALUES (1, 'admin', 'adminpass')")
        
            conn.commit()
            conn.close()
        
        # Home route
        @app.route('/')
        def home():
            return redirect(url_for('login'))
        
        # Login route
        @app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                
                # Vulnerable to SQL injection
                conn = get_db_connection()
                query = f"SELECT * FROM employee_credentials WHERE username = '{username}' AND password = '{password}'"
                cur = conn.execute(query)
                user = cur.fetchone()
                conn.close()
        
                if user:
                    session['logged_in'] = True
                    session['username'] = username
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid credentials. Try again.')
            
            return render_template('login.html')
        
        # Dashboard route - after successful login
        @app.route('/dashboard')
        def dashboard():
            if 'logged_in' in session:
                conn = get_db_connection()
                employees = conn.execute('SELECT * FROM employee_credentials').fetchall()
                conn.close()
                return render_template('dashboard.html', employees=employees)
            else:
                return redirect(url_for('login'))

        @app.route('/get_tables')
        def get_tables():
            if 'logged_in' in session:
                conn = get_db_connection()
                tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
                conn.close()
                return str(tables)
            else:
                return redirect(url_for('login'))
                
        @app.route('/update_salary', methods=['POST'])
        def update_salary():
            if 'logged_in' in session:
                employee_name = request.form['employee_name']
                new_salary = request.form['salary']
                
                # Vulnerable query
                conn = get_db_connection()
                query = f"UPDATE employee_data SET salary = '{new_salary}' WHERE employee_name = '{employee_name}'"
                conn.execute(query)
                conn.commit()
                conn.close()
                return "Salary updated!"
            else:
                return redirect(url_for('login'))

        # Logout route
        @app.route('/logout')
        def logout():
            session.clear()
            return redirect(url_for('login'))
        
        if __name__ == '__main__':
            # Initialize the database (only run this once)
            init_db()
            app.run(debug=True)
            
        #templates/login.html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Login</title>
        </head>
        <body>
            <h1>Login</h1>
            <form method="POST" action="{{ url_for('login') }}">
                <label for="username">Username:</label>
                <input type="text" name="username" required><br><br>
                
                <label for="password">Password:</label>
                <input type="password" name="password" required><br><br>
                
                <button type="submit">Login</button>
            </form>
            
            {% with messages = get_flashed_messages() %}
              {% if messages %}
                <ul>
                {% for message in messages %}
                  <li>{{ message }}</li>
                {% endfor %}
                </ul>
              {% endif %}
            {% endwith %}
        </body>
        </html>
        
        #templates/dashboard.html
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Dashboard</title>
        </head>
        <body>
            <h1>Welcome, {{ session['username'] }}</h1>
            <h2>Employee Data</h2>
            
            <table border="1">
                <tr>
                    <th>Employee Number</th>
                    <th>Name</th>
                    <th>Role</th>
                    <th>Salary</th>
                    <th>City</th>
                </tr>
                {% for employee in employees %}
                <tr>
                    <td>{{ employee['employee_number'] }}</td>
                    <td>{{ employee['employee_name'] }}</td>
                    <td>{{ employee['role'] }}</td>
                    <td>{{ employee['salary'] }}</td>
                    <td>{{ employee['city'] }}</td>
                </tr>
                {% endfor %}
            </table>
            
            <br>
            <a href="{{ url_for('logout') }}">Logout</a>
        </body>
        </html>

        #attack login: admin' --
        #safguarding
        conn = get_db_connection()
        query = "SELECT * FROM employee_credentials WHERE username = ? AND password = ?"
        cur = conn.execute(query, (username, password))
        user = cur.fetchone()
        conn.close()
        ''')

    def sql_injection(self):
        print('''
        from flask import Flask, request, render_template_string
        import sqlite3
        
        app = Flask(__name__)
        
        # Use a persistent database file
        DATABASE = 'users.db'
        
        
        def get_db_connection():
            conn = sqlite3.connect(DATABASE)
            conn.row_factory = sqlite3.Row
            return conn
        
        
        # Initialize the database with some data (only run once)
        def init_db():
            conn = get_db_connection()
            conn.execute("""CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL)""")
            conn.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
            conn.execute("INSERT INTO users (username, password) VALUES ('user', 'userpass')")
            conn.commit()
            conn.close()
        
        
        # Initialize the database on app startup
        init_db()
        
        """
        # Vulnerable login function
        def check_login(username, password):
            conn = get_db_connection()
            query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
            result = conn.execute(query).fetchone()
            conn.close()
            return result
        """
        def check_login(username, password):
            conn = get_db_connection()
            # Use parameterized query to prevent SQL injection
            query = "SELECT * FROM users WHERE username=? AND password=?"
            result = conn.execute(query, (username, password)).fetchone()
            conn.close()
            return result
        
        # Route for the home page (login page)
        @app.route('/', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
        
                # Check login
                user = check_login(username, password)
        
                if user:
                    return f"<div class='alert alert-success'>Welcome, {username}!</div>"
                else:
                    return "<div class='alert alert-danger'>Login failed. Invalid username or password.</div>"
        
            return render_template_string("""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <title>Login</title>
                    <style>
                        body {
                            background-color: #f8f9fa;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            margin: 0;
                        }
                        .login-container {
                            background-color: white;
                            padding: 30px;
                            border-radius: 8px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }
                        .login-container h2 {
                            margin-bottom: 20px;
                            font-weight: bold;
                            color: #343a40;
                        }
                    </style>
                </head>
                <body>
                    <div class="login-container">
                        <h2>Login</h2>
                        <form method="post">
                            <div class="mb-3">
                                <label for="username" class="form-label">Username</label>
                                <input type="text" class="form-control" id="username" name="username" required>
                            </div>
                            <div class="mb-3">
                                <label for="password" class="form-label">Password</label>
                                <input type="password" class="form-control" id="password" name="password" required>
                            </div>
                            <button type="submit" class="btn btn-primary w-100">Login</button>
                        </form>
                    </div>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
                </body>
                </html>
            """)
        
        
        if __name__ == '__main__':
            app.run(debug=True)
        ''')
