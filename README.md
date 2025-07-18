# FoodFactProject
# 🥦 Analyse des prix alimentaires en France avec Open Food Facts

Ce projet explore les **prix et caractéristiques des produits alimentaires vendus en France**, en s’appuyant sur les données issues de l’**API Open Food Facts**. Une **pipeline de collecte et transformation** a été conçu pour centraliser les informations, les nettoyer, puis les modéliser afin d’alimenter un **tableau de bord Power BI interactif et orienté décision**.

---

## 🎯 Objectifs

- Collecter automatiquement les données nutritionnelles, geographique et tarifaires des produits alimentaires français
- Nettoyer, filtrer et enrichir ces données pour garantir leur qualité
- Construire un **modèle sémantique** facilitant l’analyse métier
- Visualiser les tendances et comparatifs grâce à Power BI

---

## 🔄 Pipeline de données

Le pipeline comprend les étapes suivantes :

1. **Extraction** : Requête vers l'API [Open Food Facts](https://fr.openfoodfacts.org/data) pour collecter les données produits (JSON)
2. **Transformation** :
   - Filtrage sur les produits commercialisés en France
   - Suppression des doublons et remplissage des valeurs manquantes
   - Normalisation des noms, catégories et marques
3. **Chargement** :
   - Données structurées intégrées dans Power BI via Power Query
   - Modèle relationnel & sémantique construit pour l’analyse

---

## 🧰 Technologies utilisées

| Outil / Service          | Rôle                                                          |
|--------------------------|---------------------------------------------------------------|
| **API Open Food Facts**  | Source des données produit                                    |
| **PySpark / Fabric**     | Extraction & transformation des données                       |
| **Power BI Desktop**     | Modélisation sémantique et visualisation                      |
| **Git**                  | Versionnage et documentation du projet                        |

---

## 📊 Fonctionnalités du tableau de bord

- Analyse des **prix moyens par catégorie de produit** (ex. biscuits, boissons, légumes)
- Suivi de la **répartition par marque**, **type de conditionnement** ou **nutriscore**
- Comparaison des prix par produit et région
- Identification des lieux les plus proche pour acheter un produit en prenant en compte les tarifs
- Filtres dynamiques par **rayon, région, ou type nutritionnel**

---
