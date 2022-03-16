citiesArchive = open('cities.txt')
cities = citiesArchive.readlines()
lenCities = len(cities)

routesArchive = open('routes2.csv', 'a')
routesArchive.write('"Origem";"Pais de origem";"Latitude de origem";"Longitude de origem";"destino";"Pais de destino";"Latitude de destino";"Longitude de destino"\n')

for i in range(lenCities):
    for j in range(lenCities):
        if cities[i] != cities[j]:
            citieI = cities[i].rstrip('\n').split(',')
            citieJ = cities[j].rstrip('\n').split(',')
            routesArchive.write('"'+citieI[0]+'";"'+citieI[1]+'";"'+citieI[2]+'";"'+citieI[3]+'";"'+citieJ[0]+'";"'+citieJ[1]+'";"'+citieJ[2]+'";"'+citieJ[3]+'"\n')

routesArchive.close()