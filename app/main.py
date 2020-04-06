import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from tempfile import mkdtemp

from functions import getJSON, getHouse, getCharacter

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/characters")
def characters():
    if request.args:
        query = request.args
        character = getCharacter(query['id'])
        if 'message' not in character:
            return render_template("character.html", character=character)
    else:
        myJSON = getJSON('characters')
        return render_template("characters.html", characters=myJSON)

@app.route("/houses")
def houses():
    myJSON = getJSON('houses')
    if request.args:
        query = request.args
        if query['house'] == "Gryffindor":
            house = getHouse(myJSON[0]['_id'])[0]
            return render_template("house.html", house=house)
        elif query['house'] == "Ravenclaw":
            house = getHouse(myJSON[1]['_id'])[0]
            return render_template("house.html", house=house)
        elif query['house'] == "Hufflepuff":
            house = getHouse(myJSON[3]['_id'])[0]
            return render_template("house.html", house=house)
        elif query['house'] == "Slytherin":
            house = getHouse(myJSON[2]['_id'])[0]
            return render_template("house.html", house=house)
    else:
        return render_template("houses.html", houses=myJSON)

@app.route("/spells")
def spells():
    myJSON = getJSON('spells')
    return render_template("spells.html", spells=myJSON)