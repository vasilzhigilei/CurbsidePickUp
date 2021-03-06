from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
@app.route("/index")
def home():
    restaurant = {"name": "Boba's Boba Tea", "phone" : "(434) 204-3099"}
    return render_template("index.html", restaurant=restaurant)

@app.route('/sms', methods=['GET', 'POST'])
def sms_receive():
    try:
        msg = request.values.get('Body').strip()
        res = MessagingResponse()
        sms = {'number':request.values.get('From'), 'msg': msg}
        socketio.emit('generateSMS', sms, namespace='/test')
        res.message("Thank you! Please stay seated in your vehicle. We will hand deliver your order when it's ready.")
        return str(res)
    except:
        return render_template("index.html", restaurant={"name": "ERROR - SMS"})

@socketio.on('my event', namespace='/test')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    emit('toclient', json)

if __name__ == "__main__":
    socketio.run(app)