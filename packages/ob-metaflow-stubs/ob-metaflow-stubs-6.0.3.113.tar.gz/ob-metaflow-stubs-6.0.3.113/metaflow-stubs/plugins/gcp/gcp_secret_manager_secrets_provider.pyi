##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.441503                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.exception
    import abc
    import metaflow.plugins.secrets

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

class SecretsProvider(abc.ABC, metaclass=abc.ABCMeta):
    def get_secret_as_dict(self, secret_id, options = {}, role = None) -> typing.Dict[str, str]:
        """
        Retrieve the secret from secrets backend, and return a dictionary of
        environment variables.
        """
        ...
    ...

def get_credentials(scopes, *args, **kwargs):
    ...

GCP_SECRET_MANAGER_PREFIX: None

class MetaflowGcpSecretsManagerBadResponse(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the response from GCP Secrets Manager is not valid in some way
    """
    ...

class MetaflowGcpSecretsManagerDuplicateKey(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the response from GCP Secrets Manager contains duplicate keys
    """
    ...

class MetaflowGcpSecretsManagerJSONParseError(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the SecretString response from GCP Secrets Manager is not valid JSON
    """
    ...

class MetaflowGcpSecretsManagerNotJSONObject(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the SecretString response from GCP Secrets Manager is not valid JSON dictionary
    """
    ...

class GcpSecretManagerSecretsProvider(metaflow.plugins.secrets.SecretsProvider, metaclass=abc.ABCMeta):
    def get_secret_as_dict(self, secret_id, options = {}, role = None):
        """
        Reads a secret from GCP Secrets Manager and returns it as a dictionary of environment variables.
        
        If the secret contains a string payload ("SecretString"):
        - if the `json` option is True:
            Secret will be parsed as a JSON. If successfully parsed, AND the JSON contains a
            top-level object, each entry K/V in the object will also be converted to an entry in the result. V will
            always be casted to a string (if not already a string).
        - If `json` option is False (default):
            Will be returned as a single entry in the result, with the key being the last part after / in secret_id.
        
        On GCP Secrets Manager, the secret payload is a binary blob. However, by default we interpret it as UTF8 encoded
        string. To disable this, set the `binary` option to True, the binary will be base64 encoded in the result.
        
        All keys in the result are sanitized to be more valid environment variable names. This is done on a best effort
        basis. Further validation is expected to be done by the invoking @secrets decorator itself.
        
        :param secret_id: GCP Secrets Manager secret ID
        :param options: unused
        :return: dict of environment variables. All keys and values are strings.
        """
        ...
    ...

