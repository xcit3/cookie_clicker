#importing all necessary libraries/functions
from flask import Flask, redirect, render_template, request, session, flash, make_response, url_for, jsonify
from sqlalchemy import create_engine, text
from functools import wraps
import random
from random import shuffle
from hashlib import sha256
import time

#initialising web app
app = Flask(__name__)
app.secret_key = 'CvnRdyzG01qRT6PCS0ei0sZADfTWvQ6oWhUtWKbVArfySfRtlTDQZSW3iPqN4af6mk5iWH2UqUB8sLbfwMGWOqEVxvjCBJRv'
app.static_folder = 'static'

#Initialising sessions - persistent user data
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



class Player:
    def __init__(self):
        self.cps = 0
    def buy_building(building):
        self.cps += building.cps



class Building():
    def __init__(self, name, cost, cps):
        self.name = name
        self.bought = 0
        self.cost = cost
        self.cps = cps
    def buy(self):
        self.cost = round(self.cost*1.15, 1)
        self.bought += 1




class Upgrade():
    def __init__(self, name, cost, building, unlock):
        self.name = name
        self.cost = cost
        self.building = building
    def buy(self, buildings):
        buildings[self.building].cps *= multiplier

class Multiplier(Upgrade):
    def __init__(self, name, cost, building, unlock, multiplier):
        super().__init__(name, cost, building, unlock)
        self.multiplier = multiplier





buildings = {}
buildings['Cursor'] = Building('Cursor', 10, 0.1)
buildings['Grandma'] = Building('Grandma', 100, 1)
buildings['Farm'] = Building('Farm', 1100, 8)
buildings['Mine'] = Building('Mine', 12000, 47)
buildings['Factory'] = Building('factory', 130000, 260)
buildings['Bank'] = Building('Bank', 1400000, 1400)
buildings['Temple'] = Building('Temple', 20000000, 7800)
buildings['Wizard Tower'] = Building('Wizard Tower', 330000000, 44000)
buildings['Shipment'] = Building('Shipment', 5100000000, 260000)


multipliers = {}
multipliers['Reinforced index finger'] = Multiplier('Reinforced index finger', 100, 'Cursor', 1, 2)
multipliers['Carpal tunnel prevention cream'] = Multiplier('Carpal tunnel prevention cream', 500, 'Cursor', 1, 2)
multipliers['Ambidextrous'] = Multiplier('Ambidextrous', 10000, 'Cursor', 10, 2)

upgrades = {}


@app.route('/')
def home():
    return render_template('home.html', buildings=list(buildings.values()), multipliers=list(multipliers.values()))


@app.route('/buy', methods=["POST"])
def buy():
    building = request.form.get('building')
    building = buildings[building]
    building.buy()
    message = {"cost":building.cost, 'bought':building.bought}
    return jsonify(message)

@app.route('/buymulti', methods=['POST'])
def buymulti():
    return 'a'



if __name__ == "__main__":
    app.run(debug=True)




