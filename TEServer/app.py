from flask import Flask,jsonify,request

app = Flask(__name__)

angle = 0

@app.route('/')
def index():
    return "Go to http://[hostname]/motor/api/  to get it."

@app.route('/motor/api/', methods=['GET'])
def getIt():
    return jsonify({'angle': angle})

@app.route('/motor/api/<int:vrangle>', methods=['POST'])
def updateIt(vrangle):
    angle = vrangle
    return jsonify({'angle': angle})


if __name__ == '__main__':
    app.run(debug=True)
