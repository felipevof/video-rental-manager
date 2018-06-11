from flask import render_template, abort, url_for, redirect, request


def build_context(additional_fields=None):
    base = dict()

    # define global fields
    # base['current_year'] = date.today().year

    if additional_fields:
        base.update(additional_fields)

    return base


def list_response(model, session, template):
    q = request.args.get('q', None)
    if q:
        query = model.filter_by_str(session, q)
    else:
        query = session.query(model)

    objects = query.all()
    
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


def creation_response(model, form, session, mapping_function, template, redirect_state):
    form = form(request.form)

    if request.method == 'POST' and form.validate():
        obj = model()

        mapping_function(form, obj)

        session.add(obj)
        session.commit()

        return redirect(url_for(redirect_state))

    return render_template(template, form=form)


def edit_response(model, obj_id, form, session, mapping_function, template, redirect_state):
    obj = session.query(model).filter(model.id==obj_id).first()
    form = form(request.form, obj)

    if request.method == 'POST' and form.validate():
        mapping_function(form, obj)

        session.add(obj)
        session.commit()

        return redirect(url_for(redirect_state))

    return render_template(template, form=form)
