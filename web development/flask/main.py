# simple applcaition with flask
import json
from flask import Flask , render_template, request
app = Flask('main')

@app.route('/')
def hello():
    data = '''
    <h1>Hello!</h1>
    <h2>Hello!</h2>
    <h3>Hello!</h3>
    <p>This is a simple application with Flask.</p>
    

'''
    return data #render_template('jose.html')

@app.route('/jose')
def bye():
    return render_template('jose.html')

@app.route('/dog')
def hi():
    return render_template('dog.html')

@app.route('/profile')
def why():
    return render_template('anything.html')

@app.route('/save_data')
def save():
    return render_template('save.html')

# i have to make a route for savifn the data
@app.route('/saving' , methods=['POST'])
def save_data():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'age': request.form['age'],
            'password': request.form['password']
        }
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        return render_template('save.html', data=data)
    return 'Method not allowed', 405

# continue next monday

app.run()