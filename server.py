from flask import Flask, render_template, request
from backend import safecheckurl
from waitress import serve

app = Flask(__name__)

@app.route('/backend')




if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)