from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index2():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    with open('users.txt', 'a') as file:
        file.write(f"Username: {username}, Password: {password}, Email: {email}\n")

    return "Sign up successful!"




# Function to read users from the text file
def read_users():
    users = {}
    with open('users.txt', 'r') as file:
        for line in file:
            if line.strip():  # Avoid blank lines
                parts = line.strip().split(', ')
                username = parts[0].split(': ')[1]
                password = parts[1].split(': ')[1]
                users[username] = password
    return users

@app.route('/si')
def index():
    return render_template('index2.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    users = read_users()
    print(users,username,password)
    if username in users and users[username] in password:
        return f"Welcome, {username}! Sign in successful."
    else:
        return "Incorrect username or password. Please try again."


if __name__ == '__main__':
    app.run(debug=True)
