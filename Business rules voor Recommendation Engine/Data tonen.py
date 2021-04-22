import psycopg2
import random


def meestvoorkomende(data):
    if len(set(data)) >= 4:
        lijst = []
        for i in range(0, 4):
            meestvoorkomende = max(set(data), key=data.count)
            data = [x for x in data if x != meestvoorkomende]
            lijst.append(meestvoorkomende)
    elif len(set(data)) != 0:
        lijst = list(set(data))
    elif len(set(data)) == 0:
        lijst = None
    return lijst


def printen(con, data):
    cur = con.cursor()
    for x in data:
        cur.execute("select name from products where product_id = '{}'".format(x))
        print("{}   ({})".format(cur.fetchone()[0], x))


def tonen(con, id):
    cur = con.cursor()

    cur.execute("select * from sp_opdracht3 where product_id = '{}'".format(id))
    data = cur.fetchone()

    soortgelijk, samengekocht = meestvoorkomende(data[1].strip('{}').split(',')), meestvoorkomende(
        data[2].strip('{}').split(','))

    cur.execute("select name from products where product_id = '{}'".format(id))
    name = cur.fetchone()[0]
    print("Producten die vergelijkbaar zijn met '{}':\n".format(name))
    printen(con, soortgelijk)
    print("\n\nProducten die goed combineren met '{}':\n".format(name))
    printen(con, samengekocht)

    cur.close()
    con.close()
"""
Visueel tonen van de recommendations. Deze wordt opgeroepen in de functie dataTonen. Het splitst eerst de data zodat het
goed verwerkt kan worden. Vervolgens wordt de naam die bij het product dat bekeken wordt hoort opgehaald. Hierna wordt
er een lijst aangemaakt die het vorige product wat getoond is te onthouden, en dus niet opnieuw te tonen. Vervolgens
loopt er een for loop 5 keer. In deze loop bevindt zich een while loop, die blijft lopen totdat het een nieuw id wat
niet eerder getoond is heeft. Als dit het geval is wordt de naam van het aanbevolen product opgehaald en geprint. 
"""


tonen(psycopg2.connect(
    host="localhost",
    database="huwebshop",
    user="postgres",
    password=" "
), 3540)

# input("Id?\n>> ")
