from flask import Flask, send_file
import os

app = Flask(__name__)

# --- CONFIGURATION ---
FILE_NAME = "mock_data_10MB.csv"
FILE_SIZE_MB = 10

def create_dummy_csv():
    """Generates a CSV file of approximately 10MB if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        print(f"Generating {FILE_SIZE_MB}MB mock CSV...")
        with open(FILE_NAME, "wb") as f:
            # Writing roughly 10 million bytes of dummy CSV data
            # Header
            f.write(b"product_sku,mirakl_product_id,status\n")
            # Fill with dummy rows (~100 bytes per row)
            row = b"SKU123456789,MID987654321,VALID\n"
            for _ in range((FILE_SIZE_MB * 1024 * 1024) // len(row)):
                f.write(row)
        print("File generated.")

@app.route('/api/download/csv', methods=['GET'])
def download_csv():
    # send_file is efficient and handles headers like Content-Length
    return send_file(FILE_NAME, mimetype='text/csv', as_attachment=True)

if __name__ == '__main__':
    create_dummy_csv()
    # Run on port 5000
    app.run(host='0.0.0.0', port=5000)
