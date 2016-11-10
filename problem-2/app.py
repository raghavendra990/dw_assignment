#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request
import redis

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/add_key/', methods=['POST'])
def add_key():
    if not request.json or not 'key' in request.json:
        abort(400)
    r = redis.StrictRedis()
    r.set(request.json['key'] , request.json['value'])

    return jsonify({request.json['key'] : request.json['value']}), 201


@app.route('/get_key/' , methods=['POST'])
def get_key():
    if not request.json or not 'key' in request.json:
        abort(400)
    r = redis.StrictRedis()
    value = r.get(request.json['key'])

    if value  is None  :
        return jsonify({"error":"value does not exist"}), 201

    return jsonify({request.json['key'] : value}), 201

@app.route('/delete_key/' , methods=['POST'])
def delete_key():
    if not request.json or not 'key' in request.json:
        abort(400)
    r = redis.StrictRedis()
    value = r.delete(request.json['key'])

    if value  == 0  :
        return jsonify({"error":"value does not exist"}), 201

    return jsonify({"message" : "succesfully deleted key: %s"%(request.json['key'])}), 201

if __name__ == '__main__':
    app.run(debug=True)

