from flask import Flask, jsonify, request
from inshorts import getNews

app = Flask(__name__)


@app.route('/shorts/<category>', methods=['GET', 'POST'])
def news(category):
    return jsonify(getNews(category))


if __name__ == '__main__':
    app.run(debug=True)
