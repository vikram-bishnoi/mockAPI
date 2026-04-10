from flask import Flask, send_file
import os

app = Flask(__name__)

# --- CONFIGURATION ---
FILE_NAME = "abc.csv"
FILE_SIZE_MB = 10

@app.route('/api/download/csv', methods=['GET'])
def download_csv():
    # send_file is efficient and handles headers like Content-Length
    return send_file(FILE_NAME, mimetype='text/csv', as_attachment=True)

if __name__ == '__main__':
    
    # Run on port 5000
    app.run(host='0.0.0.0', port=5000)
