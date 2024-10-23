from __future__ import annotations

from gradio_client.documentation import document, set_documentation_group
from typing import Dict, Union

from dataclasses import dataclass
from gradio.blocks import BlockContext
from gradio.context import Context
from gradio.component_meta import ComponentMeta
from gradio.events import Events

set_documentation_group("layout")

@dataclass
class CloseMessageStyle:
    """Configuration for modal close confirmation styling."""
    message_color: str = "var(--neutral-700)"
    confirm_text: str = "Yes"
    cancel_text: str = "No"
    confirm_bg_color: str = "var(--primary-500)"
    cancel_bg_color: str = "var(--neutral-500)"
    confirm_text_color: str = "white"
    cancel_text_color: str = "white"
    modal_bg_color: str = "var(--background-fill-primary)"
from gradio.events import Dependency

@document()
class modal_component(BlockContext, metaclass=ComponentMeta):
    """A modal component with customizable animations."""

    EVENTS = [Events.blur]

    def __init__(
        self,
        *,
        visible: bool = False,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        display_close_icon: bool = True,
        render: bool = True,
        close_on_esc: bool = True,
        close_outer_click: bool = True,
        close_message: str | None = None,
        close_message_style: Union[Dict, CloseMessageStyle] | None = None,
        bg_blur: int | None = 4,
        width: int | None = None,
        height: int | None = None,
        content_width_percent: int | None = None,
        content_height_percent: int | None = None,
        content_padding: str | None = None,
        opacity_level: float = 0.4,
        animate: AnimationType = None,
        animation_duration: float = 0.4,
    ):
        """
        Parameters:
            visible: If False, modal will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional string or list of strings that are assigned as the class of this component in the HTML DOM. Can be used for targeting CSS styles.
            allow_user_close: If True, user can close the modal (by clicking outside, clicking the X, or the escape key).
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            close_on_esc: If True, allows closing the modal with the escape key. Defaults to True.
            close_outer_click: If True, allows closing the modal by clicking outside. Defaults to True.
            close_message: The message to show when the user tries to close the modal. Defaults to None.
            CloseMessageStyle: Configuration for modal close confirmation styling.
                message_color: str = "var(--neutral-700)"
                confirm_text: str = "Yes"
                cancel_text: str = "No"
                confirm_bg_color: str = "var(--primary-500)"
                cancel_bg_color: str = "var(--neutral-500)"
                confirm_text_color: str = "white"
                cancel_text_color: str = "white"
                modal_bg_color: str = "var(--background-fill-primary)"
                confirm_border_color: str | None = None
                cancel_border_color: str | None = None
                height: str = "auto"
                width: str = "auto"
                size: The size of the modal. Defaults to "lg". This could be "sm" or "lg".
            bg_blur: The percentage of background blur. Should be a float between 0 and 1. Defaults to None.
            width: Modify the width of the modal.
            height: Modify the height of the modal.
            content_width_percent: Modify the width of the modal content as a percentage of the screen width.
            content_height_percent: Modify the height of the modal content as a percentage of the screen height.
            content_padding: Modify the padding of the modal content.
            opacity_level: The level of background blur. Should be an integer between 0 and 1. Defaults to 0.4.
            animate: The animation to use when the modal open. Defaults to None.
            animation_duration: The duration of the animation in seconds. Defaults to 0.4.

        """
        self.display_close_icon = display_close_icon
        self.close_on_esc = close_on_esc
        self.close_outer_click = close_outer_click
        self.close_message = close_message
        self.animation_duration = animation_duration

        if close_message_style is None:
            self.close_message_style = CloseMessageStyle()
        elif isinstance(close_message_style, dict):
            self.close_message_style = CloseMessageStyle(**close_message_style)
        else:
            self.close_message_style = close_message_style

        self.bg_blur = bg_blur
        self.width = width
        self.height = height
        self.content_width_percent = content_width_percent
        self.content_height_percent = content_height_percent
        self.content_padding = content_padding
        self.opacity_level = opacity_level
        self.animate = animate

        BlockContext.__init__(
            self,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
        )

        if Context.root_block:
            self.blur(
                None,
                None,
                self,
                js="""
                () => {
                    return {
                        "__type__": "update",
                        "visible": false
                    }
                }
                """
            )
    from typing import Callable, Literal, Sequence, Any, TYPE_CHECKING
    from gradio.blocks import Block
    if TYPE_CHECKING:
        from gradio.components import Timer

    
    def blur(self,
        fn: Callable[..., Any] | None = None,
        inputs: Block | Sequence[Block] | set[Block] | None = None,
        outputs: Block | Sequence[Block] | None = None,
        api_name: str | None | Literal[False] = None,
        scroll_to_output: bool = False,
        show_progress: Literal["full", "minimal", "hidden"] = "full",
        queue: bool | None = None,
        batch: bool = False,
        max_batch_size: int = 4,
        preprocess: bool = True,
        postprocess: bool = True,
        cancels: dict[str, Any] | list[dict[str, Any]] | None = None,
        every: Timer | float | None = None,
        trigger_mode: Literal["once", "multiple", "always_last"] | None = None,
        js: str | None = None,
        concurrency_limit: int | None | Literal["default"] = "default",
        concurrency_id: str | None = None,
        show_api: bool = True) -> Dependency:
        """
        Parameters:
            fn: the function to call when this event is triggered. Often a machine learning model's prediction function. Each parameter of the function corresponds to one input component, and the function should return a single value or a tuple of values, with each element in the tuple corresponding to one output component.
            inputs: list of gradio.components to use as inputs. If the function takes no inputs, this should be an empty list.
            outputs: list of gradio.components to use as outputs. If the function returns no outputs, this should be an empty list.
            api_name: defines how the endpoint appears in the API docs. Can be a string, None, or False. If False, the endpoint will not be exposed in the api docs. If set to None, the endpoint will be exposed in the api docs as an unnamed endpoint, although this behavior will be changed in Gradio 4.0. If set to a string, the endpoint will be exposed in the api docs with the given name.
            scroll_to_output: if True, will scroll to output component on completion
            show_progress: how to show the progress animation while event is running: "full" shows a spinner which covers the output component area as well as a runtime display in the upper right corner, "minimal" only shows the runtime display, "hidden" shows no progress animation at all
            queue: if True, will place the request on the queue, if the queue has been enabled. If False, will not put this event on the queue, even if the queue has been enabled. If None, will use the queue setting of the gradio app.
            batch: if True, then the function should process a batch of inputs, meaning that it should accept a list of input values for each parameter. The lists should be of equal length (and be up to length `max_batch_size`). The function is then *required* to return a tuple of lists (even if there is only 1 output component), with each list in the tuple corresponding to one output component.
            max_batch_size: maximum number of inputs to batch together if this is called from the queue (only relevant if batch=True)
            preprocess: if False, will not run preprocessing of component data before running 'fn' (e.g. leaving it as a base64 string if this method is called with the `Image` component).
            postprocess: if False, will not run postprocessing of component data before returning 'fn' output to the browser.
            cancels: a list of other events to cancel when this listener is triggered. For example, setting cancels=[click_event] will cancel the click_event, where click_event is the return value of another components .click method. Functions that have not yet run (or generators that are iterating) will be cancelled, but functions that are currently running will be allowed to finish.
            every: continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.
            trigger_mode: if "once" (default for all events except `.change()`) would not allow any submissions while an event is pending. If set to "multiple", unlimited submissions are allowed while pending, and "always_last" (default for `.change()` and `.key_up()` events) would allow a second submission after the pending event is complete.
            js: optional frontend js method to run before running 'fn'. Input arguments for js method are values of 'inputs' and 'outputs', return should be a list of values for output components.
            concurrency_limit: if set, this is the maximum number of this event that can be running simultaneously. Can be set to None to mean no concurrency_limit (any number of this event can be running simultaneously). Set to "default" to use the default concurrency limit (defined by the `default_concurrency_limit` parameter in `Blocks.queue()`, which itself is 1 by default).
            concurrency_id: if set, this is the id of the concurrency group. Events with the same concurrency_id will be limited by the lowest set concurrency_limit.
            show_api: whether to show this event in the "view API" page of the Gradio app, or in the ".view_api()" method of the Gradio clients. Unlike setting api_name to False, setting show_api to False will still allow downstream apps as well as the Clients to use this event. If fn is None, show_api will automatically be set to False.
        """
        ...