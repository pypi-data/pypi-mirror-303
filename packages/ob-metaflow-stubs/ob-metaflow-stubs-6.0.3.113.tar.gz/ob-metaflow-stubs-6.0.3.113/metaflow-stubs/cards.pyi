##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.387703                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.plugins.cards.card_modules.basic
    import metaflow
    import metaflow.plugins.cards.card_modules.card
    import metaflow.plugins.cards.card_modules.components
    import typing
    import metaflow.plugins.cards.card_client

def get_cards(task: typing.Union[str, "metaflow.Task"], id: typing.Optional[str] = None, type: typing.Optional[str] = None, follow_resumed: bool = True) -> metaflow.plugins.cards.card_client.CardContainer:
    """
    Get cards related to a `Task`.
    
    Note that `get_cards` resolves the cards contained by the task, but it doesn't actually
    retrieve them from the datastore. Actual card contents are retrieved lazily either when
    the card is rendered in a notebook to when you call `Card.get`. This means that
    `get_cards` is a fast call even when individual cards contain a lot of data.
    
    Parameters
    ----------
    task : Union[str, `Task`]
        A `Task` object or pathspec `{flow_name}/{run_id}/{step_name}/{task_id}` that
        uniquely identifies a task.
    id : str, optional, default None
        The ID of card to retrieve if multiple cards are present.
    type : str, optional, default None
        The type of card to retrieve if multiple cards are present.
    follow_resumed : bool, default True
        If the task has been resumed, then setting this flag will resolve the card for
        the origin task.
    
    Returns
    -------
    CardContainer
        A list-like object that holds `Card` objects.
    """
    ...

class MetaflowCardComponent(object, metaclass=type):
    @property
    def component_id(self):
        ...
    @component_id.setter
    def component_id(self, value):
        ...
    def update(self, *args, **kwargs):
        """
        #FIXME document
        """
        ...
    def render(self):
        """
        `render` returns a string or dictionary. This class can be called on the client side to dynamically add components to the `MetaflowCard`
        """
        ...
    ...

class MetaflowCard(object, metaclass=type):
    """
    Metaflow cards derive from this base class.
    
    Subclasses of this class are called *card types*. The desired card
    type `T` is defined in the `@card` decorator as `@card(type=T)`.
    
    After a task with `@card(type=T, options=S)` finishes executing, Metaflow instantiates
    a subclass `C` of `MetaflowCard` that has its `type` attribute set to `T`, i.e. `C.type=T`.
    The constructor is given the options dictionary `S` that contains arbitrary
    JSON-encodable data that is passed to the instance, parametrizing the card. The subclass
    may override the constructor to capture and process the options.
    
    The subclass needs to implement a `render(task)` method that produces the card
    contents in HTML, given the finished task that is represented by a `Task` object.
    
    Attributes
    ----------
    type : str
        Card type string. Note that this should be a globally unique name, similar to a
        Python package name, to avoid name clashes between different custom cards.
    
    Parameters
    ----------
    options : Dict
        JSON-encodable dictionary containing user-definable options for the class.
    """
    def __init__(self, options = {}, components = [], graph = None):
        ...
    def render(self, task: "metaflow.Task") -> str:
        """
        Produce custom card contents in HTML.
        
        Subclasses override this method to customize the card contents.
        
        Parameters
        ----------
        task : Task
            A `Task` object that allows you to access data from the finished task and tasks
            preceding it.
        
        Returns
        -------
        str
            Card contents as an HTML string.
        """
        ...
    def render_runtime(self, task, data):
        ...
    def refresh(self, task, data):
        ...
    def reload_content_token(self, task, data):
        ...
    ...

class Artifact(metaflow.plugins.cards.card_modules.components.UserComponent, metaclass=type):
    """
    A pretty-printed version of any Python object.
    
    Large objects are truncated using Python's built-in [`reprlib`](https://docs.python.org/3/library/reprlib.html).
    
    Example:
    ```
    from datetime import datetime
    current.card.append(Artifact({'now': datetime.utcnow()}))
    ```
    
    Parameters
    ----------
    artifact : object
        Any Python object.
    name : str, optional
        Optional label for the object.
    compressed : bool, default: True
        Use a truncated representation.
    """
    def update(self, artifact):
        ...
    def __init__(self, artifact: typing.Any, name: typing.Optional[str] = None, compressed: bool = True):
        ...
    def render(self, *args, **kwargs):
        ...
    ...

