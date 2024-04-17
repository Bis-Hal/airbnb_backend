from flask import request,Flask
import flask
from request_handler import getResponse

app = Flask('D:\\backend')

@app.get
@app.route('/')
def controller():
    room = request.args.get('room', default=None, type=str)
    property = request.args.get('property', default=None, type=str)
    country = request.args.get('country', default=None, type=str)
    amenities = request.args.get('amenities', default=0, type=int)
    print("Hit 01")
    print(room)
    print(property)
    print(country)
    print(amenities)
    response = flask.Response(getResponse(room))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


    

def init_server():
    app.run(host='127.0.0.1',port=3000)