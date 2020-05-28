from flask import render_template, request, url_for, redirect, send_file
from app import app
from game import Deck, Card
import random
deck = Deck()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    title= 'random'

    deck = Deck()
    

    deck.shuffle()


    card = deck.drawCard()

    return render_template('index.html', title=title, card=card)

@app.route('/card', methods=['GET', 'POST'])
def card():
    title= 'random'
    card = deck.drawCard()

    return render_template('index.html', title=title, card=card)