class Table(metaflow.plugins.cards.card_modules.components.UserComponent, metaclass=type):
    """
    A table.
    
    The contents of the table can be text or numerical data, a Pandas dataframe,
    or other card components: `Artifact`, `Image`, `Markdown` objects.
    
    Example: Text and artifacts
    ```
    from metaflow.cards import Table, Artifact
    current.card.append(
        Table([
            ['first row', Artifact({'a': 2})],
            ['second row', Artifact(3)]
        ])
    )
    ```
    
    Example: Table from a Pandas dataframe
    ```
    from metaflow.cards import Table
    import pandas as pd
    import numpy as np
    current.card.append(
        Table.from_dataframe(
            pd.DataFrame(
                np.random.randint(0, 100, size=(15, 4)),
                columns=list("ABCD")
            )
        )
    )
    ```
    
    Parameters
    ----------
    data : List[List[str or MetaflowCardComponent]], optional
        List (rows) of lists (columns). Each item can be a string or a `MetaflowCardComponent`.
    headers : List[str], optional
        Optional header row for the table.
    """
    def update(self, *args, **kwargs):
        ...
    def __init__(self, data: typing.Optional[typing.List[typing.List[typing.Union[str, metaflow.plugins.cards.card_modules.card.MetaflowCardComponent]]]] = None, headers: typing.Optional[typing.List[str]] = None, disable_updates: bool = False):
        ...
    @classmethod
    def from_dataframe(cls, dataframe = None, truncate: bool = True):
        """
        Create a `Table` based on a Pandas dataframe.
        
        Parameters
        ----------
        dataframe : Optional[pandas.DataFrame]
            Pandas dataframe.
        truncate : bool, default: True
            Truncate large dataframe instead of showing all rows (default: True).
        """
        ...
    def render(self, *args, **kwargs):
        ...
    ...

class Image(metaflow.plugins.cards.card_modules.components.UserComponent, metaclass=type):
    """
    An image.
    
    `Images can be created directly from PNG/JPG/GIF `bytes`, `PIL.Image`s,
    or Matplotlib figures. Note that the image data is embedded in the card,
    so no external files are required to show the image.
    
    Example: Create an `Image` from bytes:
    ```
    current.card.append(
        Image(
            requests.get("https://www.gif-vif.com/hacker-cat.gif").content,
            "Image From Bytes"
        )
    )
    ```
    
    Example: Create an `Image` from a Matplotlib figure
    ```
    import pandas as pd
    import numpy as np
    current.card.append(
        Image.from_matplotlib(
            pandas.DataFrame(
                np.random.randint(0, 100, size=(15, 4)),
                columns=list("ABCD"),
            ).plot()
        )
    )
    ```
    
    Example: Create an `Image` from a [PIL](https://pillow.readthedocs.io/) Image
    ```
    from PIL import Image as PILImage
    current.card.append(
        Image.from_pil_image(
            PILImage.fromarray(np.random.randn(1024, 768), "RGB"),
            "From PIL Image"
        )
    )
    ```
    
    Parameters
    ----------
    src : bytes
        The image data in `bytes`.
    label : str
        Optional label for the image.
    """
    @staticmethod
    def render_fail_headline(msg):
        ...
    def __init__(self, src = None, label = None, disable_updates: bool = True):
        ...
    @classmethod
    def from_pil_image(cls, pilimage, label: typing.Optional[str] = None, disable_updates: bool = False):
        """
        Create an `Image` from a PIL image.
        
        Parameters
        ----------
        pilimage : PIL.Image
            a PIL image object.
        label : str, optional
            Optional label for the image.
        """
        ...
    @classmethod
    def from_matplotlib(cls, plot, label: typing.Optional[str] = None, disable_updates: bool = False):
        """
        Create an `Image` from a Matplotlib plot.
        
        Parameters
        ----------
        plot :  matplotlib.figure.Figure or matplotlib.axes.Axes or matplotlib.axes._subplots.AxesSubplot
            a PIL axes (plot) object.
        label : str, optional
            Optional label for the image.
        """
        ...
    def render(self, *args, **kwargs):
        ...
    def update(self, image, label = None):
        """
        Update the image.
        
        Parameters
        ----------
        image : PIL.Image or matplotlib.figure.Figure or matplotlib.axes.Axes or matplotlib.axes._subplots.AxesSubplot or bytes or str
            The updated image object
        label : str, optional
            Optional label for the image.
        """
        ...
    ...

