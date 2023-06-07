from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ
from prometheus_flask_exporter import PrometheusMetrics
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")
# Cofigure the connection with a database
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URL')
# Give sqlalchemy away to handle our app
db = SQLAlchemy(app)

class Beer(db.Model):
    __tablename__ = "beers"

    id = db.Column(db.Integer, primary_key=True)
    beer_id = db.Column(db.Integer)
    name = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float(10), nullable=False)
    alcohol_percentage = db.Column(db.Float(5), nullable=True)

    def json(self):
        return {'id': id, "beer_id": self.beer_id, "name": self.name, "price": self.price, "alcohol_percentage": self.alcohol_percentage}

@app.route('/test', methods=["GET"])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)

@app.route('/beer/<beer_id>', methods=['GET'])
def get_beer(beer_id):
        beer = Beer.query.filter_by(beer_id=beer_id).first()

        if beer:
            return make_response(jsonify({
                '1.beer_id': beer.beer_id, 
                '2.name': beer.name,
                '3.price': beer.price,
                '4.alcoholPercentage': beer.alcohol_percentage
            }))
        else:
            return make_response(jsonify({'error': 'Beer not found'})), 404
        
@app.route('/beer', methods=['POST'])
def search_beer():
    # Get the search parameters from the request payload
    data = request.get_json()

    name = data.get('name', '')
    price_from = data.get('priceFrom', '')
    price_to = data.get('priceTo', '')
    alcohol_from = data.get('alcoholPercentageFrom', '')
    alcohol_to = data.get('alcoholPercentageTo', '')

    filtered_beers = Beer.query.filter(
        Beer.name.ilike(f'%{name}%'),
        Beer.price.between(price_from, price_to),
        Beer.alcohol_percentage.between(alcohol_from, alcohol_to)
    ).all()

    response = []
    for beer in filtered_beers:
        response.append({
            '1.beer_id': beer.beer_id,
            '2.name': beer.name,
            '3.price': beer.price,
            '4.alcoholPercentage': beer.alcohol_percentage
        })
    return jsonify(response)

@app.route('/health', methods=['GET'])
def check_health():
    try:
        db.session.execute("SELECT 1")
        return jsonify({'status': 'Database connection is healthy'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/beer/<beer_id>', methods=['DELETE'])
def delete_beer(beer_id):
    beer = Beer.query.filter_by(beer_id=beer_id).first()

    if beer:
        deleted_beer_name = beer.name  # Store the name of the beer before deleting
        db.session.delete(beer)
        db.session.commit()
        return make_response(jsonify({'Deleted beer': f'{deleted_beer_name} deleted'}), 200)
    else:
        return make_response(jsonify({'error': 'Beer not found'}), 404)

import traceback

@app.route('/add-beer', methods=['POST'])
def add_beer():
    # Get the data from the request payload
    data = request.get_json()

    # Extract the beer details from the payload
    id = data.get("id")
    beer_id = data.get('beer_id')
    name = data.get('name')
    price = data.get('price')
    alcohol_percentage = data.get('alcohol_percentage')

    # Check if the beer already exists in the database
    existing_beer = Beer.query.filter((Beer.id == id) | (Beer.beer_id == beer_id)).first()
    if existing_beer:
        return jsonify({'message': 'Beer already exists with this id or beer_id'})

    # Create a new Beer instance
    new_beer = Beer(id=id, beer_id=beer_id, name=name, price=price, alcohol_percentage=alcohol_percentage)

    try:
        # Add the new beer to the database
        db.session.add(new_beer)
        db.session.commit()
        return jsonify({'message': 'Beer added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)

