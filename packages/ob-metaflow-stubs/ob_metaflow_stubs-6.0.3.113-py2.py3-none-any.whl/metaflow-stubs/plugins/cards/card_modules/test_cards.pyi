##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.425291                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow
    import metaflow.plugins.cards.card_modules.card

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

def render_safely(func):
    """
    This is a decorator that can be added to any `MetaflowCardComponent.render`
    The goal is to render subcomponents safely and ensure that they are JSON serializable.
    """
    ...

class TestStringComponent(metaflow.plugins.cards.card_modules.card.MetaflowCardComponent, metaclass=type):
    def __init__(self, text):
        ...
    def render(self):
        ...
    def update(self, text):
        ...
    ...

class TestPathSpecCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def render(self, task):
        ...
    ...

class TestEditableCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {}, components = [], graph = None):
        ...
    def render(self, task):
        ...
    ...

class TestEditableCard2(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {}, components = [], graph = None):
        ...
    def render(self, task):
        ...
    ...

class TestNonEditableCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {}, components = [], graph = None):
        ...
    def render(self, task):
        ...
    ...

class TestMockCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {"key": "dummy_key"}, **kwargs):
        ...
    def render(self, task):
        ...
    ...

class TestErrorCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def render(self, task):
        ...
    ...

class TestTimeoutCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    def __init__(self, options = {"timeout": 50}, **kwargs):
        ...
    def render(self, task):
        ...
    ...

REFRESHABLE_HTML_TEMPLATE: str

class TestJSONComponent(metaflow.plugins.cards.card_modules.card.MetaflowCardComponent, metaclass=type):
    def __init__(self, data):
        ...
    def render(self, *args, **kwargs):
        ...
    def update(self, data):
        ...
    ...

class TestRefreshCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    """
    This card takes no components and helps test the `current.card.refresh(data)` interface.
    """
    def render(self, task) -> str:
        ...
    def render_runtime(self, task, data):
        ...
    def refresh(self, task, data):
        ...
    ...

class TestRefreshComponentCard(metaflow.plugins.cards.card_modules.card.MetaflowCard, metaclass=type):
    """
    This card takes components and helps test the `current.card.components["A"].update()`
    interface
    """
    def __init__(self, options = {}, components = [], graph = None):
        ...
    def render(self, task) -> str:
        ...
    def render_runtime(self, task, data):
        ...
    def refresh(self, task, data):
        ...
    def reload_content_token(self, task, data):
        ...
    ...

