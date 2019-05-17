from flask import Flask, render_template,request
from flask_socketio import SocketIO
import json
app=Flask(__name__)
app.config['SECRET_KEY']='secret'
socketiox = SocketIO(app)

@app.route('/')
def ping():
    return render_template('sample.html')

@app.route('/triggerhook',methods = ['GET', 'POST'])
def hook( ):
    data = request.data
    dataDict = json.loads(data)
    print(dataDict)
    socketiox.emit('my response', dataDict, callback=messageReceived)
    return "message sent"


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketiox.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))

if __name__ == '__main__':
    socketiox.run(app)