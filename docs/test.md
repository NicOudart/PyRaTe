# Test d'un classifieur

Nous avons un classifieur prêt à être utilisé.
Mais avant de l'appliquer à nos données d'étude, nous aimerions être sûrs qu'il performera bien sur des données qu'il n'a jamais vues.
Nous allons donc le tester avec **PyRaTe**.

---

## Problème du sur-apprentissage

En apprentissage automatique, le nerf de la guerre est la **généralisation**.

En effet, un modèle qui a d'excellente performances sur les données d'entrainement, mais de mauvaises performances sur n'importe quelles autres données **ne sert à rien**.
On veut que le modèle soit capable de **généraliser** ce qu'il a apprit.

Ceci peut arriver lorsqu'un modèle apprend **trop spécifiquement** des données d'entrainement.
C'est ce que l'on appelle le **sur-apprentissage**, et c'est la hantise de tous les "data-scientists".

## Générer une base de données de test

![Labélisation de la base de test](img/Labelling.png)

# Performances en généralisation

![Exactitude en test](img/Test_accuracy.png)

![Matrice de confusion en test](img/Confusion_matrix_test.png)
