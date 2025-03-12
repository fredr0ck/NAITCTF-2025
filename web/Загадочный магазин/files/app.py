import sqlite3
from flask import Flask, request, jsonify, render_template
import os
import re
import random

app = Flask(__name__)

HOSTNAME = os.getenv('HOSTNAME', '127.0.0.1:5002')
PORT = str(os.getenv('PORT', '5002'))

db_file = 'task2/products.db' 
product_count = 7

def filter_query(query):
    return re.sub(r"[;#]", "", query)  

def request_to_db(query):
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    products = conn.cursor().execute(query).fetchall()
    prod_dict = [dict(product) for product in products]
    return prod_dict
    conn.close()

@app.route('/')
def index():
    product_ids = []
    product_names = []
    product_descriptions = []
    product_prices = []
    product_images = []

    query = f"SELECT * FROM products WHERE id < {product_count+1}"
    prod_dict = request_to_db(query)
    random_dict = random.sample(range(0, product_count), product_count)
    for i in range(len(random_dict)):
        product_ids.insert(random_dict[i], (prod_dict[i])['id'])
        product_names.insert(random_dict[i], (prod_dict[i])['product_name'])
        product_descriptions.insert(random_dict[i], (prod_dict[i])['description'])
        product_prices.insert(random_dict[i], (prod_dict[i])['price'])
        product_images.insert(random_dict[i], (prod_dict[i])['image'])

    return render_template('index.html', ids=product_ids, names=product_names, descriptions=product_descriptions, prices=product_prices, image=product_images)

@app.route('/product', methods=['GET'])
def details():
    product_names = []
    product_prices = []
    product_status = []

    keyword = request.args.get('id')
    keyword = filter_query(keyword)
    if keyword:
        query = f"SELECT * FROM products WHERE id = {keyword}"
        prod_dict = request_to_db(query)
        for product in prod_dict:
            product_names.append(product['product_name'])
            product_prices.append(product['price'])
            product_status.append(product['status'])
        return render_template('checkstock.html', names=product_names, prices=product_prices, status=product_status, zip=zip)






    return jsonify({'message': 'No keyword provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(PORT))
