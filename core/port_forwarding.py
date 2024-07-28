import paramiko
import threading
import socket
import logging

class PortForwarding:
    def __init__(self, ssh_client):
        self.ssh_client = ssh_client

    def dynamic_port_forwarding(self, local_port, remote_host, remote_port):
        try:
            transport = self.ssh_client.get_transport()
            transport.request_port_forward('', local_port)

            def handler(chan):
                sock = socket.socket()
                sock.connect((remote_host, remote_port))
                while True:
                    data = chan.recv(1024)
                    if not data:
                        break
                    sock.send(data)
                    response = sock.recv(1024)
                    chan.send(response)

            while True:
                chan = transport.accept(1000)
                if chan is None:
                    continue
                threading.Thread(target=handler, args=(chan,)).start()
        except Exception as e:
            logging.error(f"Failed to setup dynamic port forwarding - {str(e)}")
            raise
