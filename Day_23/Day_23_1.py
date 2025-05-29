from flask import Flask, jsonify
#create a server
app = Flask(__name__)

@app.route('/signin', methods=['Get'])
def get_signin():
    return"signin"

@app.route('/signup', methods=['Get'])
def get_signup():
    return"signup"

@app.route('/home', methods=['Get'])
def geth_home():
    return"home"

@app.route('/chart', methods=['Get'])
def get_chart():
    return"chart"

@app.route('/about_us', methods=['Get'])
def get_about_us():
    return"about_us"

@app.route('/contact_us', methods=['Get'])
def get_contact_us():
    return"contact_us"

@app.route('/help', methods=['Get'])
def get_help():
    return"help"

#start server on port 4000
app.run(host='0.0.0.0',port=4000,debug=True)