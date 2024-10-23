##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.451155                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.graph
    import metaflow
    import metaflow.datastore.inputs
    import metaflow.flowspec
    import typing
    import metaflow.metaflow_current
    import metaflow.events
    import metaflow.decorators

current: metaflow.metaflow_current.Current

class Trigger(object, metaclass=type):
    """
    Defines a container of event triggers' metadata.
    """
    def __init__(self, _meta = None):
        ...
    @classmethod
    def from_runs(cls, run_objs: typing.List["metaflow.Run"]):
        ...
    @property
    def event(self) -> typing.Optional[metaflow.events.MetaflowEvent]:
        """
        The `MetaflowEvent` object corresponding to the triggering event.
        
        If multiple events triggered the run, this property is the latest event.
        
        Returns
        -------
        MetaflowEvent, optional
            The latest event that triggered the run, if applicable.
        """
        ...
    @property
    def events(self) -> typing.Optional[typing.List[metaflow.events.MetaflowEvent]]:
        """
        The list of `MetaflowEvent` objects correspondings to all the triggering events.
        
        Returns
        -------
        List[MetaflowEvent], optional
            List of all events that triggered the run
        """
        ...
    @property
    def run(self) -> typing.Optional["metaflow.Run"]:
        """
        The corresponding `Run` object if the triggering event is a Metaflow run.
        
        In case multiple runs triggered the run, this property is the latest run.
        Returns `None` if none of the triggering events are a `Run`.
        
        Returns
        -------
        Run, optional
            Latest Run that triggered this run, if applicable.
        """
        ...
    @property
    def runs(self) -> typing.Optional[typing.List["metaflow.Run"]]:
        """
        The list of `Run` objects in the triggering events.
        Returns `None` if none of the triggering events are `Run` objects.
        
        Returns
        -------
        List[Run], optional
            List of runs that triggered this run, if applicable.
        """
        ...
    def __getitem__(self, key: str) -> typing.Union["metaflow.Run", metaflow.events.MetaflowEvent]:
        """
        If triggering events are runs, `key` corresponds to the flow name of the triggering run.
        Otherwise, `key` corresponds to the event name and a `MetaflowEvent` object is returned.
        
        Returns
        -------
        Union[Run, MetaflowEvent]
            `Run` object if triggered by a run. Otherwise returns a `MetaflowEvent`.
        """
        ...
    def __iter__(self):
        ...
    def __contains__(self, ident: str) -> bool:
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

ARGO_EVENTS_WEBHOOK_URL: None

