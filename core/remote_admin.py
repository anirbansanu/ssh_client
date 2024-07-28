from flask import Flask, request, jsonify
import logging

class RemoteAdmin:
    def __init__(self, ssh_client):
        self.ssh_client = ssh_client
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/execute', methods=['POST'])
        def execute_command():
            data = request.json
            command = data['command']
            try:
                result = self.ssh_client.execute_command(command)
                return jsonify({'result': result})
            except Exception as e:
                logging.error(f"Failed to execute remote command {command} - {str(e)}")
                return jsonify({'error': str(e)}), 500

    def run(self, host='0.0.0.0', port=5000):
        self.app.run(host=host, port=port)
