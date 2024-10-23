##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.400125                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.runner.metaflow_runner

class Runner(object, metaclass=type):
    """
    Metaflow's Runner API that presents a programmatic interface
    to run flows and perform other operations either synchronously or asynchronously.
    The class expects a path to the flow file along with optional arguments
    that match top-level options on the command-line.
    
    This class works as a context manager, calling `cleanup()` to remove
    temporary files at exit.
    
    Example:
    ```python
    with Runner('slowflow.py', pylint=False) as runner:
        result = runner.run(alpha=5, tags=["abc", "def"], max_workers=5)
        print(result.run.finished)
    ```
    
    Parameters
    ----------
    flow_file : str
        Path to the flow file to run
    show_output : bool, default True
        Show the 'stdout' and 'stderr' to the console by default,
        Only applicable for synchronous 'run' and 'resume' functions.
    profile : Optional[str], default None
        Metaflow profile to use to run this run. If not specified, the default
        profile is used (or the one already set using `METAFLOW_PROFILE`)
    env : Optional[Dict], default None
        Additional environment variables to set for the Run. This overrides the
        environment set for this process.
    cwd : Optional[str], default None
        The directory to run the subprocess in; if not specified, the current
        directory is used.
    file_read_timeout : int, default 3600
        The timeout until which we try to read the runner attribute file.
    **kwargs : Any
        Additional arguments that you would pass to `python myflow.py` before
        the `run` command.
    """
    def __init__(self, flow_file: str, show_output: bool = True, profile: typing.Optional[str] = None, env: typing.Optional[typing.Dict] = None, cwd: typing.Optional[str] = None, file_read_timeout: int = 3600, **kwargs):
        ...
    def __enter__(self) -> metaflow.runner.metaflow_runner.Runner:
        ...
    def __aenter__(self) -> metaflow.runner.metaflow_runner.Runner:
        ...
    def _Runner__get_executing_run(self, tfp_runner_attribute, command_obj):
        ...
    def run(self, **kwargs) -> metaflow.runner.metaflow_runner.ExecutingRun:
        """
        Blocking execution of the run. This method will wait until
        the run has completed execution.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python myflow.py` after
            the `run` command, in particular, any parameters accepted by the flow.
        
        Returns
        -------
        ExecutingRun
            ExecutingRun containing the results of the run.
        """
        ...
    def resume(self, **kwargs):
        """
        Blocking resume execution of the run.
        This method will wait until the resumed run has completed execution.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python ./myflow.py` after
            the `resume` command.
        
        Returns
        -------
        ExecutingRun
            ExecutingRun containing the results of the resumed run.
        """
        ...
    def async_run(self, **kwargs) -> metaflow.runner.metaflow_runner.ExecutingRun:
        """
        Non-blocking execution of the run. This method will return as soon as the
        run has launched.
        
        Note that this method is asynchronous and needs to be `await`ed.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python myflow.py` after
            the `run` command, in particular, any parameters accepted by the flow.
        
        Returns
        -------
        ExecutingRun
            ExecutingRun representing the run that was started.
        """
        ...
    def async_resume(self, **kwargs):
        """
        Non-blocking resume execution of the run.
        This method will return as soon as the resume has launched.
        
        Note that this method is asynchronous and needs to be `await`ed.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python myflow.py` after
            the `resume` command.
        
        Returns
        -------
        ExecutingRun
            ExecutingRun representing the resumed run that was started.
        """
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __aexit__(self, exc_type, exc_value, traceback):
        ...
    def cleanup(self):
        """
        Delete any temporary files created during execution.
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

class NBRunnerInitializationError(Exception, metaclass=type):
    """
    Custom exception for errors during NBRunner initialization.
    """
    ...

class NBRunner(object, metaclass=type):
    """
    A  wrapper over `Runner` for executing flows defined in a Jupyter
    notebook cell.
    
    Instantiate this class on the last line of a notebook cell where
    a `flow` is defined. In contrast to `Runner`, this class is not
    meant to be used in a context manager. Instead, use a blocking helper
    function like `nbrun` (which calls `cleanup()` internally) or call
    `cleanup()` explictly when using non-blocking APIs.
    
    ```python
    run = NBRunner(FlowName).nbrun()
    ```
    
    Parameters
    ----------
    flow : FlowSpec
        Flow defined in the same cell
    show_output : bool, default True
        Show the 'stdout' and 'stderr' to the console by default,
        Only applicable for synchronous 'run' and 'resume' functions.
    profile : Optional[str], default None
        Metaflow profile to use to run this run. If not specified, the default
        profile is used (or the one already set using `METAFLOW_PROFILE`)
    env : Optional[Dict], default None
        Additional environment variables to set for the Run. This overrides the
        environment set for this process.
    base_dir : Optional[str], default None
        The directory to run the subprocess in; if not specified, a temporary
        directory is used.
    file_read_timeout : int, default 3600
        The timeout until which we try to read the runner attribute file.
    **kwargs : Any
        Additional arguments that you would pass to `python myflow.py` before
        the `run` command.
    """
    def __init__(self, flow, show_output: bool = True, profile: typing.Optional[str] = None, env: typing.Optional[typing.Dict] = None, base_dir: str = "/tmp", file_read_timeout: int = 3600, **kwargs):
        ...
    def nbrun(self, **kwargs):
        """
        Blocking execution of the run. This method will wait until
        the run has completed execution.
        
        Note that in contrast to `run`, this method returns a
        `metaflow.Run` object directly and calls `cleanup()` internally
        to support a common notebook pattern of executing a flow and
        retrieving its results immediately.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python myflow.py` after
            the `run` command, in particular, any parameters accepted by the flow.
        
        Returns
        -------
        Run
            A `metaflow.Run` object representing the finished run.
        """
        ...
    def nbresume(self, **kwargs):
        """
        Blocking resuming of a run. This method will wait until
        the resumed run has completed execution.
        
        Note that in contrast to `resume`, this method returns a
        `metaflow.Run` object directly and calls `cleanup()` internally
        to support a common notebook pattern of executing a flow and
        retrieving its results immediately.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python myflow.py` after
            the `resume` command.
        
        Returns
        -------
        Run
            A `metaflow.Run` object representing the resumed run.
        """
        ...
    def run(self, **kwargs):
        """
        Runs the flow.
        """
        ...
    def resume(self, **kwargs):
        """
        Resumes the flow.
        """
        ...
    def async_run(self, **kwargs):
        """
        Non-blocking execution of the run. This method will return as soon as the
        run has launched. This method is equivalent to `Runner.async_run`.
        
        Note that this method is asynchronous and needs to be `await`ed.
        
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python myflow.py` after
            the `run` command, in particular, any parameters accepted by the flow.
        
        Returns
        -------
        ExecutingRun
            ExecutingRun representing the run that was started.
        """
        ...
    def async_resume(self, **kwargs):
        """
        Non-blocking execution of the run. This method will return as soon as the
        run has launched. This method is equivalent to `Runner.async_resume`.
        
        Note that this method is asynchronous and needs to be `await`ed.
        
        Parameters
        ----------
        **kwargs : Any
            Additional arguments that you would pass to `python myflow.py` after
            the `run` command, in particular, any parameters accepted by the flow.
        
        Returns
        -------
        ExecutingRun
            ExecutingRun representing the run that was started.
        """
        ...
    def cleanup(self):
        """
        Delete any temporary files created during execution.
        
        Call this method after using `async_run` or `async_resume`. You don't
        have to call this after `nbrun` or `nbresume`.
        """
        ...
    ...

