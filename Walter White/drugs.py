from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/picture1")
def pic1():
    return render_template("picture1.html")

@app.route("/picture2")
def pic2():
    return render_template("picture2.html")

@app.route("/picture3")
def pic3():
    return render_template("picture3.html")

@app.route("/picture4")
def pic4():
    return render_template("picture4.html")

@app.route("/picture5")
def pic5():
    return render_template("picture5.html")
    
if __name__ == "__main__":
    app.run(debug=True)

