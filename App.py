from flask import Flask, Blueprint
from urls.urls import API

app = Flask(__name__)
app.register_blueprint(API, url_prefix='/')
if __name__ == "__main__":
    app.run(debug=True)
