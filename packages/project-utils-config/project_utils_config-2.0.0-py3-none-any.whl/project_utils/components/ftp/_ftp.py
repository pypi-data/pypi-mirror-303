from typing import Optional
from paramiko import SSHClient, AutoAddPolicy, SFTPClient

from project_utils.conf import FTP


class FTPAPP:
    __config: FTP
    __sftp: SFTPClient
    __client: SSHClient

    def __init__(self, host: str = "localhost", port: str = "22", user: Optional[str] = None,
                 password: Optional[str] = None):
        self.__config = FTP(host, port, user, password)
        self.__client: SSHClient = SSHClient()
        self.__client.set_missing_host_key_policy(AutoAddPolicy)
        self.__client.connect(
            self.__config.host,
            self.__config.port,
            self.__config.user,
            self.__config.password
        )

    def __enter__(self):
        self.connect()
        return self.__sftp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False

    def connect(self):
        self.__sftp = SFTPClient.from_transport(self.__client.get_transport())
        return self.__sftp

    def close(self):
        self.__sftp.close()
        self.__client.close()
