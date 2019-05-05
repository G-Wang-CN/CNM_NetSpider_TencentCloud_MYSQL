import urllib.request
import urllib.parse
import mysql.connector
import json

'''
本代码用于对中央气象台发布天气预报的数据进行采集。



'''


def get_city_url(locationId):
    """for given location ID(s), search from MySQL server and find relevent url for getting data"""
    cnx = mysql.connector.connect(user='%User', password='%Password', host='%host', port='%port',
                                  database='%database')
    cursor = cnx.cursor()
    query = ("SELECT url FROM Location WHERE locationID = %s" % locationId)
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        searchLink = result[0][0]
        return searchLink
    except:
       print("Error: unable to fecth data")


def get_data(searchlink):
    """for the given url address,"""
    url = searchlink
#    Url = 'http://www.nmc.cn/f/rest/real/54399?_=1544806754524'
    r = urllib.request.Request(url)
    r.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    response = urllib.request.urlopen(r)
    qqq = json.load(response)
    print(qqq)

    Weatherdata={}
    Weatherdata['tempTime'] = qqq['publish_time']
    Weatherdata['locationId'] = int(qqq['station']['code'])
    Weatherdata['temperature_C'] = qqq['weather']['temperature']
    Weatherdata['rain'] = qqq['weather']['rain']
    Weatherdata['humidity'] = qqq['weather']['humidity']
    Weatherdata['WeatherInfo'] = qqq['weather']['info']
    Weatherdata['WindDirect'] = qqq['wind']['direct']
    Weatherdata['WindPower'] = qqq['wind']['power']
    Weatherdata['WindSpeed'] = qqq['wind']['speed']
    return Weatherdata
