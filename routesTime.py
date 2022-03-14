import requests
import pandas as pd

response = requests.get('https://sirius.searates.com/distance-and-time/search?type=sea&speed=13&lat_from=-23.9678823&lng_from=-46.3288865&lat_to=22.3192011&lng_to=114.1696121&from_country_code=BR&to_country_code=HK')
response_json = response.json()
# print(response_json)
#print(response_json['sea']['transit_time_days'])
print(response_json['transit_time_chart']['drilldown'][1]['name'])
print(response_json['transit_time_chart']['drilldown'][1]['y'])

data = pd.DataFrame(columns=[ 'origem', 'destino', 'empresa', 'tempo',])

data.at[j, 'origem'] = origem