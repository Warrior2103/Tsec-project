import pickle
import base64

from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/")
def my_form():
       return render_template('index.html')

@app.route("/", methods=["POST"])

def hackme():

    data = base64.urlsafe_b64decode(request.form['pickled'])

    deserialized = pickle.loads(data)

    return '', 204

if __name__=="__main__":
        app.run(host="localhost", port=5002, debug=True)
