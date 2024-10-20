import gradio as gr
from gradio_neouploadbutton import NeoUploadButton


example = NeoUploadButton().example_value()

with gr.Blocks() as demo:
    button = NeoUploadButton(
        value=example, label="Load a file", loading_message="... Loading ..."
    )  # populated component

    file = gr.File()  # output component
    button.upload(fn=lambda x: x, inputs=button, outputs=file)


if __name__ == "__main__":
    demo.launch()
