##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.419907                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.metaflow_current
    import metaflow.decorators

UBF_CONTROL: str

CONTROL_TASK_TAG: str

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

class MetaDatum(tuple, metaclass=type):
    """
    MetaDatum(field, value, type, tags)
    """
    @staticmethod
    def __new__(_cls, field, value, type, tags):
        """
        Create new instance of MetaDatum(field, value, type, tags)
        """
        ...
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
        ...
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
        ...
    ...

current: metaflow.metaflow_current.Current

class Parallel(tuple, metaclass=type):
    """
    Parallel(main_ip, num_nodes, node_index, control_task_id)
    """
    @staticmethod
    def __new__(_cls, main_ip, num_nodes, node_index, control_task_id):
        """
        Create new instance of Parallel(main_ip, num_nodes, node_index, control_task_id)
        """
        ...
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
        ...
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
        ...
    ...

class ParallelDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    """
    MF Add To Current
    -----------------
    parallel -> metaflow.metaflow_current.Parallel
    
        @@ Returns
        -------
        Parallel
            `namedtuple` with the following fields:
                - main_ip : str
                    The IP address of the control task.
                - num_nodes : int
                    The total number of tasks created by @parallel
                - node_index : int
                    The index of the current task in all the @parallel tasks.
                - control_task_id : Optional[str]
                    The task ID of the control task. Available to all tasks.
    
    is_parallel -> bool
        True if the current step is a @parallel step.
    """
    def __init__(self, attributes = None, statically_defined = False):
        ...
    def runtime_step_cli(self, cli_args, retry_count, max_user_code_retries, ubf_context):
        ...
    def step_init(self, flow, graph, step_name, decorators, environment, flow_datastore, logger):
        ...
    def task_pre_step(self, step_name, task_datastore, metadata, run_id, task_id, flow, graph, retry_count, max_user_code_retries, ubf_context, inputs):
        ...
    def task_decorate(self, step_func, flow, graph, retry_count, max_user_code_retries, ubf_context):
        ...
    def setup_distributed_env(self, flow):
        ...
    ...

