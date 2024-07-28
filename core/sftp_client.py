import pysftp
import logging

class SFTPClient:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.sftp = None

    def connect(self):
        try:
            self.sftp = pysftp.Connection(self.hostname, username=self.username, password=self.password, port=self.port)
        except Exception as e:
            logging.error(f"Failed to connect to SFTP server {self.hostname}:{self.port} - {str(e)}")
            raise

    def upload(self, local_path, remote_path):
        try:
            self.sftp.put(local_path, remote_path)
        except Exception as e:
            logging.error(f"Failed to upload file {local_path} to {remote_path} - {str(e)}")
            raise

    def download(self, remote_path, local_path):
        try:
            self.sftp.get(remote_path, local_path)
        except Exception as e:
            logging.error(f"Failed to download file {remote_path} to {local_path} - {str(e)}")
            raise

    def close(self):
        if self.sftp:
            self.sftp.close()
