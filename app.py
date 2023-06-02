from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
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
        return make_response(jsonify({'Deleted beer': f'"{deleted_beer_name}" deleted'}), 200)
    else:
        return make_response(jsonify({'error': 'Beer not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

