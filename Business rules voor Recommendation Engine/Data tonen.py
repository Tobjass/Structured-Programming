import psycopg2


def meestvoorkomende(data):
    if len(set(data)) > 4:
        lijst = []
        for i in range(0, 4):
            meestvoorkomende = max(set(data), key=data.count)
            data = [x for x in data if x != meestvoorkomende]
            lijst.append(meestvoorkomende)
    elif 0 < len(set(data)) <= 4:
        lijst = list(set(data))
    elif len(set(data)) == 0:
        lijst = None
    return lijst
"""
Bepalen welke product-ids het meest in de meegegeven lijst voorkomen. Als er meer dan 4 verschillende ids zijn, wordt
eerst het meest voorkomende product bepaald. Vervolgens wordt deze uit de lijst gehaald, en aan de eerder aangemaakte
lijst toegevoegd. Dit wordt in totaal 4x herhaald. Als het aantal verschillende producten tussen 1 en 4 zit wordt deze
als set returned. Als de meegegeven lijst leeg is wordt None returned.
"""


def printen(con, data):
    cur = con.cursor()
    for x in data:
        cur.execute("select name from products where product_id = '{}'".format(x))
        print("{}   ({})".format(cur.fetchone()[0], x))
"""
Printen van de data. Omdat er 2 verschillende datalijsten zijn, is hier een functie voor gemaakt om dubbele code te
voorkomen. Per product haalt het de naam op, en wordt ie vervolgens geprint.
"""


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
Data uit de relationele database halen en tonen. Na het ophalen van de data worden de meestvoorkomende producten in
soortgelijk en samengekocht bepaald, d.m.v. de functie 'meestvoorkomende'. Vervolgens wordt de naam van het product-id
wat aan de functie meegegeven is opgehaald, en geprint om de data netjes te tonen. Soortgelijk en samengekocht worden
d.m.v. de functie 'printen' getoond.
"""


tonen(psycopg2.connect(
    host="localhost",
    database="huwebshop",
    user="postgres",
    password=" "
), input("Id?\n>> "))
