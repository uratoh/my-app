from flask import Flask
import requests

app = Flask(__name__)


@app.route("/")
def index():
    res = requests.get("https://www.24h.com.vn/upload/rss/bongda.rss", timeout=5)
    items = res.text.split("<item>")[1:31]

    html = "<h1>Tin Bóng Đá 24h</h1>"
    for item in items:
        title = item.split("<title>")[1].split("</title>")[0]
        link = item.split("<link>")[1].split("</link>")[0]
        html += f'<p><a href="{link}" target="_blank">{title}</a></p>'

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
