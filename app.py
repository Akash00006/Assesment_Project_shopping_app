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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)