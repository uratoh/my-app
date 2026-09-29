from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

URL = "https://www.24h.com.vn/"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <title>Tin tức 24h</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; }
        h1 { color: #d32f2f; }
        ul { list-style: none; padding: 0; }
        li { margin-bottom: 12px; border-bottom: 1px solid #eee; padding-bottom: 12px; }
        a { text-decoration: none; color: #1a0dab; font-size: 16px; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Tin mới nhất từ 24h.com.vn</h1>
    <ul>
    {% for item in articles %}
        <li><a href="{{ item.link }}" target="_blank">{{ item.title }}</a></li>
    {% endfor %}
    </ul>
</body>
</html>
"""


def get_articles():
    """Lấy tiêu đề + link bài báo từ trang chủ 24h.com.vn"""
    articles = []
    try:
        resp = requests.get(URL, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        seen = set()
        for a in soup.find_all("a", href=True):
            title = a.get_text(strip=True)
            href = a["href"]

            # Bỏ qua link không có tiêu đề hoặc tiêu đề quá ngắn (thường là menu, icon...)
            if not title or len(title) < 20:
                continue

            # Chuẩn hóa link tương đối thành link đầy đủ
            if not href.startswith("http"):
                href = "https://www.24h.com.vn" + href

            if href in seen:
                continue
            seen.add(href)

            articles.append({"title": title, "link": href})
            if len(articles) >= 15:
                break
    except Exception as e:
        articles.append({"title": f"Lỗi khi tải tin: {e}", "link": "#"})

    return articles


@app.route("/")
def home():
    articles = get_articles()
    return render_template_string(HTML_TEMPLATE, articles=articles)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
