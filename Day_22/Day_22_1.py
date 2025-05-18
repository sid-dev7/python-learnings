#import package
from flask import Flask
#create a web server 

app = Flask(__name__)

#  let the server respond for a request sent with path = /
@app.route('/', methods = ["GET"])

def root():

    return "Congratulations Sid Welcome to your first webpage!"

#start the server on port 4000

app.run(host='0.0.0.0',port=4000)


