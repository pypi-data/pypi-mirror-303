##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.0);ob(v1)                               #
# Generated on 2024-10-21T18:58:33.026230                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.monitor

class DebugMonitor(metaflow.monitor.NullMonitor, metaclass=type):
    @classmethod
    def get_worker(cls):
        ...
    ...

class DebugMonitorSidecar(object, metaclass=type):
    def __init__(self):
        ...
    def process_message(self, msg):
        ...
    ...

