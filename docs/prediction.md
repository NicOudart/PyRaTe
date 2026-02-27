# Prédiction de labels

![En-tête prédiction](img/Header_4.png)

Maintenant que nous avons validé les performances de notre classifieur en généralisation, nous pouvons l'utiliser avec confiance pour prédire les labels de tous les pixels de notre image "raster".
**PyRaTe** permet à la fois la prédiction et l'affichage des labels prédits.

---

## Prédire avec un classifieur

Avec **PyRaTe**, pour **prédire** les labels des pixels avec le classifieur que vous avez entrainé, utilisez la commande suivante :

~~~bash
img_label,labels_code = PyRaTe.prediction(classifier_pipeline,band_list)
~~~

Il y a 2 variables de sortie : 

* `img_label` est une matrice Numpy contenant des nombres entiers, correspondant aux différents labels.

* `labels_code` est une matrice Numpy contenant les différents labels dans l'ordre des nombres entiers de `img_label`.

Ces 2 sorties, associées aux données de géoréférencement du "raster" permettent d'afficher les prédictions pour notre image.

Vous pouvez également appliquer cette fonction à de nouvelles images à classifier.

## Affichage des labels

Avec **PyRaTe**, pour afficher les **labels** prédits pour une image, avec le géoréférencement, utilisez la commande suivante :

~~~bash
PyRaTe.label_display(img_label,band_bounds,labels_code)
~~~

Voici la figure qui s'affiche alors :

![Affichage de labels prédits](img/Label_display.png)

## Pour aller plus loin ...