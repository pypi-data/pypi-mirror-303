##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.409089                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.plugins.cards.card_modules.basic
    import metaflow.plugins.cards.card_modules.components
    import metaflow.plugins.cards.card_modules.card
    import typing

class LogComponent(metaflow.plugins.cards.card_modules.basic.DefaultComponent, metaclass=type):
    def __init__(self, data = None):
        ...
    def render(self):
        ...
    ...

class ErrorComponent(metaflow.plugins.cards.card_modules.card.MetaflowCardComponent, metaclass=type):
    def __init__(self, headline, error_message):
        ...
    def render(self):
        ...
    ...

class ArtifactsComponent(metaflow.plugins.cards.card_modules.basic.DefaultComponent, metaclass=type):
    def __init__(self, title = None, subtitle = None, data = {}):
        ...
    def render(self):
        ...
    ...

class TableComponent(metaflow.plugins.cards.card_modules.basic.DefaultComponent, metaclass=type):
    def __init__(self, title = None, subtitle = None, headers = [], data = [[]], vertical = False):
        ...
    @classmethod
    def validate(cls, headers, data):
        ...
    def render(self):
        ...
    ...

class ImageComponent(metaflow.plugins.cards.card_modules.basic.DefaultComponent, metaclass=type):
    def __init__(self, src = None, label = None, title = None, subtitle = None):
        ...
    def render(self):
        ...
    ...

class SectionComponent(metaflow.plugins.cards.card_modules.basic.DefaultComponent, metaclass=type):
    def __init__(self, title = None, subtitle = None, columns = None, contents = []):
        ...
    @classmethod
    def render_subcomponents(cls, component_array, additional_allowed_types = [str, dict], allow_unknowns = False):
        ...
    def render(self):
        ...
    ...

class MarkdownComponent(metaflow.plugins.cards.card_modules.basic.DefaultComponent, metaclass=type):
    def __init__(self, text = None):
        ...
    def render(self):
        ...
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

class TaskToDict(object, metaclass=type):
    def __init__(self, only_repr = False, runtime = False):
        ...
    def __call__(self, task, graph = None):
        ...
    def object_type(self, object):
        ...
    def parse_image(self, data_object):
        ...
    def infer_object(self, artifact_object):
        ...
    ...

def render_safely(func):
    """
    This is a decorator that can be added to any `MetaflowCardComponent.render`
    The goal is to render subcomponents safely and ensure that they are JSON serializable.
    """
    ...

def create_component_id(component):
    ...

def with_default_component_id(func):
    ...

class UserComponent(metaflow.plugins.cards.card_modules.card.MetaflowCardComponent, metaclass=type):
    def update(self, *args, **kwargs):
        ...
    ...

class StubComponent(UserComponent, metaclass=type):
    def __init__(self, component_id):
        ...
    def update(self, *args, **kwargs):
        ...
    ...

class Artifact(UserComponent, metaclass=type):
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

class Table(UserComponent, metaclass=type):
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

class Image(UserComponent, metaclass=type):
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

class Error(UserComponent, metaclass=type):
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

class Markdown(UserComponent, metaclass=type):
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

class ProgressBar(UserComponent, metaclass=type):
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

class VegaChart(UserComponent, metaclass=type):
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

