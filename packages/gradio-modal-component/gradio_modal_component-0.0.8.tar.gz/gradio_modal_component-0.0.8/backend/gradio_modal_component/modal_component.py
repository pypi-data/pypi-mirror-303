from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Union, Literal

from gradio.blocks import BlockContext
from gradio.component_meta import ComponentMeta
from gradio.events import Events
from gradio.context import Context

AnimationType = Literal[
    "Zoom In",
    "Top",
    "Bottom",
    "Left",
    "Right",
    "Fade In",
    None
]

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
    confirm_border_color: str | None = None
    cancel_border_color: str | None = None
    height: str = "auto"
    width: str = "auto"
    size: str = "lg"

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