from flask import Flask, jsonify
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)


NEWS_SOURCES = {
    "vnexpress": "https://vnexpress.net/rss/tin-moi-nhat.rss",
    "tuoitre": "https://tuoitre.vn/rss/trang-chu.rss",
    "thanhnien": "https://thanhnien.vn/rss/home.rss"
}


def get_news(source, url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        root = ET.fromstring(response.content)

        news = []

        for item in root.findall(".//item")[:20]:
            title = item.findtext("title")
            link = item.findtext("link")
            description = item.findtext("description")
            pub_date = item.findtext("pubDate")

            news.append({
                "source": source,
                "title": title,
                "link": link,
                "description": description,
                "pub_date": pub_date
            })

        return news

    except Exception as e:
        return [{
            "source": source,
            "error": str(e)
        }]


@app.route("/")
def index():
    all_news = []

    for source, url in NEWS_SOURCES.items():
        news = get_news(source, url)
        all_news.extend(news)

    return jsonify(all_news)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
