from api.server import get_api_server
from flask import Flask

app: Flask = get_api_server()

if __name__ == '__main__':
    app.run(debug=True)