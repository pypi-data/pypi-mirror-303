##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.0);ob(v1)                               #
# Generated on 2024-10-21T18:58:32.975075                                        #
##################################################################################

from __future__ import annotations

import typing

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

CURRENT_PERIMETER_KEY: str

CURRENT_PERIMETER_URL: str

CURRENT_PERIMETER_URL_LEGACY_KEY: str

def get_perimeter_config_url_if_set_in_ob_config() -> typing.Optional[str]:
    ...

