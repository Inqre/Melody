from flask import Flask
from index import index

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024 * 10240 * 10240 * 10240 * 10240
app.debug = False
app.register_blueprint(index)

if __name__ == "__main__":
    app.run(port=5738, host="0.0.0.0")
