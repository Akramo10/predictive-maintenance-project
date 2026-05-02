# Projet de Maintenance Prédictive

## Description

Ce projet a pour objectif de développer une solution de maintenance
prédictive à partir de données issues de capteurs industriels. L'analyse
des métriques permet d'anticiper les pannes machines avant qu'elles ne
surviennent.
<img width="982" height="649" alt="image" src="https://github.com/user-attachments/assets/2b751408-26dc-4663-af5d-d0b6ebeae2de" />


## Objectif

L'objectif est de construire un modèle capable de distinguer les
comportements normaux des situations de panne en exploitant plusieurs
variables issues de capteurs. Cela permet d'optimiser la maintenance et
de réduire les arrêts imprévus.

## Dataset

Le dataset contient : - Des mesures de capteurs (metric1 à metric9) - Un
identifiant machine (device) - Une date (date) - Une variable cible
(failure)

Chaque ligne représente l'état d'une machine à un instant donné.

## Problématique principale

Le dataset est fortement déséquilibré : - Environ 99.9% de données
normales - Environ 0.1% de pannes

## Analyse exploratoire des données (EDA)

Les analyses réalisées : - Compréhension de la structure des données -
Étude de la variable cible - Comparaison entre machines normales et en
panne - Visualisations (histogrammes, boxplots, corrélations)

## Prétraitement des données

-   Conversion de la colonne date en format datetime
-   Suppression des doublons
-   Séparation entre données brutes et données traitées

## Modélisation

Un modèle Random Forest est utilisé avec gestion du déséquilibre via
class_weight.

## Évaluation

Les métriques utilisées : - Recall - Précision - F1-score - Matrice de
confusion

## Technologies utilisées

-   Python
-   Pandas
-   NumPy
-   Matplotlib / Seaborn
-   Scikit-learn

## Auteur

Akram
