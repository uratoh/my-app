from flask import Flask, render_template_string

app = Flask(__name__)

NEWS = [
    ("Real Madrid thắng đậm 3-0", "https://www.24h.com.vn"),
    ("Man City đánh bại Arsenal", "https://www.24h.com.vn"),
    ("Việt Nam vào chung kết", "https://www.24h.com.vn"),
    ("Liverpool giữ ngôi đầu bảng", "https://www.24h.com.vn"),
    ("Barcelona ký hợp đồng mới", "https://www.24h.com.vn"),
    ("Bayern hòa kịch tính", "https://www.24h.com.vn"),
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
    return render_template_string(HTML, news=NEWS)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
