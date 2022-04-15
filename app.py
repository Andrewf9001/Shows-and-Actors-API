from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
import os

app = Flask(__name__)
heroku = Heroku(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

CORS(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class ShowsAndActors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actor_name = db.Column(db.String(50))
    character_name = db.Column(db.String(50), unique=False)
    show = db.Column(db.String(150), unique=False)
    year_released = db.Column(db.Integer, unique=False)

    def __init__(self, actor_name, character_name, show, year_released):
        self.actor_name = actor_name
        self.character_name = character_name
        self.show = show
        self.year_released = year_released


class ShowsAndActorsSchema(ma.Schema):
    class Meta:
        fields = ('actor_name', 'character_name', 'show', 'year_released')


show_schema = ShowsAndActorsSchema()
shows_schema = ShowsAndActorsSchema(many=True)

@app.route("/shows-and-actors", methods=["POST"])
def add_show_and_actor():
    actor_name = request.json['actor_name']
    character_name = request.json['character_name']
    show = request.json['show']
    year_released = request.json['year_released']

    new_show_actor = ShowsAndActors(actor_name, character_name, show, year_released)

    db.session.add(new_show_actor)
    db.session.commit()

    show_actor = ShowsAndActors.query.get(new_show_actor.id)

    return show_schema.jsonify(show_actor)


@app.route("/view-all-shows-and-actors", methods=["GET"])
def get_all_shows_and_actors():
    all_results = ShowsAndActors.query.all()
    result = shows_schema.dump(all_results)
    return jsonify(result)


@app.route("/view-single-show-and-actor/<id>", methods=["GET"])
def get_single_show_and_actor(id):
    result = ShowsAndActors.query.get(id)
    return show_schema.jsonify(result)


@app.route("/update-show-and-actor/<id>", methods=["PUT"])
def update_show_and_actor(id):
    show_actor = ShowsAndActors.query.get(id)

    actor_name = request.json['actor_name']
    character_name = request.json['character_name']
    show = request.json['show']
    year_released = request.json['year_released']

    show_actor.actor_name = actor_name
    show_actor.character_name = character_name
    show_actor.show = show
    show_actor.year_released = year_released

    db.session.commit()
    return show_schema.jsonify(show_actor)


@app.route("/delete-show-and-actor/<id>", methods=["DELETE"])
def delete_show_and_actor(id):
    show_actor = ShowsAndActors.query.get(id)
    db.session.delete(show_actor)
    db.session.commit()

    return "Actor and Show successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)