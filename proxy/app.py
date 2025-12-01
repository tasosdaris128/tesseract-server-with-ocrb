from flask import Flask, request, jsonify
import requests
import json
import re


app = Flask(__name__)


# Replace with the actual URL of the other service
TARGET_SERVICE_URL = "http://tserver:8884/tesseract"


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"})


@app.route('/tesseract', methods=['POST'])
def tesseract():
    # Get the 'options' field
    options_str = request.form.get('options')
    if not options_str:
        return jsonify({"error": "Missing 'options'"}), 400

    try:
        options = json.loads(options_str)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON in 'options'"}), 400

    # Get the uploaded file
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "Missing file"}), 400

    # Prepare the payload for the other service
    files = {'file': (file.filename, file.stream, file.mimetype)}
    data = {'options': json.dumps(options)}  # Send options as JSON string

    # Forward request to the other service
    try:
        response = requests.post(TARGET_SERVICE_URL, files=files, data=data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

    # Parse the service response
    try:
        service_response = response.json()
        stderr = service_response.get("data", {}).get("stderr", "")
        stdout = service_response.get("data", {}).get("stdout", "")

        # Split stdout into lines, strip whitespace, and remove empty lines
        results = [line.strip() for line in re.split(r'[\n\f]+', stdout) if line.strip()]

        return jsonify({
            "errorMessage": stderr,
            "results": results
        })
    except (ValueError, AttributeError) as e:
        return jsonify({"error": "Invalid response from service", "details": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