class FlowSpec(object, metaclass=metaflow.flowspec._FlowSpecMeta):
    """
    Main class from which all Flows should inherit.
    
    Attributes
    ----------
    index
    input
    """
    def __init__(self, use_cli = True):
        """
        Construct a FlowSpec
        
        Parameters
        ----------
        use_cli : bool, default True
            Set to True if the flow is invoked from __main__ or the command line
        """
        ...
    @property
    def script_name(self) -> str:
        """
        [Legacy function - do not use. Use `current` instead]
        
        Returns the name of the script containing the flow
        
        Returns
        -------
        str
            A string containing the name of the script
        """
        ...
    def __iter__(self):
        """
        [Legacy function - do not use]
        
        Iterate over all steps in the Flow
        
        Returns
        -------
        Iterator[graph.DAGNode]
            Iterator over the steps in the flow
        """
        ...
    def __getattr__(self, name: str):
        ...
    def cmd(self, cmdline, input = {}, output = []):
        """
        [Legacy function - do not use]
        """
        ...
    @property
    def index(self) -> typing.Optional[int]:
        """
        The index of this foreach branch.
        
        In a foreach step, multiple instances of this step (tasks) will be executed,
        one for each element in the foreach. This property returns the zero based index
        of the current task. If this is not a foreach step, this returns None.
        
        If you need to know the indices of the parent tasks in a nested foreach, use
        `FlowSpec.foreach_stack`.
        
        Returns
        -------
        int, optional
            Index of the task in a foreach step.
        """
        ...
    @property
    def input(self) -> typing.Optional[typing.Any]:
        """
        The value of the foreach artifact in this foreach branch.
        
        In a foreach step, multiple instances of this step (tasks) will be executed,
        one for each element in the foreach. This property returns the element passed
        to the current task. If this is not a foreach step, this returns None.
        
        If you need to know the values of the parent tasks in a nested foreach, use
        `FlowSpec.foreach_stack`.
        
        Returns
        -------
        object, optional
            Input passed to the foreach task.
        """
        ...
    def foreach_stack(self) -> typing.Optional[typing.List[typing.Tuple[int, int, typing.Any]]]:
        """
        Returns the current stack of foreach indexes and values for the current step.
        
        Use this information to understand what data is being processed in the current
        foreach branch. For example, considering the following code:
        ```
        @step
        def root(self):
            self.split_1 = ['a', 'b', 'c']
            self.next(self.nest_1, foreach='split_1')
        
        @step
        def nest_1(self):
            self.split_2 = ['d', 'e', 'f', 'g']
            self.next(self.nest_2, foreach='split_2'):
        
        @step
        def nest_2(self):
            foo = self.foreach_stack()
        ```
        
        `foo` will take the following values in the various tasks for nest_2:
        ```
            [(0, 3, 'a'), (0, 4, 'd')]
            [(0, 3, 'a'), (1, 4, 'e')]
            ...
            [(0, 3, 'a'), (3, 4, 'g')]
            [(1, 3, 'b'), (0, 4, 'd')]
            ...
        ```
        where each tuple corresponds to:
        
        - The index of the task for that level of the loop.
        - The number of splits for that level of the loop.
        - The value for that level of the loop.
        
        Note that the last tuple returned in a task corresponds to:
        
        - 1st element: value returned by `self.index`.
        - 3rd element: value returned by `self.input`.
        
        Returns
        -------
        List[Tuple[int, int, Any]]
            An array describing the current stack of foreach steps.
        """
        ...
    def merge_artifacts(self, inputs: metaflow.datastore.inputs.Inputs, exclude: typing.Optional[typing.List[str]] = None, include: typing.Optional[typing.List[str]] = None):
        """
        Helper function for merging artifacts in a join step.
        
        This function takes all the artifacts coming from the branches of a
        join point and assigns them to self in the calling step. Only artifacts
        not set in the current step are considered. If, for a given artifact, different
        values are present on the incoming edges, an error will be thrown and the artifacts
        that conflict will be reported.
        
        As a few examples, in the simple graph: A splitting into B and C and joining in D:
        ```
        A:
          self.x = 5
          self.y = 6
        B:
          self.b_var = 1
          self.x = from_b
        C:
          self.x = from_c
        
        D:
          merge_artifacts(inputs)
        ```
        In D, the following artifacts are set:
          - `y` (value: 6), `b_var` (value: 1)
          - if `from_b` and `from_c` are the same, `x` will be accessible and have value `from_b`
          - if `from_b` and `from_c` are different, an error will be thrown. To prevent this error,
            you need to manually set `self.x` in D to a merged value (for example the max) prior to
            calling `merge_artifacts`.
        
        Parameters
        ----------
        inputs : Inputs
            Incoming steps to the join point.
        exclude : List[str], optional, default None
            If specified, do not consider merging artifacts with a name in `exclude`.
            Cannot specify if `include` is also specified.
        include : List[str], optional, default None
            If specified, only merge artifacts specified. Cannot specify if `exclude` is
            also specified.
        
        Raises
        ------
        MetaflowException
            This exception is thrown if this is not called in a join step.
        UnhandledInMergeArtifactsException
            This exception is thrown in case of unresolved conflicts.
        MissingInMergeArtifactsException
            This exception is thrown in case an artifact specified in `include` cannot
            be found.
        """
        ...
    def next(self, *dsts: typing.Callable[..., None], **kwargs):
        """
        Indicates the next step to execute after this step has completed.
        
        This statement should appear as the last statement of each step, except
        the end step.
        
        There are several valid formats to specify the next step:
        
        - Straight-line connection: `self.next(self.next_step)` where `next_step` is a method in
          the current class decorated with the `@step` decorator.
        
        - Static fan-out connection: `self.next(self.step1, self.step2, ...)` where `stepX` are
          methods in the current class decorated with the `@step` decorator.
        
        - Foreach branch:
          ```
          self.next(self.foreach_step, foreach='foreach_iterator')
          ```
          In this situation, `foreach_step` is a method in the current class decorated with the
          `@step` decorator and `foreach_iterator` is a variable name in the current class that
          evaluates to an iterator. A task will be launched for each value in the iterator and
          each task will execute the code specified by the step `foreach_step`.
        
        Parameters
        ----------
        dsts : Callable[..., None]
            One or more methods annotated with `@step`.
        
        Raises
        ------
        InvalidNextException
            Raised if the format of the arguments does not match one of the ones given above.
        """
        ...
    def __str__(self):
        ...
    def __getstate__(self):
        ...
    ...

class ArgoEvent(object, metaclass=type):
    """
    ArgoEvent is a small event, a message, that can be published to Argo Workflows. The
    event will eventually start all flows which have been previously deployed with `@trigger`
    to wait for this particular named event.
    
    Parameters
    ----------
    name : str,
        Name of the event
    url : str, optional
        Override the event endpoint from `ARGO_EVENTS_WEBHOOK_URL`.
    payload : Dict, optional
        A set of key-value pairs delivered in this event. Used to set parameters of triggered flows.
    """
    def __init__(self, name, url = None, payload = None, access_token = None):
        ...
    def add_to_payload(self, key, value):
        """
        Add a key-value pair in the payload. This is typically used to set parameters
        of triggered flows. Often, `key` is the parameter name you want to set to
        `value`. Overrides any existing value of `key`.
        
        Parameters
        ----------
        key : str
            Key
        value : str
            Value
        """
        ...
    def safe_publish(self, payload = None, ignore_errors = True):
        """
        Publishes an event when called inside a deployed workflow. Outside a deployed workflow
        this function does nothing.
        
        Use this function inside flows to create events safely. As this function is a no-op
        for local runs, you can safely call it during local development without causing unintended
        side-effects. It takes effect only when deployed on Argo Workflows.
        
        Parameters
        ----------
        payload : dict
            Additional key-value pairs to add to the payload.
        ignore_errors : bool, default True
            If True, events are created on a best effort basis - errors are silently ignored.
        """
        ...
    def publish(self, payload = None, force = True, ignore_errors = True):
        """
        Publishes an event.
        
        Note that the function returns immediately after the event has been sent. It
        does not wait for flows to start, nor it guarantees that any flows will start.
        
        Parameters
        ----------
        payload : dict
            Additional key-value pairs to add to the payload.
        ignore_errors : bool, default True
            If True, events are created on a best effort basis - errors are silently ignored.
        """
        ...
    ...

class ArgoWorkflowsInternalDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    def task_pre_step(self, step_name, task_datastore, metadata, run_id, task_id, flow, graph, retry_count, max_user_code_retries, ubf_context, inputs):
        ...
    def task_finished(self, step_name, flow: metaflow.flowspec.FlowSpec, graph: metaflow.graph.FlowGraph, is_task_ok, retry_count, max_user_code_retries):
        ...
    ...

