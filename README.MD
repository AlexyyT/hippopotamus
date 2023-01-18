# Documentation

### Scrapping Amazon
Récupèrer des avis clients sur le site amazon.fr afin de se construire une base de données d'apprentissage pour le modèle d'analyse de sentiments.

 - [x] Parser une page de selection de produit. Pour tous les produits de la page, on peut récupérer les éléments suivants :
   - [x] Nom du produit
   - [x] Note moyenne
   - [x] Nombre d'évaluations
   - [x] Prix
   - [x] Devise
   - [x] Url de la page amazon du produit
   - [x] Position du produit sur la page
   - [x] Page sur laquelle le produit est positionné
 - [x] Récupérer toutes les reviews d'un produit spécifique. On récupère les éléments suivants :
   - [x] Titre de l'avis
   - [x] Note de l'avis
   - [x] Date à laquelle l'avis à été laissé
   - [x] Les spécificités du produit concerné (couleur...)
   - [x] Acheteurs certifié ou non
   - [x] Verbatim de l'avis client
 - Reste à faire :
 - [ ] Anti erreur parseur => quand le parse fonctionne mais renvoi une erreur de connexion.

## Analyse de sentiments
L'objectif de ce programme est, à partir d'évaluation clients, pouvoir dégager pour chaque avis des causes de satisfaction ou d'insatisfaction.
### Pré-traitement de la donnée

 - [x] Charger le fichier
 - [ ] Dataframe => Liste
 - [ ] Appliquer un regex
 - [ ] Supprimer les traductions
 - [ ] Retourner la liste dans le dataframe

### Connecter les données au modèle de NLP


### Analyse de sentiments


### Définition de thèmes


