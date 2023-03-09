from flask import Flask, jsonify

app = Flask(__name__)

from listanegra import DBblacklist

@app.route('/listar')
def getlista():
    return jsonify(DBblacklist)

"""@app.route('/listar/<string:dom_prov>')
def getproveedor():
    prov_encontrado = [x for x in DBblacklist if x[]]"""

if __name__ == '__main__':
    app.run(debug=True, port=4000)