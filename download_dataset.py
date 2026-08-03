import json
import requests


def download() -> None:
    r = requests.get("https://archive-api.open-meteo.com/v1/archive", params={
        "latitude": 24.3745, "longitude": 88.6042,
        "start_date": "2026-06-05", "end_date": "2026-08-03",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,relative_humidity_2m_mean",
        "timezone": "auto"
    })

    with open('dataset.json', 'w') as file:
        json.dump(r.json(), file, indent=2)
    
    print('Dataset downloaded.')


download()
