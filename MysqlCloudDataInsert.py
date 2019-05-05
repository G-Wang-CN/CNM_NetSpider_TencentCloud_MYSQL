from __future__ import print_function
import mysql.connector
import mysql.connector.errors
import time


def InsertFunction(tableName):
    '''
    match the table name with database and return the matched insert function
    '''
    if (tableName == 'WeatherData') :
        InsertFunc = ("INSERT INTO WeatherData"
                      "(tempTime,locationId,temperature_C,Rain,Humidity,WeatherInfo,WindDirect,WindPower,WindSpeed)"
                      "VALUES (%(tempTime)s,%(locationId)s,%(temperature_C)s,%(rain)s,%(humidity)s,%(WeatherInfo)s,%(WindDirect)s,%(WindPower)s,%(WindSpeed)s)")
    elif tableName == 'SearchLinks':
        InsertFunc = ("INSERT INTO SearchLinks(article_name,article_link)"
                      "VALUES (%(article_name)s,%(article_link)s)")
    else:
        print('No table matched！')
        InsertFunc = ("")
    return InsertFunc


def MysqlCloudDataInsert(tableName, data):
    print('processing to insert weather data into database')
    cnx = mysql.connector.connect(user='%User', password='%Password', host='%host', port='%port',
                                  database='%database')
    cursor = cnx.cursor()
    try:
        cursor.execute(InsertFunction(tableName), data)
        cnx.commit()
    except mysql.connector.errors:
        print("data insert error")
    cursor.close()
    cnx.close()
    return print( 'Data insert completed.')


'''
# Insert  
add_employee = ("INSERT INTO employee "
                "(first_name, last_name, hire_date, gender, birth_date) "
                "VALUES (%s, %s, %s, %s, %s)")
data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

# Insert 
add_salary = ("INSERT INTO salaries "
              "(emp_no, salary, from_date, to_date) "
              "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
data_salary = {
 'emp_no': emp_no,
 'salary': 50000,
 'from_date': tomorrow,
 'to_date': date(9999, 1, 1),
}
cursor.execute(add_salary, data_salary)
'''
