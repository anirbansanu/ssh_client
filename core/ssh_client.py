import paramiko
import pyte
import logging

class SSHClient:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.client = None

    def connect(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.hostname, self.port, self.username, self.password)
        except Exception as e:
            logging.error(f"Failed to connect to {self.hostname}:{self.port} - {str(e)}")
            raise

    def execute_command(self, command):
        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            return stdout.read().decode('utf-8')
        except Exception as e:
            logging.error(f"Failed to execute command {command} - {str(e)}")
            raise

    def emulate_terminal(self):
        try:
            channel = self.client.invoke_shell()
            screen = pyte.Screen(80, 24)
            stream = pyte.Stream(screen)
            while True:
                data = channel.recv(1024)
                if not data:
                    break
                stream.feed(data.decode('utf-8'))
                print(screen.display)
        except Exception as e:
            logging.error(f"Failed to emulate terminal - {str(e)}")
            raise

    def close(self):
        if self.client:
            self.client.close()
