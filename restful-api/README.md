# RESTful API Development with Python

## Project Overview

This project demonstrates the progressive development of RESTful APIs using Python.  
It covers HTTP communication, data consumption from external APIs, building servers using both the standard library and Flask, and implementing API security mechanisms such as Basic Authentication and JWT-based authentication.

The goal of this project is to understand how APIs work from low-level HTTP handling to secure production-like authentication systems.

---

## Project Structure

restful-api/
│
├── task_00_http.md
├── task_01_curl.md
├── task_02_requests.py
├── task_03_http_server.py
├── task_04_flask.py
├── task_05_basic_security.py
└── README.md


---

# Tasks Description

---

## Task 0 – HTTP Fundamentals

This task explains the theoretical foundation of HTTP:

- What HTTP is
- Structure of HTTP requests and responses
- HTTP methods (GET, POST, PUT, DELETE)
- Status codes (200, 404, 401, etc.)
- Headers and content types
- JSON format in APIs

This provides the conceptual base necessary to understand REST API communication.

---

## Task 1 – Interacting with APIs using cURL

In this task, we use `curl` from the command line to interact with APIs directly.

### Features:
- Sending GET requests
- Sending POST requests
- Adding headers manually
- Sending JSON payloads
- Understanding HTTP status codes in real responses
- Using Basic Authentication with `curl`

### Concepts Covered:
- Command-line HTTP requests
- Inspecting response headers with `-i`
- Sending authentication credentials
- Debugging API responses

This task helps understand how HTTP communication works before automating it with Python.

---

## Task 2 – Consuming an External API with `requests`

In this task, we interact with the public API **JSONPlaceholder** using Python’s `requests` library.

### Features:
- Send HTTP GET requests
- Check response status codes
- Parse JSON responses
- Extract and print post titles
- Convert structured JSON data into CSV format
- Save data into `posts.csv`

### Concepts Covered:
- `requests.get()`
- `.json()` parsing
- List comprehensions
- `csv.DictWriter`

---

## Task 3 – Building a Simple HTTP Server (Standard Library)

This task uses Python’s built-in `http.server` module to create a basic API server without third-party frameworks.

### Implemented Endpoints:
- `/` → Returns plain text
- `/data` → Returns JSON data
- `/status` → Returns API status
- Undefined routes → Return 404

### Concepts Covered:
- `BaseHTTPRequestHandler`
- Handling GET requests
- Sending headers
- Setting `Content-Type`
- Returning JSON responses
- Basic routing logic

This task helps understand how web servers work internally.

---

## Task 4 – Building an API with Flask

This task introduces Flask, a lightweight web framework.

### Implemented Features:
- Route handling with `@app.route`
- JSON responses using `jsonify`
- In-memory data storage
- Dynamic routes (`/users/<username>`)
- Handling POST requests
- Input validation
- Proper HTTP status codes (200, 201, 400, 404, 409)

### Implemented Endpoints:
- `/` → Welcome message
- `/data` → List of usernames
- `/status` → API status check
- `/users/<username>` → Retrieve user
- `/add_user` → Add new user via POST

This task introduces real-world API structure and request handling.

---

## Task 5 – API Security and Authentication

This task focuses on securing APIs using authentication and authorization mechanisms.

It implements:

### 1 Basic Authentication
- Uses `Flask-HTTPAuth`
- Password hashing with `werkzeug.security`
- Protected endpoint:
  - `/basic-protected`

### 2 JWT Authentication
- Uses `Flask-JWT-Extended`
- Token generation via `/login`
- Protected endpoint:
  - `/jwt-protected`

### 3 Role-Based Access Control
- Users have roles (`user`, `admin`)
- Admin-only endpoint:
  - `/admin-only`
- Returns 403 if user lacks privileges

### Security Features:
- Hashed passwords
- JWT tokens
- Custom JWT error handlers
- Proper HTTP status codes (401 for authentication errors)

This task simulates real production-level API security practices.

---

# Technologies Used

- Python 3
- Flask
- Flask-HTTPAuth
- Flask-JWT-Extended
- requests
- http.server
- JSON
- CSV module
- cURL

---

# Authentication vs Authorization

- **Authentication** → Verifies who the user is.
- **Authorization** → Determines what the user is allowed to access.

Both mechanisms are implemented in this project.

---

# Learning Outcomes

By completing this project, the following skills were developed:

- Understanding HTTP protocol fundamentals
- Interacting with APIs using command-line tools
- Consuming external APIs programmatically
- Building APIs without frameworks
- Developing REST APIs with Flask
- Implementing secure authentication systems
- Handling errors properly with correct HTTP status codes
- Structuring backend projects professionally

---

# How to Run

## Install dependencies:

```bash
pip install Flask Flask-HTTPAuth Flask-JWT-Extended requests
```

## Run Flask server:

```bash
python3 task_04_flask.py
```

This project demonstrates the evolution of API development:

1. Understanding HTTP
2. Testing APIs with cURL
3. Consuming APIs with Python
4. Building servers from scratch
5. Using frameworks
6. Securing APIs

It provides a strong foundation for backend development and REST API design.