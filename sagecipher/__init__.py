#import pkg_resources

from sagecipher.cipher import Cipher, SshAgentKeyError

# pkg_resources disabled to work with pyinstaller
__version__ = "0.7.5" #pkg_resources.get_distribution("sagecipher").version

__all__ = [Cipher, SshAgentKeyError, __version__]
