from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/HOME')
def home():
    return render_template('home.html')


@app.route('/profile')
def pro():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
