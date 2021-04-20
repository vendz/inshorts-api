from flask import Flask, jsonify, request
from inshorts import getNews

app = Flask(__name__)


@app.route('/')
def index():
    return "API is UP and running"


@app.route('/shorts/categories')
def categories():
    return "<a href = 'https://inshort.vandit.cf/shorts/all'>1. All News</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/india'>2. India</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/business'>3. Business</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/sports'>4. sports</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/world'>5. World</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/politics'>6. Politics</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/technology'>7. Technology</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/startup'>8. Startup</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/entertainment'>9. Entertainment</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/miscellaneous'>10. Miscellaneous</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/hatke'>11. Hatke</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/science'>12. Science</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts/automobile'>13. Automobile</a><br>"


@app.route('/shorts/<category>', methods=['GET', 'POST'])
def news(category):
    return jsonify(getNews(category))


if __name__ == '__main__':
    app.run(debug=True)
