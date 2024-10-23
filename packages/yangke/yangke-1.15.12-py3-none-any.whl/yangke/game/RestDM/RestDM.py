# 本模块只能使用32位python调用
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'


if __name__ == "__main__":
    pass
