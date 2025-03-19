import os
import sys
import logging
from flask import Flask, render_template, request, jsonify
from io import StringIO

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler(sys.stdout)])

# Variable to store the latest log message
latest_log = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_code():
    global latest_log  # Use a global variable to store the latest log
    code = request.form.get('code')  # Safely retrieve 'code'
    print(request.form)
    if not code:
        return jsonify(result="Error: No code provided"), 400

    output = StringIO()
    sys.stdout = output  # Redirect stdout to capture print statements

    try:
        exec(code)  # Execute the code
        result = output.getvalue() + "Executed successfully."
        logging.info("Executed successfully.")
    except Exception as e:
        result = output.getvalue() + f"Error: {str(e)}"
        logging.error(f"Error: {e}")

    sys.stdout = sys.__stdout__  # Reset redirect.

    # Store only the latest log message
    latest_log = result
    
    return jsonify(result=latest_log)

@app.route('/save', methods=['POST'])
def save_code():
    code = request.form.get('code')  # Safely retrieve 'code'
    filename = request.form.get('filename') + '.py'  # Automatically append .py extension

    if filename and code:
        filepath = os.path.join('saved_tests', filename)
        with open(filepath, 'w') as f:
            f.write(code)
        return jsonify(result=f"{filename} saved successfully.")
    
    return jsonify(result="Filename or code is required."), 400

@app.route('/logs', methods=['GET'])
def get_logs():
    """Return the latest log message."""
    return jsonify(log=latest_log)

if __name__ == '__main__':
    if not os.path.exists('saved_tests'):
        os.makedirs('saved_tests')  # Create a directory for saved tests if it doesn't exist.
    
    app.run(debug=True)
