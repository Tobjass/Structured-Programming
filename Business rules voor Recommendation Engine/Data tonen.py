import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="MongoDB",
    user="postgres",
    password=" "
)
cur = con.cursor()


def dataTonen(type, id):
    if type == 1:
        tekst = 'Producten'
        cur.execute("select soortgelijk_id from soortgelijkproduct where product_id = '{}'".format(id))
    elif type == 2:
        tekst = 'Eerder bekeken producten'
        cur.execute("select anderebekeken_id from anderebekeken where product_id = '{}'".format(id))
    elif type == 3:
        tekst = 'Eerder gekochte producten'
        cur.execute("select anderekochten_id from anderekochten where product_id = '{}'".format(id))
    ids = cur.fetchall()

    cur.execute("select name from products where product_id = '{}'".format(id))
    print("\n{} die vergelijkbaar zijn met '{}':\n".format(tekst, cur.fetchall()[0][0]))

    for x in ids[0][0][1:len(ids[0][0])-1:].split(','):
        cur.execute("select name from products where product_id = '{}'".format(x))
        print("{}   ({})".format(cur.fetchall()[0][0], x))


dataTonen(3, input("Product id?\n>> "))
