# Basics of HTTP and HTTPS

## Differences Between HTTP and HTTPS

HTTP (Hypertext Transfer Protocol) is the standard protocol used for communication between a client (such as a web browser) and a web server. It follows a client-server model where the client sends a request and the server returns a response.

HTTP is stateless, meaning each request is independent and the server does not store information between requests.

However, HTTP does not encrypt transmitted data. This means that any intercepted communication can be read or modified.

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to secure the communication between client and server.

Main differences:

- HTTP sends data in plain text.
- HTTPS encrypts the data.
- HTTP uses port 80.
- HTTPS uses port 443.
- HTTPS ensures confidentiality, integrity, and authentication.

---

## Structure of an HTTP Request

An HTTP request is composed of:

1. Request line (Method, Path, HTTP Version)
2. Headers
3. Optional Body

Example:

GET /users HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: application/json


Components:

- Method: GET
- Path: /users
- Version: HTTP/1.1
- Headers: Provide additional information
- Body: Used mainly in POST or PUT requests

---

## Structure of an HTTP Response

An HTTP response is composed of:

1. Status line (HTTP Version, Status Code, Status Message)
2. Headers
3. Response Body

Example:

HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 45
{"message": "Success"}


Components:

- HTTP Version: HTTP/1.1
- Status Code: 200
- Status Message: OK
- Headers: Metadata about the response
- Body: Data returned to the client

---

## Common HTTP Methods

### GET
Description: Retrieves data from the server.
Use case: Fetching a web page or retrieving data from an API.

### POST
Description: Sends data to the server to create a new resource.
Use case: Submitting a form or creating a new user.

### PUT
Description: Replaces an existing resource with new data.
Use case: Updating a full user profile.

### DELETE
Description: Removes a resource from the server.
Use case: Deleting a user account.

---

## Common HTTP Status Codes

### 200 OK
Description: The request was successful.
Scenario: Successfully retrieving data from an API.

### 201 Created
Description: A new resource was successfully created.
Scenario: Successfully creating a new user.

### 400 Bad Request
Description: The request is invalid or malformed.
Scenario: Sending incorrect JSON data to an API.

### 404 Not Found
Description: The requested resource was not found.
Scenario: Accessing an endpoint that does not exist.

### 500 Internal Server Error
Description: The server encountered an unexpected error.
Scenario: A backend crash or database failure.