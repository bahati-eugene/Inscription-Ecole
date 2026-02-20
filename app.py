from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Connexion MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecole"]

eleves = db["eleves"]


# READ : afficher eleves

@app.route("/")
def index():

    liste_eleves = eleves.find()

    return render_template("index.html", eleves=liste_eleves)



# CREATE : ajouter eleve

@app.route("/add_eleve", methods=["POST"])
def add_eleve():

    eleve = {

        "nom": request.form["nom"],
        "postnom": request.form["postnom"],
        "prenom": request.form["prenom"],
        "date_naissance": request.form["date_naissance"],
        "nom_pere": request.form["nom_pere"],
        "nom_mere": request.form["nom_mere"],
        "telephone": request.form["telephone"],
        "classe": request.form["classe"],
        "section": request.form["section"],
        "frais_inscription": request.form["frais"]

    }

    eleves.insert_one(eleve)

    return redirect("/")



# DELETE : supprimer eleve

@app.route("/delete/<id>")
def delete(id):

    eleves.delete_one({"_id": ObjectId(id)})

    return redirect("/")



# PAGE UPDATE FORM

@app.route("/edit/<id>")
def edit(id):

    eleve = eleves.find_one({"_id": ObjectId(id)})

    return render_template("edit.html", eleve=eleve)



# UPDATE : modifier eleve

@app.route("/update/<id>", methods=["POST"])
def update(id):

    eleves.update_one(

        {"_id": ObjectId(id)},

        {"$set": {

            "nom": request.form["nom"],
            "postnom": request.form["postnom"],
            "prenom": request.form["prenom"],
            "date_naissance": request.form["date_naissance"],
            "nom_pere": request.form["nom_pere"],
            "nom_mere": request.form["nom_mere"],
            "telephone": request.form["telephone"],
            "classe": request.form["classe"],
            "section": request.form["section"],
            "frais_inscription": request.form["frais"]

        }}

    )

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)