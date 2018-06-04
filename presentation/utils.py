from flask import render_template


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
