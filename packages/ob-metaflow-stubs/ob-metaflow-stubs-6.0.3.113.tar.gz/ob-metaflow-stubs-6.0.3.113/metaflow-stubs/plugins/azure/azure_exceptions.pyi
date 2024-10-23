##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.463294                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

class MetaflowAzureAuthenticationError(metaflow.exception.MetaflowException, metaclass=type):
    ...

class MetaflowAzureResourceError(metaflow.exception.MetaflowException, metaclass=type):
    ...

class MetaflowAzurePackageError(metaflow.exception.MetaflowException, metaclass=type):
    ...

