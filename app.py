from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=10)

    data = response.json()

    return jsonify(data[:5])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
