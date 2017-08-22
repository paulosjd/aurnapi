from flask import Blueprint, jsonify

#db sessionmaker ??

@sites_blueprint.route('/chart/<site><int:days>')
def get_pm10(ab):
    d = make_dict(ab)
    return jsonify(d)
