import psycopg2
import random

con = psycopg2.connect(
    host="localhost",
    database="MongoDB",
    user="postgres",
    password=" "
)
cur = con.cursor()


def tonen(id, tekst, ids):
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


def dataTonen(id):
    cur.execute("select soortgelijk_id from soortgelijkproduct where product_id = '{}'".format(id))
    tonen(id, 'Producten', cur.fetchall())

    cur.execute("select anderebekeken_id from anderebekeken where product_id = '{}'".format(id))
    tonen(id, 'Eerder bekeken producten', cur.fetchall())

    cur.execute("select anderekochten_id from anderekochten where product_id = '{}'".format(id))
    tonen(id, 'Eerder gekochte producten', cur.fetchall())
"""
Laat voor het product wat bekeken wordt recommendations zien 3 soorten recommendations zien; soortgelijke producten,
wat andere klanten eerder hebben bekeken & wat andere klanten eerder gekocht hebben. Deze functie gaat dus ook elke
soort 1 voor 1 na. De recommendations van het gegeven product-id worden uit de database gehaald, en doorgestuurd naar
een andere functie (tonen).
"""


dataTonen(input("Product id?\n>> "))
