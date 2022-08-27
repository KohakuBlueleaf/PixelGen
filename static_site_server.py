from http.server import HTTPServer, SimpleHTTPRequestHandler


httpd = HTTPServer(
    ('127.0.0.1', 4999),
    lambda rq, cli, server: SimpleHTTPRequestHandler(
        rq, cli, server,
        directory = './frontend/dist'
    )
)


if __name__ == '__main__':
    httpd.serve_forever()