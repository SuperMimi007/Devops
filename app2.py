from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Good day!</p>"

if __name__ == "__main__":

    #changez de port ! 
    app.run(host="0.0.0.0",port=5007)
