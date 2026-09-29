iifrom flask import Flask, render_template_string
import requests

app = Flask(__name__)

URL = "https://www.24h.com.vn/upload/rss/bongda.rss"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

# Tin mẫu dùng khi không lấy được RSS thật (để test deploy vẫn luôn có nội dung)
SAMPLE = [
    ("Real Madrid thắng đậm 3-0", "https://www.24h.com.vn/bong-da-c48.html"),
    ("Man City đánh bại Arsenal", "https://www.24h.com.vn/bong-da-c48.html"),
    ("Việt Nam vào chung kết", "https://www.24h.com.vn/bong-da-c48.html"),
]

HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Tin Bóng Đá 24h</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <nav class="navbar navbar-dark bg-success mb-4">
    <div class="container"><span class="navbar-brand">⚽ Tin Bóng Đá 24h</span></div>
  </nav>
  <div class="container">
    <div class="row g-4">
      {% for title, link in news %}
      <div class="col-md-4">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">{{ title }}</h5>
            <a href="{{ link }}" target="_blank" class="btn btn-success btn-sm">Đọc bài</a>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</body>
</html>
"""


@app.route("/")
def index():
    news = []
    try:
        res = requests.get(URL, headers=HEADERS, timeout=5)
        for item in res.text.split("<item>")[1:13]:
            title = item.split("<title>")[1].split("</title>")[0]
            link = item.split("<link>")[1].split("</link>")[0]
            news.append((title, link))
    except Exception:
        pass

    if not news:
        news = SAMPLE

    return render_template_string(HTML, news=news)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
