from flask import Flask, render_template
import pandas as pd

app = Flask("Website")
stations = pd.read_csv("data/stations.txt", skiprows=18, sep=",", encoding="utf-8", header=None)
stations.columns = ["id", "name", "country", "lat", "lon", "height"]
stations.set_index("id", inplace=True)
stations["name"] = stations["name"].str.strip()


@app.route("/home")
def home():
    return render_template("home.html", data=stations.to_html())


@app.route("/v1/<station_nr>/<date>")
def get_weather_info_for_one_station_one_date(station_nr, date):
    station_nr = int(station_nr)
    if station_nr not in stations.index:
        print("Station not found")
        return "Station not found."

    station_info = stations.loc[station_nr]
    station_info = station_info.to_dict()

    station_data = get_station_temp_data(station_nr)
    temperature = station_data.loc[int(date)]
    station_info["Temperature"] = temperature[0]
    station_info
    return station_info


@app.route("/v1/<station_nr>")
def get_weather_info_for_one_station(station_nr):
    station_nr = int(station_nr)
    if station_nr not in stations.index:
        print("Station not found")
        return "Station not found."

    station_data = get_station_temp_data(station_nr)
    all_temperatures = station_data.to_dict()["temperature"]
    return all_temperatures


def get_station_temp_data(station_nr):
    filename = f"TG_STAID{'0' * (6 - len(str(station_nr)))}{station_nr}.txt"
    data = pd.read_csv(f"data/{filename}", skiprows=21, sep=",", encoding="utf-8", header=None)
    data.drop(data.columns[[0, 1, 4]], axis=1, inplace=True)
    data.columns = ["date", "temperature"]
    data["temperature"] = data["temperature"] / 10
    data.set_index(data.columns[0], inplace=True)
    return data


if __name__ == "__main__":
    app.run(debug=True)
