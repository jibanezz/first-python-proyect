# we can not write a big code for website so there is a famous packkage called Flask

from flask import *
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('jose.html')




@app.route('/abc')
def helo():
    return render_template('anything.html')

app.run(debug=True)

