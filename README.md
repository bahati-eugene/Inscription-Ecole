Application d'Inscription Scolaire – Flask & MongoDB

Cette application web permet de gérer l’inscription des élèves dans un établissement scolaire.
Elle a été développée en utilisant le framework Flask (Python) et la base de données non relationnelle MongoDB.

L’application permet d’effectuer les opérations CRUD (Create, Read, Update, Delete) sur les informations des élèves.

Objectifs du projet

Ce projet a été réalisé dans le cadre du cours de Base de Données Non Relationnelle.

Les objectifs sont :

Comprendre le fonctionnement de MongoDB

Créer une application web avec Flask

Implémenter les opérations CRUD

Connecter une application à une base de données MongoDB

Créer une interface utilisateur avec HTML et CSS

Technologies utilisées

Python 3

Flask

MongoDB

PyMongo

HTML

CSS

Installation
1. Installer Python

Télécharger Python depuis :
https://www.python.org

2. Installer MongoDB

Télécharger MongoDB depuis :
https://www.mongodb.com

Démarrer MongoDB service.

3. Créer un environnement virtuel
python -m venv venv

Activer :

venv\Scripts\activate
4. Installer les dépendances
pip install flask pymongo
Lancer l'application

Dans le dossier du projet :

python app.py

Puis ouvrir le navigateur :

http://127.0.0.1:5000
Fonctionnalités

L'application permet :

Ajouter un élève

Afficher la liste des élèves

Modifier les informations d’un élève

Supprimer un élève

Structure des données MongoDB

Base de données : ecole
Collection : eleves

Exemple document :

{
  nom: "Kabasele",
  postnom: "David",
  prenom: "Junior",
  classe: "5eme",
  section: "Scientifique",
  telephone: "0999999999",
  frais_inscription: "Payé"
}
Opérations CRUD
Opération	Description
Create	Ajouter un élève
Read	Afficher les élèves
Update	Modifier un élève
Delete	Supprimer un élève
Auteur

Nom : Kabasele David
Cours : Base de Données Non Relationnelle
Projet : Application d'inscription scolaire
Année : 2026

Conclusion

Cette application démontre l'utilisation de MongoDB avec Flask pour créer une application web complète implémentant les opérations CRUD avec une base de données non relationnelle.
