from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Esto permite que Next.js se conecte

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({"message": "¡Hola desde Flask!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)