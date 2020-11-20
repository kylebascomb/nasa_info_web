import requests
import config
from datetime import date


def get_current_day():
    curr_day = date.today()
    formatted_day = curr_day.strftime('%Y-%m-%d')
    return formatted_day


def get_asteroids(api_key=config.nasa_api_key, url=config.asteroid_url, start_date=get_current_day()):
    payload = {'api_key': api_key,'start_date': start_date}
    r = requests.get(url=url, params=payload)
    print(r.json())
    print(r.response)



get_asteroids()