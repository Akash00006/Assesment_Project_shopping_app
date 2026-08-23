from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Shopping_App'

@app.route('/health')
def health():
    return 'App is running'

@app.route('/cart')
def  cart():
    return 'Cart is empty.'

passwords_db = {}


@app.route('/add', methods=['POST'])
def add_password():
    data = request.get_json()
    
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing 'username' or 'password' in request body"}), 400
    
    username = data['username']
    password = data['password']
    
    
    passwords_db[username] = password
    return jsonify({"message": f"Password saved successfully for '{username}'"}), 201


@app.route('/get/<username>', methods=['GET'])
def get_password(username):
    
    if username in passwords_db:
        return jsonify({"username": username, "password": passwords_db[username]}), 200
    
    
    return jsonify({"error": "Username not found"}), 404

@app.route('/delete/<username>', methods=['DELETE'])
def delete_password(username):
    if username in passwords_db:
        del passwords_db[username]
        return jsonify({"message": f"User '{username}' deleted successfully"}), 200
    
    return jsonify({"error": "Username not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)