from flask import render_template, Blueprint, jsonify


@get_pm10_blueprint.route('/chart/<site><int:days>')
def get_pm10(ab):
    d = make_dict(ab)
    return jsonify(d)
