from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
@app.route("/index")
def home():
    restaurant = {"name": "Boba's Boba Tea"}
    return render_template("index.html", restaurant=restaurant)

@app.route('/sms', methods=['GET', 'POST'])
def sms():
    try:
        msg = request.values.get('Body').lower().strip()
        res = MessagingResponse()
        if msg == "matcha":
            res.message("noice")
        else:
            res.message("meh")
        return str(res)
    except:
        return render_template("index.html", restaurant={"name": "ERROR - SMS"})

@socketio.on('my event')                          # Decorator to catch an event called "my event":
def test_message(message):                        # test_message() is the event callback function.
    emit('my response', {'data': 'got it!'})      # Trigger a new event called "my response"
                                                  # that can be caught by another callback later in the program.

if __name__ == "__main__":
    socketio.run(app)