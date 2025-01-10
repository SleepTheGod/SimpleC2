from flask import Flask, render_template, jsonify, request
import os
import time
from werkzeug.utils import secure_filename
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Configuration for file uploads (change as needed)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    # Serve the index.html file from the 'templates' directory
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def get_status():
    # Example: Return system status or server info
    status = {
        'status': 'Running',
        'uptime': time.time() - os.path.getctime('/proc/1/stat'),
        'hostname': os.uname().nodename
    }
    return jsonify(status)

@app.route('/screenshot', methods=['GET'])
def take_screenshot():
    # Example: Take a screenshot (in reality, we would use something like PIL or an external service)
    screenshot = Image.new('RGB', (100, 100), color='red')  # Placeholder for actual screenshot
    img_io = BytesIO()
    screenshot.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io.getvalue(), 200, {'Content-Type': 'image/png'}

@app.route('/files', methods=['GET'])
def list_files():
    # Example: List files in a given directory (e.g., /home/user/files)
    files = os.listdir('/home/debian')
    return jsonify(files)

@app.route('/logs', methods=['GET'])
def get_logs():
    # Example: Retrieve logs (you can modify this to fetch actual logs)
    logs = ["Log entry 1", "Log entry 2", "Log entry 3"]
    return jsonify(logs)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': 'File uploaded successfully'}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    # Run the app
    app.run(host='0.0.0.0', port=5000, debug=True)
