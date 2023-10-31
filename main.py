from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("Квартира Куинджи.htm")

@app.route("/masterskaya")
def f_masterskaya():
    return render_template("Мастерская.htm")

@app.route("/gostinaya")
def f_gostinaya():
    return render_template("Гостиная.htm")

@app.route("/kabinet")
def f_kabinet():
    return render_template("Кабинет.htm")

if __name__ == "__main__":
    app.run(debug=True)