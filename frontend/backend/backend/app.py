from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np  # Import necessário para lidar com NaN

app = Flask(__name__)
CORS(app)

# Carrega o CSV
df = pd.read_csv('data/operadoras.csv', sep=';', encoding='utf-8')

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '').lower()
    if not termo:
        return jsonify([])

    # Filtra os resultados
    resultados = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(termo).any(), axis=1)]

    # Substitui valores NaN por strings vazias para evitar erro de JSON
    resultados = resultados.replace({np.nan: ""})

    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)


    