##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.468504                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.runner.deployer

class StepFunctions(object, metaclass=type):
    def __init__(self, name, graph, flow, code_package_sha, code_package_url, production_token, metadata, flow_datastore, environment, event_logger, monitor, tags = None, namespace = None, username = None, max_workers = None, workflow_timeout = None, is_project = False, use_distributed_map = False):
        ...
    def to_json(self):
        ...
    def trigger_explanation(self):
        ...
    def deploy(self, log_execution_history):
        ...
    def schedule(self):
        ...
    @classmethod
    def delete(cls, name):
        ...
    @classmethod
    def terminate(cls, flow_name, name):
        ...
    @classmethod
    def trigger(cls, name, parameters):
        ...
    @classmethod
    def list(cls, name, states):
        ...
    @classmethod
    def get_existing_deployment(cls, name):
        ...
    @classmethod
    def get_execution(cls, state_machine_name, name):
        ...
    ...

class DeployerImpl(object, metaclass=type):
    """
    Base class for deployer implementations. Each implementation should define a TYPE
    class variable that matches the name of the CLI group.
    
    Parameters
    ----------
    flow_file : str
        Path to the flow file to deploy.
    show_output : bool, default True
        Show the 'stdout' and 'stderr' to the console by default.
    profile : Optional[str], default None
        Metaflow profile to use for the deployment. If not specified, the default
        profile is used.
    env : Optional[Dict], default None
        Additional environment variables to set for the deployment.
    cwd : Optional[str], default None
        The directory to run the subprocess in; if not specified, the current
        directory is used.
    file_read_timeout : int, default 3600
        The timeout until which we try to read the deployer attribute file.
    **kwargs : Any
        Additional arguments that you would pass to `python myflow.py` before
        the deployment command.
    """
    def __init__(self, flow_file: str, show_output: bool = True, profile: typing.Optional[str] = None, env: typing.Optional[typing.Dict] = None, cwd: typing.Optional[str] = None, file_read_timeout: int = 3600, **kwargs):
        ...
    def __enter__(self) -> metaflow.runner.deployer.DeployerImpl:
        ...
    def create(self, **kwargs) -> metaflow.runner.deployer.DeployedFlow:
        """
        Create a deployed flow using the deployer implementation.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments to pass to `create` corresponding to the
            command line arguments of `create`
        
        Returns
        -------
        DeployedFlow
            DeployedFlow object representing the deployed flow.
        
        Raises
        ------
        Exception
            If there is an error during deployment.
        """
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Cleanup resources on exit.
        """
        ...
    def cleanup(self):
        """
        Cleanup resources.
        """
        ...
    ...

class DeployedFlow(object, metaclass=metaflow.runner.deployer.DeploymentMethodsMeta):
    """
    DeployedFlow class represents a flow that has been deployed.
    
    Parameters
    ----------
    deployer : DeployerImpl
        Instance of the deployer implementation.
    """
    def __init__(self, deployer: metaflow.runner.deployer.DeployerImpl):
        ...
    @staticmethod
    def from_deployment(identifier, metadata = None, impl = None):
        ...
    ...

class TriggeredRun(object, metaclass=type):
    """
    TriggeredRun class represents a run that has been triggered on a production orchestrator.
    
    Only when the `start` task starts running, the `run` object corresponding to the run
    becomes available.
    """
    def __init__(self, deployer: metaflow.runner.deployer.DeployerImpl, content: str):
        ...
    def wait_for_run(self, timeout = None):
        """
        Wait for the `run` property to become available.
        
        Parameters
        ----------
        timeout : int, optional
            Maximum time to wait for the `run` to become available, in seconds. If None, wait indefinitely.
        
        Raises
        ------
        TimeoutError
            If the `run` is not available within the specified timeout.
        """
        ...
    @property
    def run(self):
        """
        Retrieve the `Run` object for the triggered run.
        
        Note that Metaflow `Run` becomes available only when the `start` task
        has started executing.
        
        Returns
        -------
        Run, optional
            Metaflow Run object if the `start` step has started executing, otherwise None.
        """
        ...
    ...

def get_lower_level_group(api, top_level_kwargs: typing.Dict, _type: typing.Optional[str], deployer_kwargs: typing.Dict):
    """
    Retrieve a lower-level group from the API based on the type and provided arguments.
    
    Parameters
    ----------
    api : MetaflowAPI
        Metaflow API instance.
    top_level_kwargs : Dict
        Top-level keyword arguments to pass to the API.
    _type : str
        Type of the deployer implementation to target.
    deployer_kwargs : Dict
        Keyword arguments specific to the deployer.
    
    Returns
    -------
    Any
        The lower-level group object retrieved from the API.
    
    Raises
    ------
    ValueError
        If the `_type` is None.
    """
    ...

def handle_timeout(tfp_runner_attribute, command_obj: "CommandManager", file_read_timeout: int):
    """
    Handle the timeout for a running subprocess command that reads a file
    and raises an error with appropriate logs if a TimeoutError occurs.
    
    Parameters
    ----------
    tfp_runner_attribute : NamedTemporaryFile
        Temporary file that stores runner attribute data.
    command_obj : CommandManager
        Command manager object that encapsulates the running command details.
    file_read_timeout : int
        Timeout for reading the file.
    
    Returns
    -------
    str
        Content read from the temporary file.
    
    Raises
    ------
    RuntimeError
        If a TimeoutError occurs, it raises a RuntimeError with the command's
        stdout and stderr logs.
    """
    ...

def terminate(instance: metaflow.runner.deployer.TriggeredRun, **kwargs):
    """
    Terminate the running workflow.
    
    Parameters
    ----------
    **kwargs : Any
        Additional arguments to pass to the terminate command.
    
    Returns
    -------
    bool
        True if the command was successful, False otherwise.
    """
    ...

def production_token(instance: metaflow.runner.deployer.DeployedFlow):
    """
    Get the production token for the deployed flow.
    
    Returns
    -------
    str, optional
        The production token, None if it cannot be retrieved.
    """
    ...

def list_runs(instance: metaflow.runner.deployer.DeployedFlow, states: typing.Optional[typing.List[str]] = None):
    """
    List runs of the deployed flow.
    
    Parameters
    ----------
    states : Optional[List[str]], optional
        A list of states to filter the runs by. Allowed values are:
        RUNNING, SUCCEEDED, FAILED, TIMED_OUT, ABORTED.
        If not provided, all states will be considered.
    
    Returns
    -------
    List[TriggeredRun]
        A list of TriggeredRun objects representing the runs of the deployed flow.
    
    Raises
    ------
    ValueError
        If any of the provided states are invalid or if there are duplicate states.
    """
    ...

def delete(instance: metaflow.runner.deployer.DeployedFlow, **kwargs):
    """
    Delete the deployed flow.
    
    Parameters
    ----------
    **kwargs : Any
        Additional arguments to pass to the delete command.
    
    Returns
    -------
    bool
        True if the command was successful, False otherwise.
    """
    ...

def trigger(instance: metaflow.runner.deployer.DeployedFlow, **kwargs):
    """
    Trigger a new run for the deployed flow.
    
    Parameters
    ----------
    **kwargs : Any
        Additional arguments to pass to the trigger command, `Parameters` in particular
    
    Returns
    -------
    StepFunctionsTriggeredRun
        The triggered run instance.
    
    Raises
    ------
    Exception
        If there is an error during the trigger process.
    """
    ...

class StepFunctionsDeployer(metaflow.runner.deployer.DeployerImpl, metaclass=type):
    """
    Deployer implementation for AWS Step Functions.
    
    Attributes
    ----------
    TYPE : ClassVar[Optional[str]]
        The type of the deployer, which is "step-functions".
    """
    def __init__(self, deployer_kwargs, **kwargs):
        """
        Initialize the StepFunctionsDeployer.
        
        Parameters
        ----------
        deployer_kwargs : dict
            The deployer-specific keyword arguments.
        **kwargs : Any
            Additional arguments to pass to the superclass constructor.
        """
        ...
    ...

