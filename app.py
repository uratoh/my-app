from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://dantri.com.vn/rss.htm"

    response = requests.get(url, timeout=10)

    root = ET.fromstring(response.content)

    news = []

    for item in root.findall(".//item")[:5]:
        title = item.findtext("title")
        link = item.findtext("link")

        news.append({
            "title": title,
            "link": link
        })

    return jsonify(news)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
