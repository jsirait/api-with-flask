from middleware import db, index, user_profile, person, person_add, person_update, person_delete
from middleware import read_widgets, read_widget_by_id
from flask import jsonify


def initialize_routes(app):
    if app:
        app.add_url_rule('/api/db/', 'db', db)
        app.add_url_rule('/api/hello/', 'index', index)
        app.add_url_rule('/api/profile/<id>', 'user_profile', user_profile, methods=['GET'])
        app.add_url_rule('/api/person', 'person', person, methods=['GET'])
        app.add_url_rule('/api/person', 'person_add', person_add, methods=['POST'])
        app.add_url_rule('/api/person', 'person_update', person_update, methods=['PUT'])
        app.add_url_rule('/api/person', 'person_delete', person_delete, methods=['DELETE'])
        app.add_url_rule('/api', 'list_routes', list_routes, methods=['GET'], defaults={'app': app})
        # widget rules
        app.add_url_rule('/api/widgets', 'read_widgets', read_widgets, methods=['GET'])
        app.add_url_rule('/api/widgets/<int:widget_id>', 'widget_by_id', read_widget_by_id, methods=['GET'])


def list_routes(app):
    routes = []
    """To list all available routes of our webapp"""
    for route in app.url_map.iter_rules():
        routes.append({
            'Route': str(route),
            'Endpoint': route.endpoint,
            'Methods': list(route.methods)
        })
    return jsonify({'Routes': routes, 'Total': len(routes)})


