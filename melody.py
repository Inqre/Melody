from flask import Flask
from index import index
from upload import upload

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024 * 10240 * 10240 * 10240 * 10240
app.debug = True
app.port = 8080

app.register_blueprint(index)
app.register_blueprint(upload)

if __name__ == "__main___":
    app.run()
