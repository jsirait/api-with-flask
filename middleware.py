"""Middleware file for our function"""
from flask import jsonify, request, abort

from data_service import DataService

DATA_PROVIDER = DataService()

# a list of users
people_info = [
    {'name': 'Katara', 'age': 15, 'occupation': 'water bender'},
    {'name': 'Aang', 'age': 12, 'occupation': 'Avatar'}
]


def index():
    """This is the landing page"""
    return 'Hello world'


def db():
    """This is to welcome grads"""
    return 'Hello DB Grads!'


def user_profile(id):
    """Allows argument to be passed and shown"""
    return "Profile page of user #{}".format(id)


def person():
    return jsonify(people_info)


def person_add():
    """Add a person record to our list"""
    try:
        data = request.get_json(force=True)
        name = data['name']
        age = data['age']
        occupation = data['occupation']
        if name and age and occupation:
            people_info.append({'name': name, 'age': age, 'occupation': occupation})
            return jsonify({"Person" + name: "Added successfully"})
    except Exception as exc:
        print(exc)
        abort(400)

def person_update():
    """Update information on existing user"""
    try:
        data = request.get_json(force=True)
        name = data['name']
        age = data['age']
        occupation = data['occupation']
        people_names = [p['name'] for p in people_info]
        if name and (name in people_names) and age and occupation:
            # find index of this person
            idx = 0
            while people_names[idx] != name:
                idx += 1
            people_info[idx]['age'] = age
            people_info[idx]['occupation'] = occupation
            return jsonify({"Person " + name: "Updated successfully"})
        elif name not in people_names:
            return jsonify("Person " + name + ": Not Found"), 404
    except Exception as exc:
        print(exc)
        abort(404)

def person_delete():
    """Delete an existing user from the list"""
    try:
        data = request.get_json(force=True)
        name = data['name']
        # age = data['age']
        # occupation = data['occupation']
        people_names = [p['name'] for p in people_info]
        if name and (name in people_names): # and age and occupation:
            # find index of this person
            idx = 0
            while people_names[idx] != name:
                idx += 1
            people_info.pop(idx)
            return jsonify({"Person " + name: "Deleted successfully"})
        elif name not in people_names:
            return jsonify("Person " + name + ": Not Found"), 404
    except Exception as exc:
        print(exc)
        abort(404)


# Widgets
# Get all widgets
def read_widgets():
    widgets = DATA_PROVIDER.get_widget()
    widgets_dict = {}
    for widget in widgets:
        widgets_dict[widget[0]] = {'Name': widget[1], 'Price': widget[2]}
    return jsonify(widgets_dict)


# get widget by id
def read_widget_by_id(widget_id):
    db_widget = DATA_PROVIDER.get_widget(widget_id)
    if db_widget:
        widget = {'ID': widget_id, 'Name': db_widget[1], 'Price': str(db_widget[2])}
        return jsonify(widget)
    else:
        # if widget with the specific id is not found
        abort(404)