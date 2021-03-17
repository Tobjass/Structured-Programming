import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="MongoDB",
    user="postgres",
    password=" "
)
cur = con.cursor()


def tonen(id, tekst, ids):
    cur.execute("select name from products where product_id = '{}'".format(id))
    print("\n{} die vergelijkbaar zijn met '{}':\n".format(tekst, cur.fetchall()[0][0]))

    for x in ids[0][0][1:len(ids[0][0]) - 1:].split(','):
        cur.execute("select name from products where product_id = '{}'".format(x))
        print("{}   ({})".format(cur.fetchall()[0][0], x))


def dataTonen(id):
    cur.execute("select soortgelijk_id from soortgelijkproduct where product_id = '{}'".format(id))
    tonen(id, 'Producten', cur.fetchall())

    cur.execute("select anderebekeken_id from anderebekeken where product_id = '{}'".format(id))
    tonen(id, 'Eerder bekeken producten', cur.fetchall())

    cur.execute("select anderekochten_id from anderekochten where product_id = '{}'".format(id))
    tonen(id, 'Eerder gekochte producten', cur.fetchall())


dataTonen(input("Product id?\n>> "))
