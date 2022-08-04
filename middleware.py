"""Middleware file for our function"""
from flask import jsonify, request, abort

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