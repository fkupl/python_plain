from flask import Flask, jsonify

app = Flask(__name__)

languages = [{'iso': 'de', 'name': 'German'}, {'iso': 'en', 'name': 'English'},
             {'iso': 'ru', 'name': 'Russian'}, {'iso': 'fr', 'name': 'French'},
             {'iso': 'it', 'name': 'Italian'}, {'iso': 'es', 'name': 'Spanish'},
             {'iso': 'pt', 'name': 'Portuguese'}]

@app.route('/', methods=['GET'])
def default():
    return jsonify({'message': 'It works!'})

@app.route('/languages', methods=['GET'])
def getList():
    return jsonify({'languages': languages})

@app.route('/languages/<string:isoParam>', methods=['GET'])
def getOne(isoParam):
    langs = [language for language in languages if language['iso'] == isoParam]
    return jsonify({'language': langs[0]})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
