import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    """Reads items from a JSON file and renders them in a list."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Extract the list of items from the dictionary
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # If file is missing or corrupted, pass an empty list
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
