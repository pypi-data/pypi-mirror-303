# cred\_retrieve
**cred_retrieve** is a Python package that provides a flexible way to retrieve credentials from various sources, including KeePassXC and custom credential providers. 

## Installation
```powershell
PS > pip install cred_retrieve
```

## Usage
You can easily create a credential provider and retrieve credentials using the following examples.

### Ecample 1: Using DotEnv Provider
```dotenv
# id
ID='dotenv_id'
# pw
PW='dotenv_pw'
ETC='etc_secret'
```
```python
from cred_retrieve import create_provider

cred = create_provider('dotenv')
print(cred.get_id_pw())
print(cred['ETC'])
```

### Example 2: Using KeePassXC Provider
```python
import os
from cred_retrieve import create_provider

# Set the path to your KeePassXC database file
db = os.path.join(os.getenv('PROGRAMDATA'), 'KeePassXC', 'cred.kdbx')

# Create a provider instance
cred = create_provider('keepassxc', db)

# Retrieve credentials
username, password = cred.get_id_pw('db_password', 'entry')
print(f'Username: {username}, Password: {password}')
```

### Example 3: Registering a Custom Provider
You can also create and register your own credential provider:
```python
from cred_retrieve import creators, CredentialProvider, create_provider

# Define a custom provider
class TestProvider(CredentialProvider):
    def __init__(self):
        pass

    def get_id_pw(self):
        return 'test_id', 'test_pw'

# Register the custom provider
creators().register('test', TestProvider)

# Create an instance of the custom provider
p = create_provider('test')

# Retrieve credentials from the custom provider
username, password = p.get_id_pw()
print(f'Username: {username}, Password: {password}')
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or support, please reach out to me via [GitHub Issues](https://github.com/th-yoo/cred_retrieve/issues).
