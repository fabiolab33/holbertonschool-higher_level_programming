import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def get_sql_data():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Row_factory permite acceder a las columnas por nombre como un diccionario
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Validar fuente
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Obtener datos según la fuente
    if source == 'json':
        data = get_json_data()
    elif source == 'csv':
        data = get_csv_data()
    elif source == 'sql':
        data = get_sql_data()

    # 3. Filtrar por ID si se proporciona
    if product_id:
        data = [p for p in data if p.get('id') == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
