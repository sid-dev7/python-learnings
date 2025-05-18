#import package
from flask import Flask, jsonify
import mysql.connector

#create a web server 

app = Flask(__name__)

#  let the server respond for a request sent with path = /
@app.route('/', methods = ["GET"])
def root():
    return'<h1 style ="color: red">welcome to my webserver sid</h1>'
@app.route('/product', method=['GET'])


def get_products():
    connection = mysql.connector.connect(host ='localhost', user='root',password ='admin123',database='personsdb')
    query = 'select id, title, description, price of product'
    cursor = connection.cursor()
    result = cursor.fetchall()
    products = []
    for (id,title, description, price) in result:
        product = {
            "id" : id,
            "title" : title,
            "description" : description,
            "price": price            
        }
        products.append(product)
    connection.close()
    return jsonify(product)


#start the server on port 4000

app.run(host='0.0.0.0',port=4000)