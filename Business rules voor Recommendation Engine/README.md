Business rules voor Recommendation Engine


De recommendation engine werkt als volgt:

Eerst worden alle soortgelijke, eerder bekeken en eerder gekochte producten naar de relationele database gestuurd via het py-bestand genaamd 'Recommendation engine'. Hoe dit precies werkt is terug te vinden in het commentaar in het bestand zelf. Dit bestand hoeft maar 1x gebruikt te worden, omdat er per product en soort een recommendation wordt aangemaakt in de database. Vervolgens kan er via het py-bestand genaamd 'Data tonen' opgevraagd worden welke producten aanbevolen worden. Er zal worden gevraagd wat het product-id is, er vervolgens wordt er per soort recommendation 5 producten getoond (als er meer dan 5 aanwezig zijn zullen er 5 random gekozen worden). Op de website gaat dit natuurlijk automatisch, de website stuurt dan naar de code wat het product-id van het product dat bekeken wordt is. Hoe dit bestand precies werkt is terug te vinden in het commentaar.
