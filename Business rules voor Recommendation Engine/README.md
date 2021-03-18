Business rules voor Recommendation Engine


De recommendation engine werkt als volgt:

Eerst worden alle soortgelijke, eerder bekeken en eerder gekochte producten naar de relationele database gestuurd via het py-bestand genaamd 'Recommendation engine'. Hoe dit precies werkt is terug te vinden in het commentaar in het bestand zelf. Dit bestand hoeft maar 1x gebruikt te worden, omdat er per product en soort een recommendation wordt aangemaakt in de database. Vervolgens kan er via het py-bestand genaamd 'Data tonen' opgevraagd worden welke producten aanbevolen worden. Er zal worden gevraagd wat het product-id is, en dan wordt er per soort recommendation 5 producten getoond (als er meer dan 5 aanwezig zijn zullen er 5 random gekozen worden). Op de website gaat dit natuurlijk automatisch; de website stuurt dan naar de code wat het product-id van het product dat bekeken wordt is. Hoe dit bestand precies werkt is terug te vinden in het commentaar

Screenshots van data tonen:
![image](https://user-images.githubusercontent.com/74547189/111639331-72f2fc00-87fb-11eb-9ecf-7f3bd3c3e0d8.png)
![image](https://user-images.githubusercontent.com/74547189/111639554-a59cf480-87fb-11eb-9ed8-8bf3fa7c1aec.png)
![image](https://user-images.githubusercontent.com/74547189/111640176-396ec080-87fc-11eb-893c-4e4f224e86b8.png)
