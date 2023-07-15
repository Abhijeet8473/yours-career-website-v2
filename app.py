from flask import Flask

# app is the object of python

app = Flask(__name__)

@app.route("/")
def hello_world():       #define a function
    return "hello career world"

if __name__ == "__main__":
    app.run()

    