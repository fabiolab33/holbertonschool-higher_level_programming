# Consuming Data from an API Using curl

## Installing and Verifying curl

To check if curl is installed:

```bash
curl --version
```

If installed, it will display the version number and supported protocols.

## Making a Basic GET Request

Making a Basic GET Request

```bash
curl http://example.com
```

This sends a GET request to the server and prints the response body.

## Fetching Data from a Public API

Using JSONPlaceholder test API:

```bash
curl https://jsonplaceholder.typicode.com/posts
```

This sends a GET request and returns a JSON array of posts.

Each post contains:

- userId
- id
- title
- body

## Fetching Only Headers

To retrieve only the HTTP headers:

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

The -I flag tells curl to fetch headers only.

This allows inspection of:

- Status code (e.g., 200 OK)
- Content-Type
- Cache-Control
- Server information

## Making a POST Request

To send data using POST:

```bash
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
```
Explanation:

- -X POST specifies the HTTP method.
- -d sends data in the request body.

The API responds with a simulated created resource:

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

Note: JSONPlaceholder does not actually store the new data.

## Useful curl Options

- -I → Fetch headers only
- -X → Specify HTTP method
- -d → Send data in request body
