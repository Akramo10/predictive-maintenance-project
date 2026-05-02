# Projet de Maintenance Prédictive 🚀

## 📌 Description
Ce projet a pour objectif de développer une solution de maintenance prédictive à partir de données issues de capteurs industriels. L’analyse des métriques permet d’anticiper les pannes machines avant qu’elles ne surviennent.

## 🎯 Objectif
L’objectif est de construire un modèle capable de distinguer les comportements normaux des situations de panne en exploitant plusieurs variables issues de capteurs. Cela permet d’optimiser la maintenance et de réduire les arrêts imprévus.

## 📊 Dataset
Le dataset contient :
- Des mesures de capteurs (`metric1` à `metric9`)
- Un identifiant machine (`device`)
- Une date (`date`)
- Une variable cible (`failure`)

Chaque ligne représente l’état d’une machine à un instant donné.

## ⚠️ Problatique principale
Le dataset est fortement déséquilibré :
- ~99.9% de données normales
- ~0.1% de pannes

Cela nécessite une attention particulière lors de la modélisation.

## 🔍 Analyse Exploratoire (EDA)
Les analyses réalisées :
- Compréhension de la structure des données
- Étude de la variable cible
- Comparaison entre machines normales et en panne
- Visualisations (histogrammes, boxplots, corrélation)

### Résultats importants :
Certaines métriques comme :
- `metric2`
- `metric4`
- `metric7`
- `metric8`

présentent des différences significatives et sont fortement liées aux pannes.

## ⚙️ Prétraitement des données
- Conversion de la colonne date en format datetime
- Suppression des doublons
- Séparation entre données brutes et données traitées

## 🤖 Modélisation
Un modèle de machine learning (Random Forest) est utilisé :
- Adapté aux données tabulaires
- Capable de capturer des relations complexes
- Utilisation de `class_weight="balanced"` pour gérer le déséquilibre

## 📈 Évaluation
Les métriques utilisées :
- Recall (très important pour détecter les pannes)
- Précision
- F1-score
- Matrice de confusion

## 📁 Structure du projet
