from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/test2')
def index2():

    return render_template("index2.html")

@app.route('/test3')
def index3():

    return render_template("index3.html")

@app.route('/test4')
def index4():

    return render_template("index4.html")

@app.route('/test5')
def index5():

    return render_template("index5.html")

if __name__ =="__main__":
    app.run(debug=True)

