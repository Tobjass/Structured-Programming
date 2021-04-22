# Business rules voor Recommendation Engine

## Regels
### Soortgelijke producten (content filtering)
#### Regel 1
Als het product een subsubcategorie en gender heeft kan er mee gewerkt worden.

p = het product heeft een subsubcategorie, g = het product heeft een gender, w = er kan mee gewerkt worden

(p ∧ g) → w

#### Regel 2
Als een product in dezelfde subsubcategorie en gender valt als het product wat bekeken wordt is deze soortgelijk.

p = product valt in dezelfde subsubcategorie als het product wat bekeken wordt, g = product valt in dezelfde gender als het product wat bekeken wordt, s = producten zijn soortgelijk

(p ∧ g) → s


### Samen gekochte producten (collaborative filtering)
#### Regel 1
Als het product wat bekeken wordt gekocht is met andere producten vallen de producten uit die sessie onder ‘samen gekochte producten’.

p = het product wat bekeken wordt is samen met andere producten gekocht, s = de producten uit die sessie vallen onder ‘samen gekochte producten’

p → s

#### Regel 2
Als het product uit een sessie niet gelijk is aan het product wat bekeken wordt kan het later aanbevolen worden.

p = het product uit een sessie is gelijk aan het product wat bekeken wordt, a = kan later aanbevolen worden

¬p → a


## Werking
De recommendation engine werkt als volgt:

Eerst worden alle soortgelijke, eerder bekeken en eerder gekochte producten naar de relationele database gestuurd via het py-bestand genaamd 'Recommendation engine'. Hoe dit precies werkt is terug te vinden in het commentaar in het bestand zelf. Dit bestand hoeft maar 1x gebruikt te worden, omdat er per product en soort een recommendation wordt aangemaakt in de database. Vervolgens kan er via het py-bestand genaamd 'Data tonen' opgevraagd worden welke producten aanbevolen worden. Er zal worden gevraagd wat het product-id is, en dan wordt er per soort recommendation 5 producten getoond (als er meer dan 5 aanwezig zijn zullen er 5 random gekozen worden). Op de website gaat dit natuurlijk automatisch; de website stuurt dan naar de code wat het product-id van het product dat bekeken wordt is. Hoe dit bestand precies werkt is terug te vinden in het commentaar

Screenshots van data tonen:
![image](https://user-images.githubusercontent.com/74547189/111639331-72f2fc00-87fb-11eb-9ecf-7f3bd3c3e0d8.png)
![image](https://user-images.githubusercontent.com/74547189/111639554-a59cf480-87fb-11eb-9ed8-8bf3fa7c1aec.png)
![image](https://user-images.githubusercontent.com/74547189/111640176-396ec080-87fc-11eb-893c-4e4f224e86b8.png)
