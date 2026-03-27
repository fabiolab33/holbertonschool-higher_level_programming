import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert id to int and price to float for consistency
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # 1. Validate source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Read data based on source
    try:
        if source == 'json':
            data = read_json()
        else:
            data = read_csv()
    except Exception:
        return render_template('product_display.html', error="File not found")

    # 3. Filter by ID if provided
    if product_id:
        data = [p for p in data if p.get('id') == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
