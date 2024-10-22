import gradio as gr
from gradio_neouploadbutton import NeoUploadButton


example = NeoUploadButton().example_value()

with gr.Blocks() as demo:
    button = NeoUploadButton(
        value=example, label="Load a file", loading_message="... Loading ..."
    )  # populated component
    button2 = NeoUploadButton(
        label="Charger un fichier", loading_message="... Chargement ..."
    )  # empty component

    file = gr.File()  # output component
    button.upload(fn=lambda x: x, inputs=button, outputs=file)
    button2.upload(fn=lambda x: x, inputs=button2, outputs=file)


if __name__ == "__main__":
    demo.launch()
