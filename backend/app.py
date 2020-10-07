import flask
from flask import request, jsonify, Response

import defaultConfig

app = flask.Flask(__name__)

@app.route('/anagram', methods=['GET', 'POST'])
def api_all():
    if request.method == 'POST':
        word1 = request.form.get("word1")
        word2 = request.form.get("word2")
        
        return jsonify({'isAnagram': defaultConfig.anagramService.isAnagram(word1, word2)}), {'Access-Control-Allow-Origin': '*'}
    
    elif request.method == 'GET':
        return jsonify(defaultConfig.anagramStore.getMostFrequent(10)), {'Access-Control-Allow-Origin': '*'}

if __name__ == '__main__':
    app.run()