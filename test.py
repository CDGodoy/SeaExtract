import requests

response = requests.get("https://sirius.searates.com/distance-and-time/search?type=sea&speed=13&lat_from=-23.9678823&lng_from=-46.3288865&lat_to=-25.5148826&lng_to=-48.5225655&from_country_code=BR&to_country_code=BR")
# response = requests.get("https://sirius.searates.com/distance-and-time/search?type=sea&speed=13&lat_from=41.3517302&lng_from=-8.7478619&lat_to=22.3192011&lng_to=114.1696121&from_country_code=PT&to_country_code=HK")

response_json = response.json()

if len(response_json['transit_time_chart']) == 1:
    print(response_json['sea']['transit_time_days'])
else:
    print(len(response_json['transit_time_chart']['drilldown']))