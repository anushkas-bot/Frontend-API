"""from flask import Flask, jsonify, request #import objects from the Flask model
from flask_cors import CORS
app = Flask(__name__) #define app using Flask
CORS(app)
languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]
@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})
@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'languages' : languages})
@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})
@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages})
if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode"""

from flask import Flask, jsonify, request #import objects from the Flask model
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import send_file
import base64

app = Flask(__name__) #define app using Flask
CORS(app)

languages = [{'title' : 'Blog Overview'}, {'subtitle' : 'Dashboard'}, {'file' : 'file'}]

with open("blog1.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify(languages)

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'title' : request.json['title'], 'subtitle' : request.json['subtitle'] }
	languages.append(language)
	return jsonify(languages)

@app.route('/lang2', methods=['GET', 'POST'])
def addTwo():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        return 'file uploaded'

@app.route('/lang3', methods=['GET', 'POST'])
def addThree():
        return send_file('./blog1.jpg')

if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode

from flask import Flask, jsonify, request #import objects from the Flask model
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import send_file

app = Flask(__name__) #define app using Flask
CORS(app)

languages = [{'title' : 'Blog Overview'}, {'subtitle' : 'Dashboard'}, {'file' : 'file'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify(languages)

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'title' : request.json['title'], 'subtitle' : request.json['subtitle'] }
	languages.append(language)
	return jsonify(languages)

@app.route('/lang2', methods=['GET', 'POST'])
def addTwo():
    if request.method == 'POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        print(file.filename)
        print("'./" + file.filename + "'")
        return 'uploaded'
    if request.method == 'GET':
        return send_file("'./" + file.filename + "'")

@app.route('/lang3', methods=['GET', 'POST'])
def addThree():
        return send_file('./blog1.jpg')

@app.route('/lang4', methods=['GET', 'POST'])
def addFour():
        return encoded_string

if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode
