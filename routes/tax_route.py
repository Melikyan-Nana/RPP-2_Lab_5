from flask import Blueprint, render_template
from forms import Calc
from tables import db, CarTaxParam

calc = Blueprint('calc', __name__)


@calc.route('/v1/car/tax/calc', methods=['GET', 'POST'])
def calculation():
    tax = None
    form = Calc()
    if form.validate_on_submit():
        hp_base = int(form.hp_base.data)
        year = int(form.year.data)
        code = int(form.id.data)

        object_rate = db.session.query(CarTaxParam.rate).filter(CarTaxParam.from_hp_car < hp_base,
                                                                hp_base < CarTaxParam.to_hp_car,
                                                                CarTaxParam.from_production_year_car < year,
                                                                year < CarTaxParam.to_production_year_car,
                                                                CarTaxParam.id == code).first()
        rate = int(object_rate[0])
        tax = rate * hp_base
        message = tax
    else:
        message = "Ошибка"
    return render_template('index.html', message=message, form=form, tax=tax)
