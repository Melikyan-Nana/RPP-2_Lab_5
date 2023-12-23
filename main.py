from flask import Flask
from tables import db

from routes.region_routes import bp as region_route_bp
from routes.tax_param_route import tax
from routes.tax_route import calc


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/rpp_lab_5'
db.init_app(app)

app.register_blueprint(region_route_bp)
app.register_blueprint(tax)
app.register_blueprint(calc)

if __name__ == "__main__":
    app.run(debug=True)
