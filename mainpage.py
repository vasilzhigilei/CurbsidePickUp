from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    restaurant = {"name": "Boba's Boba Tea"}
    return render_template("index.html", restaurant=restaurant)

if __name__ == "__main__":
    app.run(debug=True)