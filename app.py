import mysql.connector
from flask import Flask, make_response, jsonify, request

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='estoque',
    port='3306'
)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Busca estoque atualizado
@app.route('/Estoque', methods=['GET'])
def get_estoque():

    my_cursor = mydb.cursor()  
    my_cursor.execute('SELECT * FROM estoque')
    produtos = my_cursor.fetchall()

    list_produtos = list()
    for produto in produtos:
        list_produtos.append(
            {
                'id': produto[0],
                'categoria': produto[1],
                'produto': produto[2],
            }
        )
    return make_response(
        jsonify(
        Mensagem="Lista de produtos",
        Dados=list_produtos
        )
    )

# Criando item no estoque
@app.route('/Estoque', methods=['POST'])
def create_estoque():
    att_estoque = request.json

    my_cursor = mydb.cursor()
    sql = f"INSERT INTO estoque (categoria, produto) VALUES ('{att_estoque['categoria']}', '{att_estoque['produto']}');"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
        Mensagem='Produto cadastrado com sucesso!',
        Produto=att_estoque)
        )

#Editar item no estoque
@app.route('/Estoque/<int:id>', methods=['PUT'])
def update_estoque(id):
    att_estoque = request.json

    my_cursor = mydb.cursor()
    sql = f"UPDATE estoque SET categoria = '{att_estoque['categoria']}', produto = '{att_estoque['produto']}' WHERE id = {id};"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
        Mensagem='Produto atualizado com sucesso!',
        Produto=id)
        )

#Deletando produtos
@app.route('/Estoque/<int:id>', methods=['DELETE'])
def delete_estoque(id):
    my_cursor = mydb.cursor()
    sql = f"DELETE FROM estoque WHERE id = {id};"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
        Mensagem='Produto deletado com sucesso!',
        Produto=id)
        )

app.run()