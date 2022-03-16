import requests
import pandas as pd


df = pd.read_csv("routes2.csv", sep=";")

empresaNull = "Não informado"

data = pd.DataFrame(columns=['origem', 'pais de origem', 'destino', 'pais de destino', 'empresa', 'tempo', 'latitude origem', 'longitude origem', 'latitude destino', 'longitude destino'])

j = 0
archive = open('routesTime.csv', 'w')
archive.close()

for i in range(len(df.index)):
    speed = 17 #Velocidade de cruzeiro
    latitudeFrom = df.loc[i, "Latitude de origem"]
    longitudeFrom = df.loc[i, "Longitude de origem"]
    latitudeTo = df.loc[i, "Latitude de destino"]
    longitudeTo = df.loc[i, "Longitude de destino"]
    countryCodeFrom = df.loc[i, "Pais de origem"]
    countryCodeTO = df.loc[i, "Pais de destino"]

    response = requests.get('https://sirius.searates.com/distance-and-time/search?type=sea&speed='+str(speed)+'&lat_from='+str(latitudeFrom)+'&lng_from='+str(longitudeFrom)+'&lat_to='+str(latitudeTo)+'&lng_to='+str(longitudeTo)+'&from_country_code='+countryCodeFrom+'&to_country_code='+countryCodeTO+'')
    response_json = response.json()

    if len(response_json['transit_time_chart']) == 1:
        dataNew = pd.DataFrame(columns=['origem', 'pais de origem', 'destino', 'pais de destino', 'empresa', 'tempo', 'latitude origem', 'longitude origem', 'latitude destino', 'longitude destino'])
        dataNew.at[0, 'origem'] = df.loc[i, "Origem"]
        dataNew.at[0, 'pais de origem'] = df.loc[i, "Pais de origem"]
        dataNew.at[0, 'latitude origem'] = df.loc[i, "Latitude de origem"]
        dataNew.at[0, 'longitude origem'] = df.loc[i, "Longitude de origem"]
        dataNew.at[0, 'destino'] = df.loc[i, "destino"]
        dataNew.at[0, 'pais de destino'] = df.loc[i, "Pais de destino"]
        dataNew.at[0, 'latitude destino'] = df.loc[i, "Latitude de destino"]
        dataNew.at[0, 'longitude destino'] = df.loc[i, "Longitude de destino"]
        dataNew.at[0, 'empresa'] = empresaNull
        dataNew.at[0, 'tempo'] = response_json['sea']['transit_time_days']
        data = data.append(dataNew, ignore_index=True)
    else:
        dataNew = pd.DataFrame(columns=['origem', 'pais de origem', 'destino', 'pais de destino', 'empresa', 'tempo', 'latitude origem', 'longitude origem', 'latitude destino', 'longitude destino'])
        for j in range(len(response_json['transit_time_chart']['drilldown'])):
            dataNew.at[j, 'origem'] = df.loc[i, "Origem"]
            dataNew.at[j, 'pais de origem'] = df.loc[i, "Pais de origem"]
            dataNew.at[j, 'latitude origem'] = df.loc[i, "Latitude de origem"]
            dataNew.at[j, 'longitude origem'] = df.loc[i, "Longitude de origem"]
            dataNew.at[j, 'destino'] = df.loc[i, "destino"]
            dataNew.at[j, 'pais de destino'] = df.loc[i, "Pais de destino"]
            dataNew.at[j, 'latitude destino'] = df.loc[i, "Latitude de destino"]
            dataNew.at[j, 'longitude destino'] = df.loc[i, "Longitude de destino"]
            dataNew.at[j, 'empresa'] = response_json['transit_time_chart']['drilldown'][j]['name']
            dataNew.at[j, 'tempo'] = response_json['transit_time_chart']['drilldown'][j]['y']
            print('j',j)
        data = data.append(dataNew, ignore_index=True)
    print('i',i)
    data.to_csv("routesTime.csv", sep=";", mode='a', header=False, index=False)
    





# response_json = response.json()
# # print(response_json)
# #print(response_json['sea']['transit_time_days'])
# print(response_json['transit_time_chart']['drilldown'][0]['name'])
# print(response_json['transit_time_chart']['drilldown'][1]['y'])

# data = pd.DataFrame(columns=['origem', 'pais de origem', 'destino', 'pais de destino', 'empresa', 'tempo', 'latitude origem', 'longitude origem', 'latitude destino', 'longitude destino'])

# # data.at[j, 'origem'] = origem