import ptvsd
from flask import Flask
from config import DEBUG

if DEBUG:
    print('debugger is active')
    address = ('0.0.0.0', 3000)
    ptvsd.enable_attach(address=address)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
