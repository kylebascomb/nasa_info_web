import requests
from datetime import date, timedelta
import config


def get_current_week_list():
    day_list = []
    curr_day = date.today()
    for i in range(0,7):
        formatted_day = curr_day.strftime('%Y-%m-%d')
        day_list.append(formatted_day)
        curr_day = curr_day - timedelta(days=1)
    return day_list


def get_nasa_photos(api_key=config.nasa_api_key, week_list=get_current_week_list(), hd=False, url=config.photo_url):
    nasa_photos = []
    for day in week_list:
        payload = {'api_key': api_key,'hd': hd,'date': day}
        r = requests.get(url = url, params = payload)
        pic_dict = {}
        pic_dict["copyright"] = r.json().get('copyright')
        pic_dict["date"] = r.json().get("date")
        pic_dict["explanation"] = r.json().get("explanation")
        pic_dict["url"] = r.json().get("url")
        pic_dict["title"] = r.json().get("title")
        nasa_photos.append(pic_dict)
    return nasa_photos

