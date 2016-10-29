from flask import Flask,request

app = Flask(__name__)

angle = "00000000"

@app.route('/')
def index():
    return "Go to http://[hostname]/motor/api/  to get it."

@app.route('/motor/api/', methods=['GET'])
def getIt(angle):
        return angle

@app.route('/motor/api/<string:vrangle>', methods=['POST'])
def updateIt(vrangle,angle):
    angle = vrangle
    return angle

if __name__ == '__main__':
    app.run(debug=True)
