import gradio as gr
from gradio_modal_component import modal_component


def display_image(img):
    return img


def get_blur_value(selected_blur):
    return selected_blur


def show_modal_with_dimensions(width, height):
    # Convert inputs to integers with default values if empty or invalid
    try:
        width = int(width) if width else None
        height = int(height) if height else None
    except ValueError:
        width = None
        height = None

    return modal_component(visible=True, width=width, height=height)


def show_modal_with_dimensions_and_percentage(
    width_input8, height_input8, width_percent8, height_percent8
):
    # Convert inputs to integers with default values if empty or invalid
    try:
        width = int(width_input8) if width_input8 else None
        height = int(height_input8) if height_input8 else None
        width_percent = int(width_percent8) if width_percent8 else None
        height_percent = int(height_percent8) if height_percent8 else None
    except ValueError:
        width = None
        height = None

    return modal_component(
        visible=True,
        width=width,
        height=height,
        content_width_percent=width_percent,
        content_height_percent=height_percent,
    )


with gr.Blocks() as demo:
    gr.Markdown("# Image Modal Demonstration")

    with gr.Tab("Tab 1"):
        # MODAL 1
        gr.Markdown(
            """
        - Fixed close icon (X) is overlapped by the image. or big components.

        """
        )
        show_btn = gr.Button("Show Modal")

        # MODAL 2
        gr.Markdown(
            """
        - Enable the `display_close_icon` parameter to allow the user to close the modal by clicking outside, clicking the X, or pressing the escape key. In this case `display_close_icon = False` (Modal 1 is true), If not set defaults to `True`.
        - Enale the `esc_close` parameter to allow the user to close the modal by pressing the escape key.
        """
        )
        show_btn2 = gr.Button("Show Modal 2")

        # MODAL 3
        gr.Markdown(
            """
        - Enale the `close_outer_click` parameter to allow the user to close the modal by click on the blur. Defaults to `True`, in this case `close_outer_click = False`.
        """
        )
        show_btn3 = gr.Button("Show Modal 3")

        # MODAL 4
        gr.Markdown(
            """
        - Enable the `close_message` parameter to show a message when the user tries to close the modal.
        - The close message dialog can be customized using `close_message_style` to modify button text, colors, and background.
        """
        )
        with gr.Row():
            show_btn4 = gr.Button("Show Modal 4 (Default Style)")
            show_btn4_custom = gr.Button("Show Modal 4 (Custom Style)")

        # MODAL 5
        gr.Markdown(
            """
        - Handle Z-index.
        """
        )

        show_btn5 = gr.Button("Show Modal 5")

        # MODAL 6
        gr.Markdown(
            """
        - Add `bg_blur` option to dynamically change the background blur of the modal.
        """
        )
        with gr.Row():
            # Dropdown for selecting blur level
            blur_level = gr.Dropdown(
                [0, 4, 8, 12, 16],
                label="Blur Level",
                value=4,  # Default value
                interactive=True,
            )
            opacity_level = gr.Dropdown(
                [0, 0.1, 0.2, 0.3, 0.4, 0.5],
                label="Opacity Level",
                value=0.4,  # Default value
                interactive=True,
            )

        show_btn6 = gr.Button("Show Modal 6")

        # MODAL 7
        gr.Markdown(
            """
        - Add `width` and `height` option to dynamically change the size of the modal (Mesure in pixels.)
        """
        )

        with gr.Row():
            width_input = gr.Textbox(
                label="Width", placeholder="Enter width", value="1000"
            )
            height_input = gr.Textbox(
                label="Height", placeholder="Enter height", value="500"
            )

        show_btn7 = gr.Button("Show Modal 7")

        # MODAL 8
        gr.Markdown(
            """
        - Add `content_width_percent` and `content_height_percent` option to dynamically change the size of the modal.
        - **Please note that if the content height is higher than the modal height, the modal will scroll. That why you can see the ratio correctly.**
        """
        )
        with gr.Row():
            width_input8 = gr.Textbox(
                label="Width (px)", placeholder="Enter width", value="1000"
            )
            height_input8 = gr.Textbox(
                label="Height (px)", placeholder="Enter height", value="500"
            )
            width_percent8 = gr.Textbox(
                label="Width percent (%)", placeholder="Enter width", value="50"
            )
            height_percent8 = gr.Textbox(
                label="Height percent (%)", placeholder="Enter height", value="80"
            )

        show_btn8 = gr.Button("Show Modal 8")

        # MODAL 9
        gr.Markdown(
            """
        - Add `content_padding` configuration to control the spacing around modal content
        - Padding can be specified using CSS-style values (e.g., "100px 50px" for vertical/horizontal padding)
        - Please modify `content_padding` in the code to see the changes. current value is `100px`
        """
        )

        with gr.Row():
            width_input9 = gr.Textbox(
                label="Width", placeholder="Enter width", value="1000"
            )
            height_input9 = gr.Textbox(
                label="Height", placeholder="Enter height", value="500"
            )

        show_btn9 = gr.Button("Show Modal 9")

        # MODAL 10
        gr.Markdown(
            """
        - Add `content_padding` configuration to control the spacing around modal content
        - Padding can be specified using CSS-style values (e.g., "100px 50px" for vertical/horizontal padding)
        - Please modify `content_padding` in the code to see the changes. current value is `100px`
        - Add `animate` default = `None`; `animate_duration` default = `0.4` option to show the modal with animation
        """
        )

        show_btn10 = gr.Button("Show Modal 10")

    # MODAL lIST

    with modal_component(visible=False, display_close_icon=True) as modal:
        gr.Image(
            "https://images.unsplash.com/photo-1612178537253-bccd437b730e",
            label="Random Image",
        )

    with modal_component(
        visible=False, display_close_icon=False, close_on_esc=True
    ) as modal2:
        with gr.Column():
            upload_img = gr.Image(label="Upload Image", type="pil")
            display_btn = gr.Button("Display Image")
            output_img = gr.Image(label="Displayed Image")
        display_btn.click(fn=display_image, inputs=upload_img, outputs=output_img)

    with modal_component(visible=False, close_outer_click=False) as modal3:
        with gr.Column():
            upload_img = gr.Image(label="Upload Image", type="pil")
            display_btn = gr.Button("Display Image")
            output_img = gr.Image(label="Displayed Image")
        display_btn.click(fn=display_image, inputs=upload_img, outputs=output_img)

    # Original Modal 4 with default styling
    with modal_component(
        visible=False,
        close_outer_click=True,
        close_message="Are you sure you want to close?",
    ) as modal4:
        with gr.Column():
            upload_img = gr.Image(label="Upload Image", type="pil")
            display_btn = gr.Button("Display Image")
            output_img = gr.Image(label="Displayed Image")
        display_btn.click(fn=display_image, inputs=upload_img, outputs=output_img)

    # New Modal 4 with custom styling
    with modal_component(
        visible=False,
        close_outer_click=True,
        close_message="Do you want to discard your changes?",
        close_message_style={
            "message_color": "#000000",  # Black text
            "confirm_text": "Discard",
            "cancel_text": "Keep Editing",
            "confirm_bg_color": "#DC2626",  # Red color
            "cancel_bg_color": "#059669",  # Green color
            "confirm_text_color": "#FFFFFF",  # White text
            "cancel_text_color": "#FFFFFF",  # White text
            "modal_bg_color": "#F3F4F6",  # Light gray background
            "confirm_border_color": None,
            "cancel_border_color": None,
            # "height": "100px",
            # "width": "200px",
            "size": "lg", # "lg | sm"
        },
    ) as modal4_custom:
        with gr.Column():
            upload_img = gr.Image(label="Upload Image", type="pil")
            display_btn = gr.Button("Display Image")
            output_img = gr.Image(label="Displayed Image")
        display_btn.click(fn=display_image, inputs=upload_img, outputs=output_img)

    with modal_component(visible=False, close_outer_click=True) as modal5:
        with modal_component(
            visible=False,
            close_outer_click=True,
            close_message="Are you sure want to close ?",
        ) as modal51:
            with gr.Column():
                upload_img = gr.Image(label="Upload Image", type="pil")
                display_btn = gr.Button("Display Image")
                output_img = gr.Image(label="Displayed Image")
            display_btn.click(fn=display_image, inputs=upload_img, outputs=output_img)

        gr.Markdown(
            """
        # Handling Z-index for Modal
        """
        )

        show_btn51 = gr.Button("Show Sub Modal 5")

    with modal_component(visible=False) as modal6:
        gr.Markdown(
            f"""
            # View Background Blur and Opacity Level
            """
        )

    with modal_component(visible=False) as modal7:
        gr.Markdown("# Custom Sized Modal")
        with gr.Column():
            gr.Markdown("This modal demonstrates custom width and height settings.")
            gr.Image(
                "https://images.unsplash.com/photo-1612178537253-bccd437b730e",
                label="Sample Image with Custom Dimensions",
            )

    with modal_component(
        visible=False,
        content_width_percent=50,
        content_height_percent=10,
        width=1000,
        height=500,
    ) as modal8:
        gr.Markdown("# Custom Sized Modal")
        with gr.Column():
            gr.Markdown("This modal demonstrates custom width and height settings.")
            upload_img = gr.Image(label="Upload Image", type="pil")
            display_btn = gr.Button("Display Image")
            output_img = gr.Image(label="Displayed Image")
        display_btn.click(fn=display_image, inputs=upload_img, outputs=output_img)

    # Modal 9 with custom padding
    # Padding can be specified using CSS padding format: e.g. '100px' or '100px 50px' or '100px 50px 100px 50px'
    # Padding values refer to "Top Right Bottom Left"
    with modal_component(
        visible=False, width=1000, height=500, content_padding="100px"
    ) as modal9:
        gr.Markdown("# Padded Modal Example")
        with gr.Column():
            gr.Markdown(
                """
            This modal demonstrates custom padding settings.
            - The content is centered with configurable padding
            - Padding can be adjusted dynamically
            - Supports different padding values for each side
            """
            )
            upload_img = gr.Image(label="Upload Image", type="pil")
            display_btn = gr.Button("Display Image")
            output_img = gr.Image(label="Displayed Image")
        display_btn.click(fn=display_image, inputs=upload_img, outputs=output_img)

    with modal_component(
        visible=False, width=500, height=200, opacity_level=0, bg_blur=0,
        animate="Left",
        animation_duration=0.5,
    ) as modal10:
        gr.Markdown(
            """# Opacity level Modal Example

                    - Modal 10 Example
                    - Opacity level set to 0
                    - Background blur set to 0
                    """
        )

    show_btn.click(lambda: modal_component(visible=True), None, modal)
    show_btn2.click(lambda: modal_component(visible=True), None, modal2)
    show_btn3.click(lambda: modal_component(visible=True), None, modal3)

    show_btn4.click(lambda: modal_component(visible=True), None, modal4)
    show_btn4_custom.click(lambda: modal_component(visible=True), None, modal4_custom)

    show_btn5.click(lambda: modal_component(visible=True), None, modal5)
    show_btn51.click(lambda: modal_component(visible=True), None, modal51)

    show_btn6.click(
        lambda blur, opacity: modal_component(
            visible=True, bg_blur=blur, opacity_level=opacity
        ),
        inputs=[blur_level, opacity_level],
        outputs=modal6,
    )

    show_btn7.click(
        fn=show_modal_with_dimensions,
        inputs=[width_input, height_input],
        outputs=modal7,
    )

    show_btn8.click(
        fn=show_modal_with_dimensions_and_percentage,
        inputs=[width_input8, height_input8, width_percent8, height_percent8],
        outputs=modal8,
    )

    show_btn9.click(lambda: modal_component(visible=True), None, modal9)
    show_btn10.click(lambda: modal_component(visible=True), None, modal10)


if __name__ == "__main__":
    demo.launch()
