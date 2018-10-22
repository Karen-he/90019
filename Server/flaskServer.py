from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Change</h1>"

@app.route("/summary")
def about():
    return "<h1>summary</h1>"

@app.route("/timeline")
def about():
    return "<h1>timeline</h1>"

@app.route("/info")
def about():
    return "<h1>info</h1>"

#coonect to views

#hashtag

#hashtag with sentiments

#hashtag with time

#hashtag with location

# run py file in debug mode
if __name__ == '__main__':
    app.run(debug=True)
