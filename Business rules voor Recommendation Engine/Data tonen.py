import psycopg2
import random


def tonen(con, id):
    cur = con.cursor()

    x = ids[0][0][1:len(ids[0][0]) - 1:].split(',')

    cur.execute("select name from products where product_id = '{}'".format(id))
    print("\n\n{} die vergelijkbaar zijn met '{}' (5/{}):\n".format(tekst, cur.fetchall()[0][0], len(x)))

    oude = []
    for i in range(0, 5):
        while True:
            randomid = random.randrange(0, len(x))
            if randomid in oude:
                continue
            else:
                oude.append(randomid)
                break
        cur.execute("select name from products where product_id = '{}'".format(x[randomid]))
        print("{}   ({})".format(cur.fetchall()[0][0], x[randomid]))
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
), input("Id?\n>> "))
