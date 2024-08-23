from flask import Flask, jsonify, make_response, request
# Importa o banco de Dados
from bd import Carros


# Instanciar o modulo Flask na nossa variavel app
app = Flask('carros')

#PRIMEIRO MÉTODO - VIZUALISAR DADOS (GET)
#app.route -> definir que essa função é uma rota para que o flask entenda que aquilo é um metodo que deve ser executado
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros 


#PRIMEIRO MÉTODO PARTE 2 - VIZUALIZAR DADOS VIA ID (GET POR ID)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)

#SEGUNDO MÉTODO - CRIAR NOVOS DADOS (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso',
                carro=carro
                )
    )

#TERCEIRO MÉTODO - EDITAR DADOS (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_dados(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])


#QUARTO MÉTODO - DELETAR DADOS (DELETE)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carros(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem:": "Carro excluido com sucesso!"})

app.run(port=5000, host="localhost")