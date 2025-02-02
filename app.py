import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'}), 200

if __name__ == '__main__':
    # שימוש במשתנה סביבה PORT, או ברירת מחדל 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
