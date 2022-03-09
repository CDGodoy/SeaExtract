citiesArchive = open('cities.txt')
cities = citiesArchive.readlines()
lenCities = len(cities)

routesArchive = open('routes.csv', 'a')

for i in range(lenCities):
    for j in range(lenCities):
        if cities[i] != cities[j]:
            routesArchive.write('"'+cities[i].rstrip('\n')+'";"'+cities[j].rstrip('\n')+'"\n')