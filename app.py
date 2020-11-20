from flask import Flask, render_template
import requests
import json
import mars_weather
import weekly_pictures as nasa_photos


app = Flask(__name__)


@app.route("/")
def index():
    weather_list = mars_weather.get_mars_weather()
    return render_template('index.html', weather_list = weather_list)

@app.route("/weekly_pictures")
def weekly_pictures():
    picture_list = nasa_photos.get_nasa_photos()
    return render_template("weekly_pictures.html", nasa_photos= picture_list)