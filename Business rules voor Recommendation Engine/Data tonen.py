import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="MongoDB",
    user="postgres",
    password=" "
)
cur = con.cursor()


def soortgelijkProduct_dataTonen(id):
    cur.execute("select name from products where product_id = '{}'".format(id))
    print("\nProducten die vergelijkbaar zijn met '{}':\n".format(cur.fetchall()[0][0]))

    cur.execute("select soortgelijk_id from soortgelijkproduct where product_id = '{}'".format(id))
    soortgelijk_id = cur.fetchall()

    for x in soortgelijk_id[0][0][1:len(soortgelijk_id[0][0])-1:].split(','):
        cur.execute("select name from products where product_id = '{}'".format(x))
        print("{}   ({})".format(cur.fetchall()[0][0], x))


def andereBekeken_dataTonen(id):
    cur.execute("select name from products where product_id = '{}'".format(id))
    print("\nEerder bekeken producten die vergelijkbaar zijn met '{}':\n".format(cur.fetchall()[0][0]))

    cur.execute("select anderebekeken_id from anderebekeken where product_id = '{}'".format(id))
    anderebekeken_id = cur.fetchall()

    for x in anderebekeken_id[0][0][1:len(anderebekeken_id[0][0]) - 1:].split(','):
        cur.execute("select name from products where product_id = '{}'".format(x))
        print("{}   ({})".format(cur.fetchall()[0][0], x))


andereBekeken_dataTonen(input("Product id?\n>> "))
