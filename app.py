from flask import Flask

app = Flask(__name__)

NEWS = [
    ("Real Madrid thắng đậm 3-0", "https://www.24h.com.vn"),
    ("Man City đánh bại Arsenal", "https://www.24h.com.vn"),
    ("Việt Nam vào chung kết", "https://www.24h.com.vn"),
]


@app.route("/")
def index():
    html = "<h1>Tin Bóng Đá 24h</h1>"
    for title, link in NEWS:
        html += f'<p><a href="{link}">{title}</a></p>'
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
