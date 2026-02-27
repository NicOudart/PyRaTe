# Tutoriel PyRaTe

![En-tête logo](img/Logo.png)

_Logiciel conçu pour les projets de télédétection des étudiants de l'Université de Versailles Saint-Quentin (UVSQ)_

---

## Introduction

**PyRaTe** est une bibliothèque Python conçue pour vous aider lors de vos projets de "télédétection".

Il s'agit un package de fonctions vous permettant d'entrainer un classifieur à identifier les pixels dans une image satellite "raster" multi-bande : un problème classique en télédétection.

Elle contient des fonctions pour :

* L'**importation** des différentes bandes d'une image satellite au format **GeoTIFF**.

* Un **affichage RGB** géoréférencé à partir de 3 bandes d'une image satellite.

* **Labéliser** des pixels d'une image donnée, pour constituer une base de données d'entrainement sous la forme d'un DataFrame Pandas.

* Afficher la **distribution des pixels** d'une base de données (par bande et par label).

* **Entrainer un classifieur** à identifier les pixels dans une image satellite.

* **Tester les performances** d'un classifieur sur des pixels autres que ceux des données d'entrainement.

* Afficher les **labels prédits** pour les pixels d'une image, avec géoréférencement.

Vous trouverez sur ce site web un **tutoriel** pour prendre en main **PyRaTe**, sur un exemple d'image satellite "raster" multi-bande.

## Installation

Téléchargez la dernière version de **PyRaTe** sa page GitHub, dans l'onglet "Releases" :

[Lien vers PyRaTe](https://github.com/NicOudart/PyRaTe)

Enregistrez le dossier téléchargé (et dézippé) sur votre ordinateur.

Pour installer **PyRaTe**, récupérez le chemin où vous l'avez enregistrée sur votre ordinateur "path/PyRaTe" et utilisez la commande Python :

~~~bash
pip install path/PyRaTe
~~~

Une fois **PyRaTe** installée, vous pourrez l'importer sous Python avec la commande :

~~~bash
import PyRaTe
~~~

C'est bon, vous pouvez utiliser **PyRaTe** !

---

## Credits

© Nicolas OUDART

LATMOS/IPSL, UVSQ Université Paris-Saclay, Guyancourt, France