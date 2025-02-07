from flask import Flask, render_template

app = Flask("Website")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/v1/<station>/<date>")
def about(station, date):
    # df = pandas.read_csv("data.csv")
    # temperature = df.station(date)
    temperature = 23
    res = {"station": station, "date": date, "temperature": temperature}
    return res


if __name__ == "__main__":
    app.run(debug=True)
