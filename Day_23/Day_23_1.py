
from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/signin', methods=['GET'])
def get_root():
    # get the file named index.html from templates directory
    return render_template('index.html')

@app.route('/signin', methods=['GET'])
def get_signin():
    return "signin"

@app.route('/signup', methods=['GET'])
def get_signup():
    return "signup"

@app.route('/home', methods=['GET'])
def get_home():
    return "home"

@app.route('/chart', methods=['GET'])
def get_chart():
    return "chart"

@app.route('/about_us', methods=['GET'])
def get_about_us():
    return "about_us"

@app.route('/contact_us', methods=['GET'])
def get_contact_us():
    return "contact_us"

@app.route('/help', methods=['GET'])
def get_help():
    return "help"

app.run(host='0.0.0.0', port=4000, debug=True)
