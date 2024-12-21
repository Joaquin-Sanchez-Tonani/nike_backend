from flask import Flask, request, jsonify
from database import get_db_connection
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=["http://localhost:5173", "https://732693c135089d87863b6a61a906720c.serveo.net/"])
@app.route('/categories', methods=['POST'])
def categories():
    try:
        # Connection to the database
        db = get_db_connection()
        cursor = db.cursor()

        # QUERY
        query = 'SELECT * FROM categories'
        cursor.execute(query)
        result = cursor.fetchall()

        # Close database
        db.close()
        cursor.close()

        return jsonify(result)
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Something went wrong"}), 500

@app.route('/products', methods=['POST'])
def products():
    try:
        # Connection to the database
        db = get_db_connection()
        cursor = db.cursor()

        # QUERY
        query = 'SELECT * FROM products'
        cursor.execute(query)
        result = cursor.fetchall()

        # Close database
        db.close()
        cursor.close()

        return jsonify(result)
    except Exception as e:
        return jsonify("Error:", e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)