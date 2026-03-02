"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_family_members():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200

@app.route('/members/<int:member_id>', methods=['GET'])
def get_a_single_member(member_id):
    # This is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
  
    return jsonify({"msg": "Familiar no encontrado"}), 404


# This is how you can use the Family datastructure by calling its methods
@app.route('/members', methods=['POST'])
def add_family_member():
    new_member = request.json
    if not new_member:
        return jsonify({"msg":"Los campos están incompletos"}), 400
    
    jackson_family.add_member(new_member)
    return jsonify({"msg": f"{new_member['first_name']} ha sido añadido a la familia"}), 200



 # This is how you can use the Family datastructure by calling its methods
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    erase_member=jackson_family.delete_member(member_id)
    if erase_member:
        return jsonify({"done": True, "msg": f"El familiar con el id {member_id} ha sido eliminado"}), 200
    return jsonify({"msg":"No se pudo eliminar al familiar"}), 404



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
