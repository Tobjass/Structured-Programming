import psycopg2
from pymongo import MongoClient


def uploaden(con, client):
    cur = con.cursor()
    db = client['huwebshop']

    cur.execute("DROP TABLE IF EXISTS sessions; DROP TABLE IF EXISTS profiles; DROP TABLE IF EXISTS products; CREATE TABLE products(product_id VARCHAR(29) NOT NULL, brand VARCHAR(27) NULL, category VARCHAR(44) NULL, color VARCHAR(14) NULL, description VARCHAR(1001) NULL, gender VARCHAR(16) NULL, herhaalaankopen BOOLEAN NOT NULL, name VARCHAR(89) NOT NULL, price DECIMAL(6, 2) NOT NULL, discount VARCHAR(12) NULL, doelgroep VARCHAR(15) NULL, sub_category VARCHAR(26) NULL, sub_sub_category VARCHAR(34) NULL, PRIMARY KEY(product_id)); CREATE TABLE profiles(profile_id VARCHAR(25) NOT NULL, buids VARCHAR(10369) NULL, viewed_before VARCHAR(131) NULL, similars VARCHAR(127) NULL, previously_recommended VARCHAR(4295) NULL, product_id VARCHAR(29) NULL, PRIMARY KEY(profile_id), FOREIGN KEY(product_id) REFERENCES products(product_id)); CREATE TABLE sessions(session_id VARCHAR(83) NOT NULL, buid VARCHAR(505), session_start TIMESTAMP NOT NULL, session_end TIMESTAMP NOT NULL, has_sale BOOLEAN NOT NULL, order_products VARCHAR(1051) NULL, product_id VARCHAR(29) NULL, profile_id VARCHAR(25) NULL, PRIMARY KEY(session_id), FOREIGN KEY(product_id) REFERENCES products(product_id), FOREIGN KEY(profile_id) REFERENCES profiles(profile_id))")

    for x in db.products.find({}):
        try:
            name = x['name']
        except:
            continue

        cur.execute(
            "insert into products (product_id, brand, category, color, description, gender, herhaalaankopen, name, price, discount, doelgroep, sub_category, sub_sub_category) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (x['_id'], x['brand'], x['category'], x['color'], x['description'], x['gender'],
             x.get('herhaalaankopen', False), name, x['price']['selling_price'] / 100, x['properties'].get('discount'),
             x['properties'].get('doelgroep'), x.get('sub_category'), x.get('sub_sub_category')))

    for x in db.profiles.find({}):
        cur.execute(
            "insert into profiles (profile_id, buids, viewed_before, similars, previously_recommended) values (%s, %s, %s, %s, %s)",
            (str(x['_id']), None if (not x.get('buids')) else x.get('buids'),
             None if (x.get('recommendations') is None or not x['recommendations'].get('viewed_before')) else x[
                 'recommendations'].get('viewed_before'),
             None if (x.get('recommendations') is None or not x['recommendations'].get('similars')) else x[
                 'recommendations'].get('similars'),
             None if (not x.get('previously_recommended')) else x.get('previously_recommended')))

    for x in db.sessions.find({}):
        try:
            buid = x['buid'][0] if (len(x['buid']) == 1 and type(x['buid'][0]) is str) else (
                x['buid'][0][0] if (len(x['buid']) == 1) else (
                    x['buid'] if (type(x['buid'][0]) is str and type(x['buid'][1]) is str) else (
                        [x['buid'][0], x['buid'][1][0]] if (type(x['buid'][0]) is str) else (
                            [x['buid'][0][0], x['buid'][1]]))))
        except:
            buid = None

        cur.execute(
            "insert into sessions (session_id, buid, session_start, session_end, has_sale, order_products) values (%s, %s, %s, %s, %s, %s)",
            (str(x['_id']), buid, x['session_start'], x['session_end'], x['has_sale'],
             None if (x.get('order') is None or not x['order'].get('products')) else str(x['order'].get('products'))))

    client.close()
    con.commit()
    cur.close()
    con.close()


uploaden(psycopg2.connect(
    host="localhost",
    database="huwebshop",
    user="postgres",
    password=" "
), MongoClient('localhost' +':'+ '27017'))

"""
Uploaden van alle data uit de MongoDB naar de relationele database. Bij het aanroepen van de functie worden de
connecties meegegeven om globals te vermijden. Eerst worden de cursors voor de relationele database en MongoDB
aangemaakt. Vervolgens wordt het DDL script uitgevoerd om de 3 tabellen aan te maken. Een overzichtelijkere versie van
dit script is te vinden in de readme file van dit mapje. De data moet na elkaar geüpload worden om foreign keys mogelijk
te maken. Bij elke for loop wordt de data uit de MongoDB gehaald, en in de cursor genaamd 'cur' verwerkt en
doorgestuurd naar de relationele database. Als het uploaden voltooid is worden de connecties gesloten.
"""
