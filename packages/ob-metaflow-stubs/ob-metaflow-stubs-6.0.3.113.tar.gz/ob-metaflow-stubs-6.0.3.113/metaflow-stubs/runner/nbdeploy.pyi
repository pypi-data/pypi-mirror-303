##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.402020                                        #
##################################################################################

from __future__ import annotations

import typing

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

def get_current_cell(ipython):
    ...

def format_flowfile(cell):
    """
    Formats the given cell content to create a valid Python script that can be executed as a Metaflow flow.
    """
    ...

DEFAULT_DIR: str

class NBDeployerInitializationError(Exception, metaclass=type):
    """
    Custom exception for errors during NBDeployer initialization.
    """
    ...

class NBDeployer(object, metaclass=type):
    """
    A  wrapper over `Deployer` for deploying flows defined in a Jupyter
    notebook cell.
    
    Instantiate this class on the last line of a notebook cell where
    a `flow` is defined. In contrast to `Deployer`, this class is not
    meant to be used in a context manager.
    
    ```python
    deployer = NBDeployer(FlowName)
    ar = deployer.argo_workflows(name="madhur")
    ar_obj = ar.create()
    result = ar_obj.trigger(alpha=300)
    print(result.status)
    print(result.run)
    result.terminate()
    ```
    
    Parameters
    ----------
    flow : FlowSpec
        Flow defined in the same cell
    show_output : bool, default True
        Show the 'stdout' and 'stderr' to the console by default,
    profile : Optional[str], default None
        Metaflow profile to use to deploy this run. If not specified, the default
        profile is used (or the one already set using `METAFLOW_PROFILE`)
    env : Optional[Dict[str, str]], default None
        Additional environment variables to set. This overrides the
        environment set for this process.
    base_dir : Optional[str], default None
        The directory to run the subprocess in; if not specified, a temporary
        directory is used.
    **kwargs : Any
        Additional arguments that you would pass to `python myflow.py` i.e. options
        listed in `python myflow.py --help`
    """
    def __init__(self, flow, show_output: bool = True, profile: typing.Optional[str] = None, env: typing.Optional[typing.Dict] = None, base_dir: str = "/tmp", file_read_timeout: int = 3600, **kwargs):
        ...
    def cleanup(self):
        """
        Delete any temporary files created during execution.
        """
        ...
    ...

