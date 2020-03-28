from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    msg = request.values.get('Body').lower().strip()
    res = MessagingResponse()
    if msg == "matcha":
        res.message("noice")
    else:
        res.message("meh")
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)