##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.418849                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.exception
    import metaflow.metaflow_current
    import metaflow.decorators

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

class MetaflowExceptionWrapper(Exception, metaclass=type):
    def __init__(self, exc = None):
        ...
    def __reduce__(self):
        ...
    def __getstate__(self):
        ...
    def __setstate__(self, state):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    ...

current: metaflow.metaflow_current.Current

NUM_FALLBACK_RETRIES: int

class FailureHandledByCatch(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, retry_count):
        ...
    ...

class CatchDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    """
    Specifies that the step will success under all circumstances.
    
    The decorator will create an optional artifact, specified by `var`, which
    contains the exception raised. You can use it to detect the presence
    of errors, indicating that all happy-path artifacts produced by the step
    are missing.
    
    Parameters
    ----------
    var : str, optional, default None
        Name of the artifact in which to store the caught exception.
        If not specified, the exception is not stored.
    print_exception : bool, default True
        Determines whether or not the exception is printed to
        stdout when caught.
    """
    def step_init(self, flow, graph, step, decos, environment, flow_datastore, logger):
        ...
    def task_exception(self, exception, step, flow, graph, retry_count, max_user_code_retries):
        ...
    def task_post_step(self, step_name, flow, graph, retry_count, max_user_code_retries):
        ...
    def step_task_retry_count(self):
        ...
    def task_decorate(self, step_func, flow, graph, retry_count, max_user_code_retries, ubf_context):
        ...
    ...

