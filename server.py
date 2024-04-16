from flask import request,Flask
import flask
from request_handler import getResponse

app = Flask('D:\Backend')

@app.get
@app.route('/')
def controller():
    prompt = request.args.get('text')
    response = flask.Response(getResponse(prompt))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


    

def init_server():
    app.run(host='127.0.0.1',port=3000)