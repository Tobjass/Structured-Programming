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
### Creëren van nieuwe kennis
Het py-bestand genaamd 'Recommendation engine' maakt recommendations per product in de relationele database aan. Deze recommendations zijn gebaseerd op de bovenstaande regels.
Dit bestand is bedoeld voor eenmalig gebruik, aangezien de nieuwe data wordt opgeslagen in de relationele database. Hoe deze code precies werkt is terug te vinden in het commentaar van dit bestand.

### Data visueel tonen
Het py-bestand genaamd 'Data tonen' haalt de kennis die is gecreëerd door 'Recommendation engine' op. Hoe deze code precies werkt is terug te vinden in het commentaar van dit bestand.

Voorbeelden:

![image](https://user-images.githubusercontent.com/74547189/115705814-43409200-a36d-11eb-9b24-47d35e153c9d.png)
![image](https://user-images.githubusercontent.com/74547189/115705895-60756080-a36d-11eb-9cef-15dc3498cbf4.png)
![image](https://user-images.githubusercontent.com/74547189/115705974-7551f400-a36d-11eb-811c-153feec71adc.png)

