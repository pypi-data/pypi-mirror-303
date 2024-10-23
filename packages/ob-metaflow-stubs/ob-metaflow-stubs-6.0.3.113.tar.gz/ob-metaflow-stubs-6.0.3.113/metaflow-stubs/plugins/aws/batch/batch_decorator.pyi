##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.471642                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.exception
    import metaflow.metaflow_current
    import metaflow.decorators

current: metaflow.metaflow_current.Current

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

def get_run_time_limit_for_task(step_decos):
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

def sync_local_metadata_to_datastore(metadata_local_dir, task_ds):
    ...

ECS_S3_ACCESS_IAM_ROLE: None

BATCH_JOB_QUEUE: None

BATCH_CONTAINER_IMAGE: None

BATCH_CONTAINER_REGISTRY: None

ECS_FARGATE_EXECUTION_ROLE: None

DATASTORE_LOCAL_DIR: str

UBF_CONTROL: str

class BatchException(metaflow.exception.MetaflowException, metaclass=type):
    ...

def compute_resource_attributes(decos, compute_deco, step_name, resource_defaults):
    """
    Compute resource values taking into account defaults, the values specified
    in the compute decorator (like @batch or @kubernetes) directly, and
    resources specified via @resources decorator.
    
    Returns a dictionary of resource attr -> value (str).
    """
    ...

def get_docker_registry(image_uri):
    """
    Explanation:
        (.+?(?:[:.].+?)\/)? - [GROUP 0] REGISTRY
            .+?                  - A registry must start with at least one character
            (?:[:.].+?)\/       - A registry must have ":" or "." and end with "/"
            ?                    - Make a registry optional
        (.*?)                - [GROUP 1] REPOSITORY
            .*?                  - Get repository name until separator
        (?:[@:])?            - SEPARATOR
            ?:                   - Don't capture separator
            [@:]                 - The separator must be either "@" or ":"
            ?                    - The separator is optional
        ((?<=[@:]).*)?       - [GROUP 2] TAG / DIGEST
            (?<=[@:])            - A tag / digest must be preceded by "@" or ":"
            .*                   - Capture rest of tag / digest
            ?                    - A tag / digest is optional
    Examples:
        image
            - None
            - image
            - None
        example/image
            - None
            - example/image
            - None
        example/image:tag
            - None
            - example/image
            - tag
        example.domain.com/example/image:tag
            - example.domain.com/
            - example/image
            - tag
        123.123.123.123:123/example/image:tag
            - 123.123.123.123:123/
            - example/image
            - tag
        example.domain.com/example/image@sha256:45b23dee0
            - example.domain.com/
            - example/image
            - sha256:45b23dee0
    """
    ...

def get_ec2_instance_metadata():
    """
    Fetches the EC2 instance metadata through AWS instance metadata service
    
    Returns either an empty dictionary, or one with the keys
        - ec2-instance-id
        - ec2-instance-type
        - ec2-region
        - ec2-availability-zone
    """
    ...

class BatchDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    """
    Specifies that this step should execute on [AWS Batch](https://aws.amazon.com/batch/).
    
    Parameters
    ----------
    cpu : int, default 1
        Number of CPUs required for this step. If `@resources` is
        also present, the maximum value from all decorators is used.
    gpu : int, default 0
        Number of GPUs required for this step. If `@resources` is
        also present, the maximum value from all decorators is used.
    memory : int, default 4096
        Memory size (in MB) required for this step. If
        `@resources` is also present, the maximum value from all decorators is
        used.
    image : str, optional, default None
        Docker image to use when launching on AWS Batch. If not specified, and
        METAFLOW_BATCH_CONTAINER_IMAGE is specified, that image is used. If
        not, a default Docker image mapping to the current version of Python is used.
    queue : str, default METAFLOW_BATCH_JOB_QUEUE
        AWS Batch Job Queue to submit the job to.
    iam_role : str, default METAFLOW_ECS_S3_ACCESS_IAM_ROLE
        AWS IAM role that AWS Batch container uses to access AWS cloud resources.
    execution_role : str, default METAFLOW_ECS_FARGATE_EXECUTION_ROLE
        AWS IAM role that AWS Batch can use [to trigger AWS Fargate tasks]
        (https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html).
    shared_memory : int, optional, default None
        The value for the size (in MiB) of the /dev/shm volume for this step.
        This parameter maps to the `--shm-size` option in Docker.
    max_swap : int, optional, default None
        The total amount of swap memory (in MiB) a container can use for this
        step. This parameter is translated to the `--memory-swap` option in
        Docker where the value is the sum of the container memory plus the
        `max_swap` value.
    swappiness : int, optional, default None
        This allows you to tune memory swappiness behavior for this step.
        A swappiness value of 0 causes swapping not to happen unless absolutely
        necessary. A swappiness value of 100 causes pages to be swapped very
        aggressively. Accepted values are whole numbers between 0 and 100.
    use_tmpfs : bool, default False
        This enables an explicit tmpfs mount for this step. Note that tmpfs is
        not available on Fargate compute environments
    tmpfs_tempdir : bool, default True
        sets METAFLOW_TEMPDIR to tmpfs_path if set for this step.
    tmpfs_size : int, optional, default None
        The value for the size (in MiB) of the tmpfs mount for this step.
        This parameter maps to the `--tmpfs` option in Docker. Defaults to 50% of the
        memory allocated for this step.
    tmpfs_path : str, optional, default None
        Path to tmpfs mount for this step. Defaults to /metaflow_temp.
    inferentia : int, default 0
        Number of Inferentia chips required for this step.
    trainium : int, default None
        Alias for inferentia. Use only one of the two.
    efa : int, default 0
        Number of elastic fabric adapter network devices to attach to container
    ephemeral_storage : int, default None
        The total amount, in GiB, of ephemeral storage to set for the task, 21-200GiB.
        This is only relevant for Fargate compute environments
    log_driver: str, optional, default None
        The log driver to use for the Amazon ECS container.
    log_options: List[str], optional, default None
        List of strings containing options for the chosen log driver. The configurable values
        depend on the `log driver` chosen. Validation of these options is not supported yet.
        Example: [`awslogs-group:aws/batch/job`]
    """
    def __init__(self, attributes = None, statically_defined = False):
        ...
    def step_init(self, flow, graph, step, decos, environment, flow_datastore, logger):
        ...
    def runtime_init(self, flow, graph, package, run_id):
        ...
    def runtime_task_created(self, task_datastore, task_id, split_index, input_paths, is_cloned, ubf_context):
        ...
    def runtime_step_cli(self, cli_args, retry_count, max_user_code_retries, ubf_context):
        ...
    def task_pre_step(self, step_name, task_datastore, metadata, run_id, task_id, flow, graph, retry_count, max_retries, ubf_context, inputs):
        ...
    def task_finished(self, step_name, flow, graph, is_task_ok, retry_count, max_retries):
        ...
    ...