class Error(metaflow.plugins.cards.card_modules.components.UserComponent, metaclass=type):
    """
    This class helps visualize Error's on the `MetaflowCard`. It can help catch and print stack traces to errors that happen in `@step` code.
    
    ### Parameters
    - `exception` (Exception) : The `Exception` to visualize. This value will be `repr`'d before passed down to `MetaflowCard`
    - `title` (str) : The title that will appear over the visualized  `Exception`.
    
    ### Usage
    ```python
    @card
    @step
    def my_step(self):
        from metaflow.cards import Error
        from metaflow import current
        try:
            ...
            ...
        except Exception as e:
            current.card.append(
                Error(e,"Something misbehaved")
            )
        ...
    ```
    """
    def __init__(self, exception, title = None):
        ...
    def render(self, *args, **kwargs):
        ...
    ...

class Markdown(metaflow.plugins.cards.card_modules.components.UserComponent, metaclass=type):
    """
    A block of text formatted in Markdown.
    
    Example:
    ```
    current.card.append(
        Markdown("# This is a header appended from `@step` code")
    )
    ```
    
    Parameters
    ----------
    text : str
        Text formatted in Markdown.
    """
    def update(self, text = None):
        ...
    def __init__(self, text = None):
        ...
    def render(self, *args, **kwargs):
        ...
    ...

class VegaChart(metaflow.plugins.cards.card_modules.components.UserComponent, metaclass=type):
    def __init__(self, spec: dict, show_controls: bool = False):
        ...
    def update(self, spec = None):
        """
        Update the chart.
        
        Parameters
        ----------
        spec : dict or altair.Chart
            The updated chart spec or an altair Chart Object.
        """
        ...
    @classmethod
    def from_altair_chart(cls, altair_chart):
        ...
    def render(self, *args, **kwargs):
        ...
    ...

class ProgressBar(metaflow.plugins.cards.card_modules.components.UserComponent, metaclass=type):
    """
    A Progress bar for tracking progress of any task.
    
    Example:
    ```
    progress_bar = ProgressBar(
        max=100,
        label="Progress Bar",
        value=0,
        unit="%",
        metadata="0.1 items/s"
    )
    current.card.append(
        progress_bar
    )
    for i in range(100):
        progress_bar.update(i, metadata="%s items/s" % i)
    
    ```
    
    Parameters
    ----------
    max : int
        The maximum value of the progress bar.
    label : str, optional
        Optional label for the progress bar.
    value : int, optional
        Optional initial value of the progress bar.
    unit : str, optional
        Optional unit for the progress bar.
    metadata : str, optional
        Optional additional information to show on the progress bar.
    """
    def __init__(self, max: int = 100, label: str = None, value: int = 0, unit: str = None, metadata: str = None):
        ...
    def update(self, new_value: int, metadata: str = None):
        ...
    def render(self, *args, **kwargs):
        ...
    ...

class DefaultCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {"only_repr": True}, components = [], graph = None):
        ...
    def render(self, task, runtime = False):
        ...
    def render_runtime(self, task, data):
        ...
    def refresh(self, task, data):
        ...
    def reload_content_token(self, task, data):
        """
        The reload token will change when the component array has changed in the Metaflow card.
        The change in the component array is signified by the change in the component_update_ts.
        """
        ...
    ...

class PageComponent(metaflow.plugins.cards.card_modules.basic.DefaultComponent, metaclass=type):
    def __init__(self, title = None, subtitle = None, contents = []):
        ...
    def render(self):
        ...
    ...

class ErrorCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {}, components = [], graph = None):
        ...
    def reload_content_token(self, task, data):
        """
        The reload token will change when the component array has changed in the Metaflow card.
        The change in the component array is signified by the change in the component_update_ts.
        """
        ...
    def render(self, task, stack_trace = None):
        ...
    ...

class BlankCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {"title": ""}, components = [], graph = None):
        ...
    def render(self, task, components = [], runtime = False):
        ...
    def render_runtime(self, task, data):
        ...
    def refresh(self, task, data):
        ...
    def reload_content_token(self, task, data):
        """
        The reload token will change when the component array has changed in the Metaflow card.
        The change in the component array is signified by the change in the component_update_ts.
        """
        ...
    ...

