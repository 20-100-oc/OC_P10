# Projet 10: Développez un chatbot pour reserver des vacances 

## Contexte

L'entreprise Fly Me souhaite proposer à ses clients un chatbot pour réserver leurs billets d'avion.  
La tâche du chatbot sera d'extraire cinq informations pendant un dialogue avec un utilisateur:  
ville de départ, ville d'arrivée, date de départ, date d'arrivée et budget maximum pour le billet.  
Si l'utilisateur ne présise pas certaines de ces informations, le bot devr poser lui-même la question.  
Le chatbot devra poser lui-même des questions si l'utilisateur ne précise pas toutes ces informations, puis résumé l'échange et demander une confirmation finale de l'utilisateur.  
Le but est de créer un service de réservation intelligente plus rapide et agréable pour la clientèle en ligne.  


## Objectifs
- Mise en place du pipeline de compréhension du language naturel LUIS:
  - création du modèle
  - formatage et importation des données d'entraînement et de validation
  - entraînement et validation du modèle
  - exposition du modèle pour l'intégration au chatbot
- Architecture du chatbot
  - modification et adaptation de l'architecture standard "Microsoft Core Bot"
  - intégration du modèle LUIS
  - création de réponses automatisées (accueil de l'utilisateur, questions en cascades, confirmation de la demande, résumé de l'échange)
  - liaison de l'outil d'analyse des échanges avec utilisateurs (App Insights)
- Elaboration de tests unitaires pour vérifier le bon fonctionnement du chatbot lors du déploiement
- Déploiement cloud du chatbot (Azure web app)
- Mise en place de l'interface d'intéraction textuelle avec le chatbot (BotFramework Emulator)
- Rédaction d'un document explicatif de la ressource App Insights (suivi et analyse des échanges)
- Rédaction d'un document sur la méthode de mise à jour du modèle et de collecte des données

## Livrables
- Chatbot déployé et interface d'interaction
- Scripts du pipeline LUIS
- Documentation de l'outil de suivi et analyse
- Documentation de la méthodologie de pilotage des performances
- Présentation Powerpoint

## Outils
- Git / Github
- Jupyter notebook
- Azure Language Understanding (LUIS)
- Azure Web App
- Azure App insights
- BotFramework Emulator
- Microsoft Bot Framework SDK
- Python
  - numpy
  - requests
  - botbuilder-core
  - botframework-connector
  - botbuilder-schema
  - botbuilder-dialogs
  - botbuilder-ai #install luis 0.2.0
  - botbuilder-applicationinsights
  - botbuilder-integration-applicationinsights-aiohttp
  - datatypes-date-time
  - azure-cognitiveservices-language-luis
  - msrest
  - opencensus-ext-azure