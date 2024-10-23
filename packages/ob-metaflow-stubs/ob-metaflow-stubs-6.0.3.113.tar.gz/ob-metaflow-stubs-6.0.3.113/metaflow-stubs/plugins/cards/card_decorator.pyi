##################################################################################
#                       Auto-generated Metaflow stub file                        #
# MF version: 2.12.25.2+obcheckpoint(0.1.1);ob(v1)                               #
# Generated on 2024-10-22T22:37:22.434996                                        #
##################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import metaflow.metaflow_current
    import metaflow.decorators

current: metaflow.metaflow_current.Current

class CardComponentCollector(object, metaclass=type):
    """
    This class helps collect `MetaflowCardComponent`s during runtime execution
    
    ### Usage with `current`
    `current.card` is of type `CardComponentCollector`
    
    ### Main Usage TLDR
    - [x] `current.card.append` customizes the default editable card.
    - [x] Only one card can be default editable in a step.
    - [x] The card class must have `ALLOW_USER_COMPONENTS=True` to be considered default editable.
        - [x] Classes with `ALLOW_USER_COMPONENTS=False` are never default editable.
    - [x] The user can specify an `id` argument to a card, in which case the card is editable through `current.card[id].append`.
        - [x] A card with an id can be also default editable, if there are no other cards that are eligible to be default editable.
    - [x] If multiple default-editable cards exist but only one card doesn't have an id, the card without an id is considered to be default editable.
    - [x] If we can't resolve a single default editable card through the above rules, `current.card`.append calls show a warning but the call doesn't fail.
    - [x] A card that is not default editable can be still edited through:
        - [x] its `current.card['myid']`
        - [x] by looking it up by its type, e.g. `current.card.get(type='pytorch')`.
    """
    def __init__(self, logger = None, card_creator = None):
        ...
    @staticmethod
    def create_uuid():
        ...
    def get(self, type = None):
        """
        `get`
        gets all the components arrays for a card `type`.
        Since one `@step` can have many `@card` decorators, many decorators can have the same type. That is why this function returns a list of lists.
        
        Args:
            type ([str], optional): `type` of MetaflowCard. Defaults to None.
        
        Returns: will return empty `list` if `type` is None or not found
            List[List[MetaflowCardComponent]]
        """
        ...
    def __getitem__(self, key):
        """
        Choose a specific card for manipulation.
        
        When multiple @card decorators are present, you can add an
        `ID` to distinguish between them, `@card(id=ID)`. This allows you
        to add components to a specific card like this:
        ```
        current.card[ID].append(component)
        ```
        
        Parameters
        ----------
        key : str
            Card ID.
        
        Returns
        -------
        CardComponentManager
            An object with `append` and `extend` calls which allow you to
            add components to the chosen card.
        """
        ...
    def __setitem__(self, key, value):
        """
        Specify components of the chosen card.
        
        Instead of adding components to a card individually with `current.card[ID].append(component)`,
        use this method to assign a list of components to a card, replacing the existing components:
        ```
        current.card[ID] = [FirstComponent, SecondComponent]
        ```
        
        Parameters
        ----------
        key: str
            Card ID.
        
        value: List[MetaflowCardComponent]
            List of card components to assign to this card.
        """
        ...
    def append(self, component, id = None):
        """
        Appends a component to the current card.
        
        Parameters
        ----------
        component : MetaflowCardComponent
            Card component to add to this card.
        """
        ...
    def extend(self, components):
        """
        Appends many components to the current card.
        
        Parameters
        ----------
        component : Iterator[MetaflowCardComponent]
            Card components to add to this card.
        """
        ...
    @property
    def components(self):
        ...
    def clear(self):
        ...
    def refresh(self, *args, **kwargs):
        ...
    ...

def get_card_class(card_type):
    ...

class CardCreator(object, metaclass=type):
    def __init__(self, top_level_options):
        ...
    def create(self, card_uuid = None, user_set_card_id = None, runtime_card = False, decorator_attributes = None, card_options = None, logger = None, mode = "render", final = False, sync = False):
        ...
    ...

TYPE_CHECK_REGEX: str

ASYNC_TIMEOUT: int

def warning_message(message, logger = None, ts = False):
    ...

class CardDecorator(metaflow.decorators.StepDecorator, metaclass=type):
    """
    Creates a human-readable report, a Metaflow Card, after this step completes.
    
    Note that you may add multiple `@card` decorators in a step with different parameters.
    
    Parameters
    ----------
    type : str, default 'default'
        Card type.
    id : str, optional, default None
        If multiple cards are present, use this id to identify this card.
    options : Dict[str, Any], default {}
        Options passed to the card. The contents depend on the card type.
    timeout : int, default 45
        Interrupt reporting if it takes more than this many seconds.
    
    MF Add To Current
    -----------------
    card -> metaflow.plugins.cards.component_serializer.CardComponentCollector
        The `@card` decorator makes the cards available through the `current.card`
        object. If multiple `@card` decorators are present, you can add an `ID` to
        distinguish between them using `@card(id=ID)` as the decorator. You will then
        be able to access that specific card using `current.card[ID].
    
        Methods available are `append` and `extend`
    
        @@ Returns
        -------
        CardComponentCollector
            The or one of the cards attached to this step.
    """
    def __init__(self, *args, **kwargs):
        ...
    def step_init(self, flow, graph, step_name, decorators, environment, flow_datastore, logger):
        ...
    def task_pre_step(self, step_name, task_datastore, metadata, run_id, task_id, flow, graph, retry_count, max_user_code_retries, ubf_context, inputs):
        ...
    def task_finished(self, step_name, flow, graph, is_task_ok, retry_count, max_user_code_retries):
        ...
    ...

