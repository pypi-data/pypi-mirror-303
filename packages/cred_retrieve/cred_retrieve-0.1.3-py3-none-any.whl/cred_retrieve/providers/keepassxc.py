import platform
import subprocess
from ..provider import CredentialProvider

op_sys = platform.system()
if op_sys == 'Windows':
    from .keepassxc_win import get_keepassxc_path
elif op_sys == 'Darwin':
    from .keepassxc_mac import get_keepassxc_path
else:
    raise Exception('Linux is not yet implemented')

def get_id_pw(database_path: str, password: str, entry_title: str) -> list:
    """Retrieve username and password from KeePassXC."""
    try:
        # Construct the command to retrieve the password
        command = [
            get_keepassxc_path(), 'show', '-qsa', 'username',
            '-sa', 'password',
            database_path,
            entry_title
        ]

        kwargs = {
            'stdin': subprocess.PIPE,
            'stdout': subprocess.PIPE,
            'stderr': subprocess.PIPE,
            'text': True,
        }

        if op_sys == 'Windows':
            kwargs['creationflags'] = subprocess.CREATE_NO_WINDOW 

        # Start the subprocess
        process = subprocess.Popen(command, **kwargs)

        # Send the password and capture the output
        stdout, stderr = process.communicate(input=password)

        # Check if the process completed successfully
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, command, output=stdout, stderr=stderr)

        # Extract and return the username and password
        return stdout.strip().split('\n')

    except subprocess.CalledProcessError as e:
        print(e)
        print(f"An error occurred while retrieving credentials: {e.stderr}")
        return None
    except FileNotFoundError:
        print("KeePassXC CLI not found. Ensure it is installed.")
        return None


class Provider(CredentialProvider):
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_id_pw(self, db_pw: str, entry: str) -> list:
        """Get ID and password using the provided database path and entry."""
        return get_id_pw(self.db_path, db_pw, entry)
