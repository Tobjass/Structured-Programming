# Document Store naar Relationele Database

Dit is de verbeterde versie van de tweede summatieve opdracht van Structured Programming en is gemaakt door Tobias Kramer (1788287). De overige benodigdheden (alles behalve de code) zijn te vinden in de github van SP-Groep-4; https://github.com/Justinterhorst/SP-Groep-4/tree/main/2.%20Document%20Store%20naar%20Relationele%20Database. Dit zijn wel oudere versies aangezien ik deze verbeterd heb.

## Setup

Het uploaden van alle data van de MongoDB naar de relationele database kan gedaan worden door 'Data uploaden naar relationele database.py' te runnen. Hoe dit precies werkt is te vinden in het commentaar in dat bestand. 

## DDL Script

Dit is een overzichtelijkere versie van het DDL script wat gebruikt wordt in het python bestand. Dit hoeft verder niet gebruikt te worden.

```
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS profiles;
DROP TABLE IF EXISTS products;

CREATE TABLE products(
product_id VARCHAR(29) NOT NULL,
brand VARCHAR(27) NULL,
category VARCHAR(44) NULL,
color VARCHAR(14) NULL,
description VARCHAR(1001) NULL,
gender VARCHAR(16) NULL,
herhaalaankopen BOOLEAN NOT NULL,
name VARCHAR(89) NOT NULL,
price DECIMAL(6, 2) NOT NULL,
discount VARCHAR(12) NULL,
doelgroep VARCHAR(15) NULL,
sub_category VARCHAR(26) NULL,
sub_sub_category VARCHAR(34) NULL,
PRIMARY KEY(product_id)
);

CREATE TABLE profiles(
profile_id VARCHAR(25) NOT NULL,
buids VARCHAR(10369) NULL,
viewed_before VARCHAR(131) NULL,
similars VARCHAR(127) NULL,
previously_recommended VARCHAR(4295) NULL,
product_id VARCHAR(29) NULL,
PRIMARY KEY(profile_id),
FOREIGN KEY(product_id) REFERENCES products(product_id)
);

CREATE TABLE sessions(
session_id VARCHAR(83) NOT NULL,
buid VARCHAR(1881) NOT NULL,
session_start TIMESTAMP NOT NULL,
session_end TIMESTAMP NOT NULL,
has_sale BOOLEAN NOT NULL,
order_products VARCHAR(1051) NULL,
profile_id VARCHAR(25) NULL,
product_id VARCHAR(29) NULL,
PRIMARY KEY(session_id),
FOREIGN KEY(profile_id) REFERENCES profiles(profile_id),
FOREIGN KEY(product_id) REFERENCES products(product_id)
);
```
