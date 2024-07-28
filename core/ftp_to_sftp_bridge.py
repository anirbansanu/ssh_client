from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import paramiko
import logging

class FTPtoSFTPBridge:
    def __init__(self, ftp_host, ftp_port, ftp_user, ftp_pass, sftp_host, sftp_port, sftp_user, sftp_pass):
        self.ftp_host = ftp_host
        self.ftp_port = ftp_port
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass
        self.sftp_host = sftp_host
        self.sftp_port = sftp_port
        self.sftp_user = sftp_user
        self.sftp_pass = sftp_pass

    class SFTPBridgeHandler(FTPHandler):
        def on_connect(self):
            try:
                self.sftp_client = self.connect_sftp()
            except Exception as e:
                logging.error(f"Failed to connect to SFTP server - {str(e)}")

        def on_disconnect(self):
            if self.sftp_client:
                self.sftp_client.close()

        def connect_sftp(self):
            transport = paramiko.Transport((self.server.bridge.sftp_host, self.server.bridge.sftp_port))
            transport.connect(username=self.server.bridge.sftp_user, password=self.server.bridge.sftp_pass)
            return paramiko.SFTPClient.from_transport(transport)

    def start_bridge(self):
        try:
            authorizer = DummyAuthorizer()
            authorizer.add_user(self.ftp_user, self.ftp_pass, '/home/nobody', perm='elradfmw')

            handler = self.SFTPBridgeHandler
            handler.authorizer = authorizer
            handler.server.bridge = self

            server = FTPServer((self.ftp_host, self.ftp_port), handler)
            server.serve_forever()
        except Exception as e:
            logging.error(f"Failed to start FTP to SFTP bridge - {str(e)}")
            raise
