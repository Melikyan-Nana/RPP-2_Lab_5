from flask import Blueprint, render_template
from forms import AddRegion, Delete
from tables import db, Region

bp = Blueprint('region_route', __name__)


@bp.route('/v1/region/add', methods=['POST', 'GET'])
def taxes():
    form = AddRegion()
    if form.validate_on_submit():
        code = int(form.id.data)
        name = form.name.data

        code_base = db.session.query(Region.id).filter(Region.id == code).first()
        if code_base:
            message = "Ошибка"
            return render_template('region-add.html', message=message)
        newRegion = Region()
        newRegion = Region(id=code,
                           name=name)
        db.session.add(newRegion)
        db.session.commit()
        message = "Correct username and password"
    else:
        message = "Ошибка"

    return render_template('region-add.html', message=message, form=form)


@bp.route('/v1/region/update', methods=['POST', 'GET'])
def update():
    form = AddRegion()
    if form.validate_on_submit():
        code = int(form.id.data)
        name = form.name.data
        code_base = Region.query.filter_by(id=code).all()
        if code_base is None:
            message = 'Регион не заполнен'
            return render_template('region-update.html', message=message)
        update = Region.query.filter(Region.id == code).first()
        if update:
            update.id = code
            update.name = name
            db.session.commit()
            message = 'Обновлено'
    else:
        message = "Ошибка"
    return render_template('region-update.html', message=message, form=form)


@bp.route('/v1/region/delete', methods=['POST', 'GET'])
def delete():
    form = Delete()
    if form.validate_on_submit():
        code = int(form.id.data)
        print(code)
        code_base = db.session.query(Region.id, Region.name).filter(Region.id == code).all()
        if code_base is None:
            message = 'Ошибка'
            return render_template('region-delete.html', message=message)
        city = Region.query.filter(Region.id == code).first()
        db.session.delete(city)
        db.session.commit()
        message = 'Успешно'
    else:
        message = "Ошибка"
    return render_template('region-delete.html', message=message, form=form)


@bp.route('/v1/web/region', methods=['GET'])
def getall():
    code_base = db.session.query(Region.name).all()
    return render_template('region-list.html', code_base=code_base)
