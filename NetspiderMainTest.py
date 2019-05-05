import NMC_GetTemperature
import MysqlCloudDataInsert
import time
import random
import mysql.connector


def mainround(TempData, locationId):
    WeatherData = NMC_GetTemperature.get_data(NMC_GetTemperature.get_city_url(locationId))
    print(time.localtime(time.time()))
    if WeatherData != TempData:
        TempData = WeatherData
        MysqlCloudDataInsert.MysqlCloudDataInsert('WeatherData', WeatherData)
    return TempData


def location_id_search():
    cnx = mysql.connector.connect(user='%User', password='%Password', host='%host', port='%port',
                                  database='%database')
    cursor = cnx.cursor()
    query = ("SELECT locationID FROM Location")
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except:
       print("Error: unable to fecth data")

    cursor.close()
    cnx.close()

while True:
    # time.sleep(1800)
    LocationID = []
    LocationID = location_id_search()
    print(LocationID)
    weatherdatatemp = []
    i = 0
    while i < len(LocationID):
        weatherdatatemp.append({})
        i = i+1
    del i
    SearchRound = 71
    #20min a round 72 rounds a day, location data update per day
    while SearchRound >= 0 :
        BreakSec, j, SleepSec = 0, 0, 0
        while j < len(LocationID):
            weatherdatatemp[j] = mainround(weatherdatatemp[j], LocationID[j])
            j = j+1
            SleepSec = random.randint(1, 1000)/50
            time.sleep(SleepSec)
            BreakSec = BreakSec+SleepSec
        time.sleep(1200 - SleepSec + random.randrange(10000) / 100)
        SearchRound = SearchRound - 1

