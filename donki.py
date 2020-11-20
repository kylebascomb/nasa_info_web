import requests
import config


def get_notifications(api_key=config.nasa_api_key, url=config.donki_notif_url):
    notif_list = []
    payload = {"api_key": api_key}
    r = requests.get(url=url, params=payload)
    notif_list.extend(r.json())
    return notif_list

nlist = get_notifications()
for notif in nlist:
    print(notif)
