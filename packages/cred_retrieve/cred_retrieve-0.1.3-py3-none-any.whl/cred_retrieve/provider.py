from abc import ABC

class CredentialProvider(ABC):
    def get_id_pw(self, *args, **kwargs):
        """Retrieve user ID and password."""
        raise NotImplementedError("get_id_pw is not implemented")

    def __getitem__(self, key: str):
        """Retrieve a value by key."""
        raise NotImplementedError("__getitem__ is not implemented")
