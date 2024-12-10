from flask import Flask

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name')
    if name:
        return jsonify({"message": f"Hello world, {name}"})
    else:
        return jsonify({"error": "Please specify a name in the 'name' query parameter. "}), 400
