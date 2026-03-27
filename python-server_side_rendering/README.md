# Python - Server-Side Rendering (SSR)

## Project Overview
This project focuses on **Server-Side Rendering (SSR)** using Python and the **Flask** web framework. The goal is to understand how web pages are generated on the server using the **Jinja2** templating engine and how to integrate dynamic data from various sources including **JSON**, **CSV**, and **SQLite** databases.

## Learning Objectives
* Understand the difference between Client-Side and Server-Side rendering.
* Implement SSR using Flask and Jinja2.
* Read and display dynamic content from different file formats (JSON, CSV).
* Connect a Flask application to a SQLite database.
* Handle query parameters and implement error handling for web routes.

## Project Structure
```text
python-server_side_rendering/
├── task_00_intro.py      # Basic string templating
├── task_01_jinja.py      # Flask setup & shared templates
├── task_02_logic.py      # Loops and conditionals (JSON)
├── task_03_files.py      # JSON and CSV integration
├── task_04_db.py         # SQLite database integration
├── products.json         # Data source 1
├── products.csv          # Data source 2
├── products.db           # Data source 3 (SQLite)
├── templates/            # Jinja2 HTML templates
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── header.html
│   ├── footer.html
│   ├── items.html
│   └── product_display.html
└── README.md
```

## Task

0. Basic Templating

A script that generates personalized invitation files from a `template.txt` file and a list of attendee dictionaries. It handles missing data by replacing it with "N/A".

1. Flask and Jinja Basics

Creation of a basic Flask app with multiple routes (`/`, `/about`, `/contact`). It uses `{% include %}` to reuse a common header and footer across all pages.

2. Loops and Conditionals

Integration of an `/items` route that reads a list from `items.json`. It uses Jinja's `{% for %}` loops to display items and `{% if %}` to show a "No items found" message if the list is empty.

3. JSON and CSV Integration

A dynamic route `/products` that accepts a `source` parameter (`json` or `csv`). It parses the selected file and displays the data in an HTML table. It supports filtering by a specific `id`.

4. SQLite Database Support

Extended the `/products` route to support `source=sql`. Data is fetched from a SQLite database (`products.db`). The system handles errors like "Wrong source" or "Product not found" gracefully.

## How to Run

1. Install dependencies:
```bash
pip3 install Flask
```

2. Run a specific task (e.g., task_04_db.py):
```bash
python3 task_04_db.py
```
3. Access the results in your browser:

- http://localhost:5000/products?source=json
- http://localhost:5000/products?source=csv
- http://localhost:5000/products?source=sql