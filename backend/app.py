from flask import Flask, jsonify, send_from_directory
import os
import sys


AGENT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'agent')
)
sys.path.append(AGENT_DIR)

from monitor import get_server_info

FRONTEND_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'frontend')
)

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path='')

@app.route('/api/system', methods=['GET'])
def system_metrics():
  data = get_server_info()
  return jsonify(data)

@app.route('/')
def index():
  return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
