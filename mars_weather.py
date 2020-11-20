import config
import requests
import json
from datetime import datetime



def get_mars_weather(api_key= config.nasa_api_key, feed_type='json',version='1.0', url='https://api.nasa.gov/insight_weather/' ):
    payload = {'api_key': api_key, 'feedtype' : feed_type, 'ver': version}

    r = requests.get(url= url, params= payload)
    return format_weather_data(r.json())

def format_weather_data(mars_weather):
    sol_ids = []
    sol_list = []

    for sol in mars_weather["sol_keys"]:
        sol_ids.append(sol)

    print(sol_ids)

    for sol_id in sol_ids:
        sol_dict = {}
        sol_dict["first_utc"] = mars_weather.get(sol_id).get("First_UTC")
        sol_dict["last_utc"] = mars_weather.get(sol_id).get("Last_UTC")
        sol_dict["first_formatted"] = get_formatted_time(sol_dict["first_utc"])
        sol_dict["last_formatted"] = get_formatted_time(sol_dict["last_utc"])
        sol_dict["sol_id"] = sol_id
        if mars_weather.get(sol_id).get("AT") != None:
            sol_dict["average_temp"] = round(mars_weather.get(sol_id).get("AT").get("av"),2)
            sol_dict["min_temp"] = round(mars_weather.get(sol_id).get("AT").get("mn"),2)
            sol_dict["max_temp"] = round(mars_weather.get(sol_id).get("AT").get("mx"),2)
            if mars_weather.get(sol_id).get("PRE") != None:
                sol_dict["average_pressure"] = round(mars_weather.get(sol_id).get("PRE").get("av"),2)
                sol_dict["min_pressure"] = round(mars_weather.get(sol_id).get("PRE").get("mn"),2)
                sol_dict["max_pressure"] = round(mars_weather.get(sol_id).get("PRE").get("mx"),2)
                if mars_weather.get(sol_id).get("HWS") != None:
                    sol_dict["average_wind"] = round(mars_weather.get(sol_id).get("HWS").get("av"),2)
                    sol_dict["min_wind"] = round(mars_weather.get(sol_id).get("HWS").get("mn"),2)
                    sol_dict["max_wind"] = round(mars_weather.get(sol_id).get("HWS").get("mx"),2)
                    sol_list.append(sol_dict)
    return sol_list

def get_formatted_time(utc_time):
    utc_time = utc_time.replace('T', '')
    utc_time = utc_time.replace('Z','')
    utc_time = datetime.strptime(utc_time, "%Y-%m-%d%H:%M:%S")
    return utc_time.strftime("%b %d")


weather = get_mars_weather()
print(weather)

