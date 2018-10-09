from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/ex", methods=['GET','POST'])
def example():
    return render_template('temindex.html')

if __name__ == "__main__":
    app.run(port = 8080)