##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.458542                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.graph
    import metaflow.runner.deployer

def get_metadata() -> str:
    """
    Returns the current Metadata provider.
    
    If this is not set explicitly using `metadata`, the default value is
    determined through the Metaflow configuration. You can use this call to
    check that your configuration is set up properly.
    
    If multiple configuration profiles are present, this call returns the one
    selected through the `METAFLOW_PROFILE` environment variable.
    
    Returns
    -------
    str
        Information about the Metadata provider currently selected. This information typically
        returns provider specific information (like URL for remote providers or local paths for
        local providers).
    """
    ...

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

class ArgoClient(object, metaclass=type):
    def __init__(self, namespace = None):
        ...
    def get_workflow(self, name):
        ...
    def get_workflow_template(self, name):
        ...
    def get_workflow_templates(self):
        ...
    def register_workflow_template(self, name, workflow_template):
        ...
    def delete_cronworkflow(self, name):
        """
        Issues an API call for deleting a cronworkflow
        
        Returns either the successful API response, or None in case the resource was not found.
        """
        ...
    def delete_workflow_template(self, name):
        """
        Issues an API call for deleting a cronworkflow
        
        Returns either the successful API response, or None in case the resource was not found.
        """
        ...
    def terminate_workflow(self, name):
        ...
    def suspend_workflow(self, name):
        ...
    def unsuspend_workflow(self, name):
        ...
    def trigger_workflow_template(self, name, parameters = {}):
        ...
    def schedule_workflow_template(self, name, schedule = None, timezone = None):
        ...
    def register_sensor(self, name, sensor = None):
        ...
    def delete_sensor(self, name):
        """
        Issues an API call for deleting a sensor
        
        Returns either the successful API response, or None in case the resource was not found.
        """
        ...
    ...

KUBERNETES_NAMESPACE: str

class ArgoWorkflows(object, metaclass=type):
    def __init__(self, name, graph: metaflow.graph.FlowGraph, flow, code_package_sha, code_package_url, production_token, metadata, flow_datastore, environment, event_logger, monitor, tags = None, namespace = None, username = None, max_workers = None, workflow_timeout = None, workflow_priority = None, auto_emit_argo_events = False, notify_on_error = False, notify_on_success = False, notify_slack_webhook_url = None, notify_pager_duty_integration_key = None, enable_heartbeat_daemon = True, enable_error_msg_capture = False):
        ...
    def __str__(self):
        ...
    def deploy(self):
        ...
    @staticmethod
    def list_templates(flow_name, all = False):
        ...
    @staticmethod
    def delete(name):
        ...
    @classmethod
    def terminate(cls, flow_name, name):
        ...
    @staticmethod
    def get_workflow_status(flow_name, name):
        ...
    @staticmethod
    def suspend(name):
        ...
    @staticmethod
    def unsuspend(name):
        ...
    @classmethod
    def trigger(cls, name, parameters = None):
        ...
    def schedule(self):
        ...
    def trigger_explanation(self):
        ...
    @classmethod
    def get_existing_deployment(cls, name):
        ...
    @classmethod
    def get_execution(cls, name):
        ...
    def list_to_prose(self, items, singular):
        ...
    ...

class Deployer(object, metaclass=type):
    """
    Use the `Deployer` class to configure and access one of the production
    orchestrators supported by Metaflow.
    
    Parameters
    ----------
    flow_file : str
        Path to the flow file to deploy.
    show_output : bool, default True
        Show the 'stdout' and 'stderr' to the console by default.
    profile : Optional[str], default None
        Metaflow profile to use for the deployment. If not specified, the default
        profile is used.
    env : Optional[Dict[str, str]], default None
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
    def _Deployer__make_function(self, deployer_class):
        """
        Create a function for the given deployer class.
        
        Parameters
        ----------
        deployer_class : Type[DeployerImpl]
            Deployer implementation class.
        
        Returns
        -------
        Callable
            Function that initializes and returns an instance of the deployer class.
        """
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

def generate_fake_flow_file_contents(flow_name: str, param_info: dict, project_name: typing.Optional[str] = None):
    ...

def from_deployment(identifier: str, metadata: typing.Optional[str] = None):
    ...

def suspend(instance: metaflow.runner.deployer.TriggeredRun, **kwargs):
    """
    Suspend the running workflow.
    
    Parameters
    ----------
    **kwargs : Any
        Additional arguments to pass to the suspend command.
    
    Returns
    -------
    bool
        True if the command was successful, False otherwise.
    """
    ...

def unsuspend(instance: metaflow.runner.deployer.TriggeredRun, **kwargs):
    """
    Unsuspend the suspended workflow.
    
    Parameters
    ----------
    **kwargs : Any
        Additional arguments to pass to the unsuspend command.
    
    Returns
    -------
    bool
        True if the command was successful, False otherwise.
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

def status(instance: metaflow.runner.deployer.TriggeredRun):
    """
    Get the status of the triggered run.
    
    Returns
    -------
    str, optional
        The status of the workflow considering the run object, or None if the status could not be retrieved.
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
    ArgoWorkflowsTriggeredRun
        The triggered run instance.
    
    Raises
    ------
    Exception
        If there is an error during the trigger process.
    """
    ...

class ArgoWorkflowsDeployer(metaflow.runner.deployer.DeployerImpl, metaclass=type):
    """
    Deployer implementation for Argo Workflows.
    
    Attributes
    ----------
    TYPE : ClassVar[Optional[str]]
        The type of the deployer, which is "argo-workflows".
    """
    def __init__(self, deployer_kwargs, **kwargs):
        """
        Initialize the ArgoWorkflowsDeployer.
        
        Parameters
        ----------
        deployer_kwargs : dict
            The deployer-specific keyword arguments.
        **kwargs : Any
            Additional arguments to pass to the superclass constructor.
        """
        ...
    ...

