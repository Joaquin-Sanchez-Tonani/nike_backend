from flask import Flask, request, jsonify
from database import get_db_connection
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Ajusta los orígenes según tu necesidad

def execute_query(query):
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result
    except Exception as e:
        print("Database error:", e)
        raise

@app.route('/categories', methods=['POST'])
def categories():
    try:
        query = 'SELECT * FROM categories'
        result = execute_query(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

@app.route('/products', methods=['POST'])
def products():
    try:
        query = 'SELECT * FROM products'
        result = execute_query(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "Something went wrong", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
