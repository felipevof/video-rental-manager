from flask import render_template, abort, url_for, redirect


def build_context(additional_fields=None):
    base = dict()

    # define global fields
    # base['current_year'] = date.today().year

    if additional_fields:
        base.update(additional_fields)

    return base


def list_response(model, session, template):
    objects = session.query(model).all()
    return render_template(template, **build_context({'objects': objects}))


def details_response(model, obj_id, session, template):
    obj = session.query(model).filter(model.id==obj_id).first()
    if obj:
        return render_template(template, **build_context({'obj': obj}))
    else:
        abort(404)


def delete_response(model, obj_id, session):
    obj = session.query(model).filter(model.id==obj_id).first()

    if obj:
        session.delete(obj)
        session.commit()
        return ""
    else:
        abort(404)
