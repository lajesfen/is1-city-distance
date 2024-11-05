from math import radians, cos, sin, asin, sqrt
import requests
import csv

class CoordinateFinder:
    def getDataFromAPI(self, city, country):
        url = f'https://nominatim.openstreetmap.org/search?q={city.lower()},{country.lower()}&format=json'
        try:
            response = requests.get(url)

            if response.status_code == 200 and response.json():
                posts = response.json()
                return { 'lat': posts[0]['lat'], 'lon': posts[0]['lon'] }
            else:
                print(f'Error fetching data from API: {response.status_code}')
                return None

        except requests.RequestException as e:
            print(f'Error fetching data from API: {e}')
            return None

    def getDataFromCSV(self, city, country):
        try:
            with open('data/worldcities.csv', mode ='r') as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    if lines[1].lower() == city.lower() and lines[4].lower() == country.lower():
                        return { 'lat': lines[2], 'lon': lines[3] }
        except FileNotFoundError:
            print("Archivo CSV no encontrado.")
        except Exception as e:
            print(f"Error leyendo el archivo CSV: {e}")
        return None 

    def getData(self, city, country, option):
        match option:
            case "API":
                return self.getDataFromAPI(city, country)
            case "CSV":
                return self.getDataFromCSV(city, country)

class DistanceCalculator:
    def calcDistance(self, lat1, lon1, lat2, lon2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dislon = lon2 - lon1 
        dislat = lat2 - lat1 
        a = sin(dislat/2)**2 + cos(lat1) * cos(lat2) * sin(dislon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371
        return c * r

class Interface:
    def getDistance(self, city1, country1, city2, country2, option):
        coordFinder = CoordinateFinder()
        distCalc = DistanceCalculator()

        data1 = coordFinder.getData(city1, country1, option)
        data2 = coordFinder.getData(city2, country2, option)

        if data1 and data2:
            distance = distCalc.calcDistance(float(data1['lat']), float(data1['lon']), float(data2['lat']), float(data2['lon']))
            print(f"La distancia entre {city1}, {country1} y {city2}, {country2} es de {round(distance, 2)} km.")
        else:
            print("No se encontraron los datos de las ciudades.")

interface = Interface()
interface.getDistance("Bogota", "Colombia", "Lima", "Peru", "CSV")