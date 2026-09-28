8from flask import Flask
import requests

app = Flask(__name__)

URL = "https://www.24h.com.vn/upload/rss/bongda.rss"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

# Tin mẫu, dùng khi không lấy được tin thật
SAMPLE = [
    ("Tin mẫu 1: Web đã deploy thành công", "https://www.24h.com.vn"),
    ("Tin mẫu 2: Không lấy được RSS từ 24h", "https://www.24h.com.vn"),
    ("Tin mẫu 3: Kiểm tra mạng hoặc User-Agent", "https://www.24h.com.vn"),
]


@app.route("/")
def index():
    news = []
    try:
        res = requests.get(URL, headers=HEADERS, timeout=5)
        for item in res.text.split("<item>")[1:11]:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]
            news.append((title, link))
    except Exception:
        pass

    if not news:
        news = SAMPLE

    html = "<h1>Tin Bóng Đá 24h</h1>"
    for title, link in news:
        html += f'<p><a href="{link}" target="_blank">{title}</a></p>'
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
