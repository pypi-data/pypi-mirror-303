import tomli
import socket
import os
import base64
from . import encrypt_util


class Config:
    def __init__(self, config_path: str):
        self.data = None
        self.key_path = os.path.expanduser('~/.ssh/id_rsa')
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        with open(self.config_path, 'rb') as f:
            self.data = tomli.load(f)

        try:
            vault_path = self.get_vault_path()
            with open(vault_path, 'rb') as f:
                self.vault = tomli.load(f)
                for k, v in self.vault.items():
                    encrypted_data = base64.b64decode(v.encode())
                    decrypted_data = encrypt_util.decryt(self.key_path, encrypted_data)
                    self.vault[k] = decrypted_data.decode('ascii').strip()
            self.populate_password(self.data)
        except Exception as e:
            print(f"Error loading vault: {e}")

    def populate_password(self, config_dict: dict[str, str]):
        for k, v in config_dict.items():
            if isinstance(v, dict):
                self.populate_password(v)
                continue
            if not isinstance(v, str) or not v.startswith('map:'):
                continue
            vault_key = v.split(':')[1]
            if vault_key in self.vault:
                config_dict[k] = self.vault[vault_key]

    def get_vault_path(self):
        dirname = os.path.dirname(self.config_path)
        return os.path.join(dirname, 'vault', socket.gethostname() + '.py')

    def get_mysql_string(self, config_name: str):
        if config_name not in self.data['mysql']:
            return
        config = self.data['mysql'][config_name]
        return 'mysql+mysqldb://%s:%s@%s:%d/%s?charset=utf8' % (
        config["user"], config["password"], config["host"], config["port"], config["db"])
