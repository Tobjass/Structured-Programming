## Soortgelijke producten (content filtering)
### Regel 1
Als het product een subsubcategorie en gender heeft kan er mee gewerkt worden.
p = het product heeft een subsubcategorie, g = het product heeft een gender, w = er kan mee gewerkt worden
(p ∧ g) → w

### Regel 2
Als een product in dezelfde subsubcategorie en gender valt als het product wat bekeken wordt is deze soortgelijk.
p = product valt in dezelfde subsubcategorie als het product wat bekeken wordt, g = product valt in dezelfde gender als het product wat bekeken wordt, s = producten zijn soortgelijk
(p ∧ g) → s


## Samen gekochte producten (collaborative filtering)
### Regel 1
Als het product wat bekeken wordt gekocht is met andere producten vallen de producten uit die sessie onder ‘samen gekochte producten’.
p = het product wat bekeken wordt is samen met andere producten gekocht, s = de producten uit die sessie vallen onder ‘samen gekochte producten’
p → s

### Regel 2
Als het product uit een sessie niet gelijk is aan het product wat bekeken wordt kan het later aanbevolen worden.
p = het product uit een sessie is gelijk aan het product wat bekeken wordt, a = kan later aanbevolen worden
¬p → a
