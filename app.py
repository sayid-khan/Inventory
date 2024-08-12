#pip install flask sqlalchemy pymysql

from flask import Flask, render_template, jsonify, redirect, request
from db import load_products_from_db, add_product_to_db, delete_product_from_db, update_product_in_db


app = Flask(__name__)


@app.route('/')
def index():
    products_list = load_products_from_db()
    return render_template('index.html', products=products_list)


@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    quantity = request.form['quantity']
    add_product_to_db(name, quantity)
    return redirect('/')


@app.route('/delete/<int:product_id>')
def delete_product(product_id):
    delete_product_from_db(product_id)
    return redirect('/')


@app.route('/edit/<int:product_id>', methods=['POST'])
def edit_product(product_id):
    name = request.form['name']
    quantity = request.form['quantity']
    update_product_in_db(product_id, name, quantity)
    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)