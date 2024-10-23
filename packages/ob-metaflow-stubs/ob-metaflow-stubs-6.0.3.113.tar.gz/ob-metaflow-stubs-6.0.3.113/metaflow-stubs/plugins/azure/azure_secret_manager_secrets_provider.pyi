##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.464455                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.exception
    import abc
    import metaflow.plugins.secrets

class SecretsProvider(abc.ABC, metaclass=abc.ABCMeta):
    def get_secret_as_dict(self, secret_id, options = {}, role = None) -> typing.Dict[str, str]:
        """
        Retrieve the secret from secrets backend, and return a dictionary of
        environment variables.
        """
        ...
    ...

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

AZURE_KEY_VAULT_PREFIX: None

def create_cacheable_azure_credential():
    ...

class MetaflowAzureKeyVaultBadVault(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the secretid is fully qualified but does not have the right key vault domain
    """
    ...

class MetaflowAzureKeyVaultBadSecretType(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the secret type is anything except secrets
    """
    ...

class MetaflowAzureKeyVaultBadSecretPath(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the secret path does not match to expected length
    """
    ...

class MetaflowAzureKeyVaultBadSecretName(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the secret name does not match expected pattern
    """
    ...

class MetaflowAzureKeyVaultBadSecretVersion(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the secret version does not match expected pattern
    """
    ...

class MetaflowAzureKeyVaultBadSecret(metaflow.exception.MetaflowException, metaclass=type):
    """
    Raised when the secret does not match supported patterns in Metaflow
    """
    ...

class AzureKeyVaultSecretsProvider(metaflow.plugins.secrets.SecretsProvider, metaclass=abc.ABCMeta):
    def get_secret_as_dict(self, secret_id, options = {}, role = None):
        ...
    ...

