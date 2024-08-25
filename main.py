from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.json.get('data', [])
        if not data or not isinstance(data, list):
            return jsonify({"is_success": False, "error": "Invalid input"}), 400

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        highest_lowercase_alphabet = [max([char for char in alphabets if char.islower()])] if any(char.islower() for char in alphabets) else []

        response = {
            "is_success": True,
            "user_id": "pothuri_naga_sai_saketH",
            "email": "pothurisaketh@gmail.com",
            "roll_number": "21BCE7052",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == "__main__":
    app.run(debug=True)
