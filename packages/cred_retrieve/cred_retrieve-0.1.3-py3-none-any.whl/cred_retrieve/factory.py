import importlib
from typing import Callable, Dict, Type
#from .provider import CredentialProvider

class CreatorRegistry:
    """Registry for storing and retrieving credential provider creators."""

    def __init__(self) -> None:
        self._creators: Dict[str, Callable[..., 'CredentialProvider']] = {}

    def register(self, provider: str, creator: Callable[..., 'CredentialProvider']) -> None:
        """
        Register a credential provider creator.

        Args:
            provider (str): The name of the provider.
            creator (Callable[..., CredentialProvider]): A callable that creates an instance of a CredentialProvider.

        Raises:
            ValueError: If the provider name is already registered.
        """
        if provider in self._creators:
            raise ValueError(f"Provider '{provider}' is already registered.")
        self._creators[provider] = creator

    def get_creator(self, provider: str) -> Callable[..., 'CredentialProvider']:
        """
        Retrieve a registered credential provider creator.

        Args:
            provider (str): The name of the provider.

        Returns:
            Callable[..., CredentialProvider]: The creator function for the specified provider.

        Raises:
            KeyError: If the provider is not registered.
        """
        return self._creators[provider]

    def list(self) -> Dict[str, None]:
        """
        List all registered provider names.

        Returns:
            Dict[str, None]: A dictionary of registered provider names.
        """
        return self._creators.keys()

_creators: CreatorRegistry = None

def creators() -> CreatorRegistry:
    """Get the global creator registry instance."""
    global _creators
    if not _creators:
        _creators = CreatorRegistry()
    return _creators

def dynamic_import(provider_name: str) -> Type['CredentialProvider']:
    """
    Dynamically import a provider module.

    Args:
        provider_name (str): The name of the provider module.

    Returns:
        Type[CredentialProvider]: The provider class.

    Raises:
        ImportError: If the module cannot be imported.
    """
    module_name = f".providers.{provider_name}"
    module = importlib.import_module(module_name, package='cred_retrieve')
    return module.Provider  # Assuming each module has a 'Provider' class

def create_provider(provider: str, *args, **kwargs) -> Type['CredentialProvider']:
    """
    Create an instance of a credential provider.

    Args:
        provider (str): The name of the provider.
        *args: Positional arguments to pass to the provider's constructor.
        **kwargs: Keyword arguments to pass to the provider's constructor.

    Returns:
        CredentialProvider: An instance of the requested credential provider.

    Raises:
        KeyError: If the provider is not registered.
        ImportError: If the provider module cannot be imported.
    """
    if provider in creators().list():
        return creators().get_creator(provider)(*args, **kwargs)
    else:
        return dynamic_import(provider)(*args, **kwargs)

if __name__ == '__main__':
    # providers/example_provider.py
    #class Provider:
    #    def get_id_pw(self):
    #        return "example_id", "example_password"
    provider_instance = create_provider('example_provider')
    user_id, password = provider_instance.get_id_pw()
    print(f"User ID: {user_id}, Password: {password}")
