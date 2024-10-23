##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.391054                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.parameters
    import metaflow._vendor.click.types
    import typing
    import metaflow.plugins.datatools.s3.s3
    import io

class MetaflowException(Exception, metaclass=type):
    def __init__(self, msg = "", lineno = None):
        ...
    def __str__(self):
        ...
    ...

class DelayedEvaluationParameter(object, metaclass=type):
    """
    This is a very simple wrapper to allow parameter "conversion" to be delayed until
    the `_set_constants` function in FlowSpec. Typically, parameters are converted
    by click when the command line option is processed. For some parameters, like
    IncludeFile, this is too early as it would mean we would trigger the upload
    of the file too early. If a parameter converts to a DelayedEvaluationParameter
    object through the usual click mechanisms, `_set_constants` knows to invoke the
    __call__ method on that DelayedEvaluationParameter; in that case, the __call__
    method is invoked without any parameter. The return_str parameter will be used
    by schedulers when they need to convert DelayedEvaluationParameters to a
    string to store them
    """
    def __init__(self, name, field, fun):
        ...
    def __call__(self, return_str = False):
        ...
    ...

class DeployTimeField(object, metaclass=type):
    """
    This a wrapper object for a user-defined function that is called
    at deploy time to populate fields in a Parameter. The wrapper
    is needed to make Click show the actual value returned by the
    function instead of a function pointer in its help text. Also, this
    object curries the context argument for the function, and pretty
    prints any exceptions that occur during evaluation.
    """
    def __init__(self, parameter_name, parameter_type, field, fun, return_str = True, print_representation = None):
        ...
    def __call__(self, deploy_time = False):
        ...
    @property
    def description(self):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...
    ...

class Parameter(object, metaclass=type):
    """
    Defines a parameter for a flow.
    
    Parameters must be instantiated as class variables in flow classes, e.g.
    ```
    class MyFlow(FlowSpec):
        param = Parameter('myparam')
    ```
    in this case, the parameter is specified on the command line as
    ```
    python myflow.py run --myparam=5
    ```
    and its value is accessible through a read-only artifact like this:
    ```
    print(self.param == 5)
    ```
    Note that the user-visible parameter name, `myparam` above, can be
    different from the artifact name, `param` above.
    
    The parameter value is converted to a Python type based on the `type`
    argument or to match the type of `default`, if it is set.
    
    Parameters
    ----------
    name : str
        User-visible parameter name.
    default : str or float or int or bool or `JSONType` or a function.
        Default value for the parameter. Use a special `JSONType` class to
        indicate that the value must be a valid JSON object. A function
        implies that the parameter corresponds to a *deploy-time parameter*.
        The type of the default value is used as the parameter `type`.
    type : Type, default None
        If `default` is not specified, define the parameter type. Specify
        one of `str`, `float`, `int`, `bool`, or `JSONType`. If None, defaults
        to the type of `default` or `str` if none specified.
    help : str, optional
        Help text to show in `run --help`.
    required : bool, default False
        Require that the user specified a value for the parameter.
        `required=True` implies that the `default` is not used.
    show_default : bool, default True
        If True, show the default value in the help text.
    """
    def __init__(self, name: str, default: typing.Union[str, float, int, bool, typing.Dict[str, typing.Any], typing.Callable[[], typing.Union[str, float, int, bool, typing.Dict[str, typing.Any]]], None] = None, type: typing.Union[typing.Type[str], typing.Type[float], typing.Type[int], typing.Type[bool], metaflow.parameters.JSONTypeClass, None] = None, help: typing.Optional[str] = None, required: bool = False, show_default: bool = True, **kwargs: typing.Dict[str, typing.Any]):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
    def option_kwargs(self, deploy_mode):
        ...
    def load_parameter(self, v):
        ...
    @property
    def is_string_type(self):
        ...
    def __getitem__(self, x):
        ...
    ...

