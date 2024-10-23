##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.422289                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.decorators

class ResourcesDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    """
    Specifies the resources needed when executing this step.
    
    Use `@resources` to specify the resource requirements
    independently of the specific compute layer (`@batch`, `@kubernetes`).
    
    You can choose the compute layer on the command line by executing e.g.
    ```
    python myflow.py run --with batch
    ```
    or
    ```
    python myflow.py run --with kubernetes
    ```
    which executes the flow on the desired system using the
    requirements specified in `@resources`.
    
    Parameters
    ----------
    cpu : int, default 1
        Number of CPUs required for this step.
    gpu : int, default 0
        Number of GPUs required for this step.
    disk : int, optional, default None
        Disk size (in MB) required for this step. Only applies on Kubernetes.
    memory : int, default 4096
        Memory size (in MB) required for this step.
    shared_memory : int, optional, default None
        The value for the size (in MiB) of the /dev/shm volume for this step.
        This parameter maps to the `--shm-size` option in Docker.
    """
    ...

