import os
from typing import Tuple, Dict
from ..provider import CredentialProvider

class Provider(CredentialProvider):
    def __init__(self, env_file: str = '.env'):
        """
        Initialize the DotEnvProvider.

        Args:
            env_file (str): The path to the .env file. Default is '.env'.
        """
        self.env_file = env_file
        self.variables = self._load_env_file()

    def _load_env_file(self) -> Dict[str, str]:
        """
        Load variables from the .env file.

        Returns:
            dict: A dictionary of environment variables.
        """
        variables = {}
        try:
            with open(self.env_file) as f:
                for line in f:
                    # Strip comments and whitespace
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    key, value = line.split('=', 1)
                    variables[key.strip()] = value.strip().strip('"').strip("'")
        except FileNotFoundError:
            raise FileNotFoundError(f"The .env file '{self.env_file}' was not found.")
        return variables

    def get_id_pw(self, id='ID', pw='PW') -> Tuple[str, str]:
        """
        Retrieve username and password from the loaded variables.

        Returns:
            Tuple[str, str]: A tuple containing (username, password).

        Raises:
            KeyError: If the necessary environment variables are not found.
        """
        username = self.variables.get(id)
        password = self.variables.get(pw)
        
        if username is None or password is None:
            raise KeyError(f"Environment variables {id} and {pw} must be set in the .env file.")
        
        return username, password

    def __getitem__(self, key: str) -> str:
        """
        Retrieve a value by key.

        Args:
            key (str): The key of the variable to retrieve.

        Returns:
            str: The value associated with the key.

        Raises:
            KeyError: If the key is not found.
        """
        if key in self.variables:
            return self.variables[key]
        else:
            raise KeyError(f"'{key}' not found in the .env variables.")