class ParameterContext(tuple, metaclass=type):
    """
    ParameterContext(flow_name, user_name, parameter_name, logger, ds_type)
    """
    @staticmethod
    def __new__(_cls, flow_name: str, user_name: str, parameter_name: str, logger: typing.Callable[..., None], ds_type: str):
        """
        Create new instance of ParameterContext(flow_name, user_name, parameter_name, logger, ds_type)
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
    def __init__(self, flow_name: str, user_name: str, parameter_name: str, logger: typing.Callable[..., None], ds_type: str):
        ...
    ...

class Local(object, metaclass=type):
    """
    This class allows you to access the local filesystem in a way similar to the S3 datatools
    client. It is a stripped down version for now and only implements the functionality needed
    for this use case.
    
    In the future, we may want to allow it to be used in a way similar to the S3() client.
    """
    @classmethod
    def get_root_from_config(cls, echo, create_on_absent = True):
        ...
    def __init__(self):
        """
        Initialize a new context for Local file operations. This object is based used as
        a context manager for a with statement.
        """
        ...
    def __enter__(self):
        ...
    def __exit__(self, *args):
        ...
    def get(self, key = None, return_missing = False):
        ...
    def put(self, key, obj, overwrite = True):
        ...
    def info(self, key = None, return_missing = False):
        ...
    ...

class S3(object, metaclass=type):
    """
    The Metaflow S3 client.
    
    This object manages the connection to S3 and a temporary diretory that is used
    to download objects. Note that in most cases when the data fits in memory, no local
    disk IO is needed as operations are cached by the operating system, which makes
    operations fast as long as there is enough memory available.
    
    The easiest way is to use this object as a context manager:
    ```
    with S3() as s3:
        data = [obj.blob for obj in s3.get_many(urls)]
    print(data)
    ```
    The context manager takes care of creating and deleting a temporary directory
    automatically. Without a context manager, you must call `.close()` to delete
    the directory explicitly:
    ```
    s3 = S3()
    data = [obj.blob for obj in s3.get_many(urls)]
    s3.close()
    ```
    You can customize the location of the temporary directory with `tmproot`. It
    defaults to the current working directory.
    
    To make it easier to deal with object locations, the client can be initialized
    with an S3 path prefix. There are three ways to handle locations:
    
    1. Use a `metaflow.Run` object or `self`, e.g. `S3(run=self)` which
       initializes the prefix with the global `DATATOOLS_S3ROOT` path, combined
       with the current run ID. This mode makes it easy to version data based
       on the run ID consistently. You can use the `bucket` and `prefix` to
       override parts of `DATATOOLS_S3ROOT`.
    
    2. Specify an S3 prefix explicitly with `s3root`,
       e.g. `S3(s3root='s3://mybucket/some/path')`.
    
    3. Specify nothing, i.e. `S3()`, in which case all operations require
       a full S3 url prefixed with `s3://`.
    
    Parameters
    ----------
    tmproot : str, default: '.'
        Where to store the temporary directory.
    bucket : str, optional
        Override the bucket from `DATATOOLS_S3ROOT` when `run` is specified.
    prefix : str, optional
        Override the path from `DATATOOLS_S3ROOT` when `run` is specified.
    run : FlowSpec or Run, optional
        Derive path prefix from the current or a past run ID, e.g. S3(run=self).
    s3root : str, optional
        If `run` is not specified, use this as the S3 prefix.
    """
    @classmethod
    def get_root_from_config(cls, echo, create_on_absent = True):
        ...
    def __enter__(self) -> metaflow.plugins.datatools.s3.s3.S3:
        ...
    def __exit__(self, *args):
        ...
    def close(self):
        """
        Delete all temporary files downloaded in this context.
        """
        ...
    def list_paths(self, keys: typing.Optional[typing.Iterable[str]] = None) -> typing.List[metaflow.plugins.datatools.s3.s3.S3Object]:
        """
        List the next level of paths in S3.
        
        If multiple keys are specified, listings are done in parallel. The returned
        S3Objects have `.exists == False` if the path refers to a prefix, not an
        existing S3 object.
        
        For instance, if the directory hierarchy is
        ```
        a/0.txt
        a/b/1.txt
        a/c/2.txt
        a/d/e/3.txt
        f/4.txt
        ```
        The `list_paths(['a', 'f'])` call returns
        ```
        a/0.txt (exists == True)
        a/b/ (exists == False)
        a/c/ (exists == False)
        a/d/ (exists == False)
        f/4.txt (exists == True)
        ```
        
        Parameters
        ----------
        keys : Iterable[str], optional, default None
            List of paths.
        
        Returns
        -------
        List[S3Object]
            S3Objects under the given paths, including prefixes (directories) that
            do not correspond to leaf objects.
        """
        ...
    def list_recursive(self, keys: typing.Optional[typing.Iterable[str]] = None) -> typing.List[metaflow.plugins.datatools.s3.s3.S3Object]:
        """
        List all objects recursively under the given prefixes.
        
        If multiple keys are specified, listings are done in parallel. All objects
        returned have `.exists == True` as this call always returns leaf objects.
        
        For instance, if the directory hierarchy is
        ```
        a/0.txt
        a/b/1.txt
        a/c/2.txt
        a/d/e/3.txt
        f/4.txt
        ```
        The `list_paths(['a', 'f'])` call returns
        ```
        a/0.txt (exists == True)
        a/b/1.txt (exists == True)
        a/c/2.txt (exists == True)
        a/d/e/3.txt (exists == True)
        f/4.txt (exists == True)
        ```
        
        Parameters
        ----------
        keys : Iterable[str], optional, default None
            List of paths.
        
        Returns
        -------
        List[S3Object]
            S3Objects under the given paths.
        """
        ...
    def info(self, key: typing.Optional[str] = None, return_missing: bool = False) -> metaflow.plugins.datatools.s3.s3.S3Object:
        """
        Get metadata about a single object in S3.
        
        This call makes a single `HEAD` request to S3 which can be
        much faster than downloading all data with `get`.
        
        Parameters
        ----------
        key : str, optional, default None
            Object to query. It can be an S3 url or a path suffix.
        return_missing : bool, default False
            If set to True, do not raise an exception for a missing key but
            return it as an `S3Object` with `.exists == False`.
        
        Returns
        -------
        S3Object
            An S3Object corresponding to the object requested. The object
            will have `.downloaded == False`.
        """
        ...
    def info_many(self, keys: typing.Iterable[str], return_missing: bool = False) -> typing.List[metaflow.plugins.datatools.s3.s3.S3Object]:
        """
        Get metadata about many objects in S3 in parallel.
        
        This call makes a single `HEAD` request to S3 which can be
        much faster than downloading all data with `get`.
        
        Parameters
        ----------
        keys : Iterable[str]
            Objects to query. Each key can be an S3 url or a path suffix.
        return_missing : bool, default False
            If set to True, do not raise an exception for a missing key but
            return it as an `S3Object` with `.exists == False`.
        
        Returns
        -------
        List[S3Object]
            A list of S3Objects corresponding to the paths requested. The
            objects will have `.downloaded == False`.
        """
        ...
    def get(self, key: typing.Union[str, metaflow.plugins.datatools.s3.s3.S3GetObject, None] = None, return_missing: bool = False, return_info: bool = True) -> metaflow.plugins.datatools.s3.s3.S3Object:
        """
        Get a single object from S3.
        
        Parameters
        ----------
        key : Union[str, S3GetObject], optional, default None
            Object to download. It can be an S3 url, a path suffix, or
            an S3GetObject that defines a range of data to download. If None, or
            not provided, gets the S3 root.
        return_missing : bool, default False
            If set to True, do not raise an exception for a missing key but
            return it as an `S3Object` with `.exists == False`.
        return_info : bool, default True
            If set to True, fetch the content-type and user metadata associated
            with the object at no extra cost, included for symmetry with `get_many`
        
        Returns
        -------
        S3Object
            An S3Object corresponding to the object requested.
        """
        ...
    def get_many(self, keys: typing.Iterable[typing.Union[str, metaflow.plugins.datatools.s3.s3.S3GetObject]], return_missing: bool = False, return_info: bool = True) -> typing.List[metaflow.plugins.datatools.s3.s3.S3Object]:
        """
        Get many objects from S3 in parallel.
        
        Parameters
        ----------
        keys : Iterable[Union[str, S3GetObject]]
            Objects to download. Each object can be an S3 url, a path suffix, or
            an S3GetObject that defines a range of data to download.
        return_missing : bool, default False
            If set to True, do not raise an exception for a missing key but
            return it as an `S3Object` with `.exists == False`.
        return_info : bool, default True
            If set to True, fetch the content-type and user metadata associated
            with the object at no extra cost, included for symmetry with `get_many`.
        
        Returns
        -------
        List[S3Object]
            S3Objects corresponding to the objects requested.
        """
        ...
    def get_recursive(self, keys: typing.Iterable[str], return_info: bool = False) -> typing.List[metaflow.plugins.datatools.s3.s3.S3Object]:
        """
        Get many objects from S3 recursively in parallel.
        
        Parameters
        ----------
        keys : Iterable[str]
            Prefixes to download recursively. Each prefix can be an S3 url or a path suffix
            which define the root prefix under which all objects are downloaded.
        return_info : bool, default False
            If set to True, fetch the content-type and user metadata associated
            with the object.
        
        Returns
        -------
        List[S3Object]
            S3Objects stored under the given prefixes.
        """
        ...
    def get_all(self, return_info: bool = False) -> typing.List[metaflow.plugins.datatools.s3.s3.S3Object]:
        """
        Get all objects under the prefix set in the `S3` constructor.
        
        This method requires that the `S3` object is initialized either with `run` or
        `s3root`.
        
        Parameters
        ----------
        return_info : bool, default False
            If set to True, fetch the content-type and user metadata associated
            with the object.
        
        Returns
        -------
        Iterable[S3Object]
            S3Objects stored under the main prefix.
        """
        ...
    def put(self, key: typing.Union[str, metaflow.plugins.datatools.s3.s3.S3PutObject], obj: typing.Union[io.RawIOBase, io.BufferedIOBase, str, bytes], overwrite: bool = True, content_type: typing.Optional[str] = None, metadata: typing.Optional[typing.Dict[str, str]] = None) -> str:
        """
        Upload a single object to S3.
        
        Parameters
        ----------
        key : Union[str, S3PutObject]
            Object path. It can be an S3 url or a path suffix.
        obj : PutValue
            An object to store in S3. Strings are converted to UTF-8 encoding.
        overwrite : bool, default True
            Overwrite the object if it exists. If set to False, the operation
            succeeds without uploading anything if the key already exists.
        content_type : str, optional, default None
            Optional MIME type for the object.
        metadata : Dict[str, str], optional, default None
            A JSON-encodable dictionary of additional headers to be stored
            as metadata with the object.
        
        Returns
        -------
        str
            URL of the object stored.
        """
        ...
    def put_many(self, key_objs: typing.List[typing.Union[typing.Tuple[str, typing.Union[io.RawIOBase, io.BufferedIOBase, str, bytes]], metaflow.plugins.datatools.s3.s3.S3PutObject]], overwrite: bool = True) -> typing.List[typing.Tuple[str, str]]:
        """
        Upload many objects to S3.
        
        Each object to be uploaded can be specified in two ways:
        
        1. As a `(key, obj)` tuple where `key` is a string specifying
           the path and `obj` is a string or a bytes object.
        
        2. As a `S3PutObject` which contains additional metadata to be
           stored with the object.
        
        Parameters
        ----------
        key_objs : List[Union[Tuple[str, PutValue], S3PutObject]]
            List of key-object pairs to upload.
        overwrite : bool, default True
            Overwrite the object if it exists. If set to False, the operation
            succeeds without uploading anything if the key already exists.
        
        Returns
        -------
        List[Tuple[str, str]]
            List of `(key, url)` pairs corresponding to the objects uploaded.
        """
        ...
    def put_files(self, key_paths: typing.List[typing.Union[typing.Tuple[str, typing.Union[io.RawIOBase, io.BufferedIOBase, str, bytes]], metaflow.plugins.datatools.s3.s3.S3PutObject]], overwrite: bool = True) -> typing.List[typing.Tuple[str, str]]:
        """
        Upload many local files to S3.
        
        Each file to be uploaded can be specified in two ways:
        
        1. As a `(key, path)` tuple where `key` is a string specifying
           the S3 path and `path` is the path to a local file.
        
        2. As a `S3PutObject` which contains additional metadata to be
           stored with the file.
        
        Parameters
        ----------
        key_paths :  List[Union[Tuple[str, PutValue], S3PutObject]]
            List of files to upload.
        overwrite : bool, default True
            Overwrite the object if it exists. If set to False, the operation
            succeeds without uploading anything if the key already exists.
        
        Returns
        -------
        List[Tuple[str, str]]
            List of `(key, url)` pairs corresponding to the files uploaded.
        """
        ...
    ...

class Azure(object, metaclass=type):
    @classmethod
    def get_root_from_config(cls, echo, create_on_absent = True):
        ...
    def __init__(self):
        ...
    def __enter__(self):
        ...
    def __exit__(self, *args):
        ...
    def get(self, key = None, return_missing = False):
        """
        Key MUST be a fully qualified path with uri scheme.  azure://<container_name>/b/l/o/b/n/a/m/e
        """
        ...
    def put(self, key, obj, overwrite = True):
        """
        Key MUST be a fully qualified path.  <container_name>/b/l/o/b/n/a/m/e
        """
        ...
    def info(self, key = None, return_missing = False):
        ...
    ...

class GS(object, metaclass=type):
    @classmethod
    def get_root_from_config(cls, echo, create_on_absent = True):
        ...
    def __init__(self):
        ...
    def __enter__(self):
        ...
    def __exit__(self, *args):
        ...
    def get(self, key = None, return_missing = False):
        """
        Key MUST be a fully qualified path.  gs://<bucket_name>/b/l/o/b/n/a/m/e
        """
        ...
    def put(self, key, obj, overwrite = True):
        """
        Key MUST be a fully qualified path.  gs://<bucket_name>/b/l/o/b/n/a/m/e
        """
        ...
    def info(self, key = None, return_missing = False):
        ...
    ...

DATACLIENTS: dict

class IncludedFile(object, metaclass=type):
    def __init__(self, descriptor: typing.Dict[str, typing.Any]):
        ...
    @property
    def descriptor(self):
        ...
    @property
    def size(self):
        ...
    def decode(self, name, var_type = "Artifact"):
        ...
    ...

class FilePathClass(metaflow._vendor.click.types.ParamType, metaclass=type):
    def __init__(self, is_text, encoding):
        ...
    def convert(self, value, param, ctx):
        ...
    def __str__(self):
        ...
    def __repr__(self):
        ...
    ...

class IncludeFile(metaflow.parameters.Parameter, metaclass=type):
    """
    Includes a local file as a parameter for the flow.
    
    `IncludeFile` behaves like `Parameter` except that it reads its value from a file instead of
    the command line. The user provides a path to a file on the command line. The file contents
    are saved as a read-only artifact which is available in all steps of the flow.
    
    Parameters
    ----------
    name : str
        User-visible parameter name.
    default : Union[str, Callable[ParameterContext, str]]
        Default path to a local file. A function
        implies that the parameter corresponds to a *deploy-time parameter*.
    is_text : bool, default True
        Convert the file contents to a string using the provided `encoding`.
        If False, the artifact is stored in `bytes`.
    encoding : str, optional, default 'utf-8'
        Use this encoding to decode the file contexts if `is_text=True`.
    required : bool, default False
        Require that the user specified a value for the parameter.
        `required=True` implies that the `default` is not used.
    help : str, optional
        Help text to show in `run --help`.
    show_default : bool, default True
        If True, show the default value in the help text.
    """
    def __init__(self, name: str, required: bool = False, is_text: bool = True, encoding: str = "utf-8", help: typing.Optional[str] = None, **kwargs: typing.Dict[str, str]):
        ...
    def load_parameter(self, v):
        ...
    ...

class UploaderV1(object, metaclass=type):
    @classmethod
    def encode_url(cls, url_type, url, **kwargs):
        ...
    @classmethod
    def store(cls, flow_name, path, is_text, encoding, handler, echo):
        ...
    @classmethod
    def size(cls, descriptor):
        ...
    @classmethod
    def load(cls, descriptor):
        ...
    ...

class UploaderV2(object, metaclass=type):
    @classmethod
    def encode_url(cls, url_type, url, **kwargs):
        ...
    @classmethod
    def store(cls, flow_name, path, is_text, encoding, handler, echo):
        ...
    @classmethod
    def size(cls, descriptor):
        ...
    @classmethod
    def load(cls, descriptor):
        ...
    ...

UPLOADERS: dict

class CURRENT_UPLOADER(object, metaclass=type):
    @classmethod
    def encode_url(cls, url_type, url, **kwargs):
        ...
    @classmethod
    def store(cls, flow_name, path, is_text, encoding, handler, echo):
        ...
    @classmethod
    def size(cls, descriptor):
        ...
    @classmethod
    def load(cls, descriptor):
        ...
    ...

