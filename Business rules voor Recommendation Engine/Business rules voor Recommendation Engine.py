import psycopg2

con = psycopg2.connect(
    host="localhost",
    database="MongoDB",
    user="postgres",
    password=" "
)
cur = con.cursor()

cur.execute("select * from products where sub_sub_category is not null")
products = cur.fetchall()

def soortgelijkProduct():
    aantal = 0
    for producten in products:
        recommendations = []
        for x in products:
            if (x[2] == producten[2] and x[5] == producten[5]) and (x[11] == producten[11] and x[12] == producten[12]):
                recommendations.append(x[0])
        recommendations.remove(producten[0])

        aantal += 1
        print("{} / {}   ({:.1f}%)".format(aantal, 13676, aantal * 100 / 13676))

        cur.execute("insert into soortgelijkproduct (product_id, soortgelijk_id) values (%s, %s)",
                    (producten[0], recommendations))


con.commit()
cur.close()
con.close()