from flask import Flask, render_template, request, jsonify

#la funcion render_template me permite retornar un HTML
#la funcion request nos permite saber por cual metiodo estoy accediendo a esa ruta o endpoint
#la funcion jsonify  permite devolver una respuesta al usuario en formato json


app = Flask(__name__)
#Hace referencia al mismo documento que estoy ejecutando
#luego mando a ejecutar nuestra aplicacion

todos = []

@app.route("/",methods=['GET'])
def main():
    return render_template('index.html')

@app.route("/todos", methods=['GET', 'POST'])
def get_todos():
    if request.method == 'GET':
        return jsonify(todos), 200
    if request.method == 'POST':
        data = request.get_json()
        
        label = data["label"] if data ["label"] else None
        if not label : return jsonify ({"msg": "Label is required"}), 400

        return jsonify(data)

@app.route("/todos/<int:id>", methods=['PUT'])
def put_todos(id = None):
    if request.method == ['PUT']:
        if id is not None:
            return jsonify({"success":"updated"})
        else:
            return jsonify({"msg":"id is required"}), 400



if __name__ == "__main__":
    app.run(debug=True)

