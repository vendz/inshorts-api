from flask import Flask, jsonify, request
from inshorts import getNews

app = Flask(__name__)


@app.route('/')
def index():
    return "API is UP and running"


@app.route('/categories')
def categories():
    return "<a href = 'https://inshort.vandit.cf/shorts?category=all'>1. All News</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=india'>2. India</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=business'>3. Business</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=sports'>4. sports</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=world'>5. World</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=politics'>6. Politics</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=technology'>7. Technology</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=startup'>8. Startup</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=entertainment'>9. Entertainment</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=miscellaneous'>10. Miscellaneous</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=hatke'>11. Hatke</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=science'>12. Science</a><br>" \
           "<a href = 'https://inshort.vandit.cf/shorts?category=automobile'>13. Automobile</a><br>"


@app.route('/shorts')
def news():
    if request.method == 'GET':
        category = request.args.get('category')
        return jsonify(getNews(category))


if __name__ == '__main__':
    app.run(debug=True)
