import psycopg2


def recommendations(con):
    cur = con.cursor()

    cur.execute("select product_id, gender, sub_sub_category from products where sub_sub_category is not null and gender is not null")
    products = cur.fetchall()

    for x in products:
        soortgelijk = []
        for y in products:
            if x[0] != y[0] and x[1:] == y[1:]:
                soortgelijk.append(y[0])

        cur.execute("select order_products from sessions where order_products LIKE '%{}%'".format(
            x[0].split("'")[1] if ("'" in x[0]) else x[0]))

        samengekocht = []
        for y in cur.fetchall():
            if x[0] in y[0] and y[0].count('{') > 1:
                if 'price' in y[0]:
                    for z in y[0].split(','):
                        if z[9:len(z)-1:] in products and z[9:len(z)-1:] != x[0]:
                            samengekocht.append(z[9:len(z)-1:])
                else:
                    for z in y[0][0:len(y[0])-1:].split(','):
                        if z[9:len(z)-2:] != x[0]:
                            samengekocht.append(z[9:len(z)-2:])

        cur.execute("insert into sp_opdracht3 (product_id, soortgelijk, samengekocht) values (%s, %s, %s)",
                    (x[0], None if (not soortgelijk) else soortgelijk, None if (not samengekocht) else samengekocht))

    con.commit()
    cur.close()
    con.close()
"""
Producten in dezelfde gender en sub_sub_category toevoegen aan de database. Per product wordt er gekeken welke producten 
vergelijkbaar zijn. Er loopt een for loop die elk product langs gaat. Als de gender en sub_sub_category gelijk zijn aan 
het product dat getoond wordt op de 'website' zal het worden toegevoegd aan de soortgelijk lijst. Daarna worden alle 
producten die samen met het product gekocht zijn opgehaald. Vervolgens wordt de data verwerkt en eventueel toegevoegd aan de
samengekocht lijst. Uiteindelijk wordt de data naar de database doorgestuurd.
"""

recommendations(psycopg2.connect(
    host="localhost",
    database="huwebshop",
    user="postgres",
    password=" "
))
