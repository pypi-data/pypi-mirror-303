
import gradio as gr
from app import demo as app
import os

_docs = {'NeoUploadButton': {'description': 'Used to create an upload button, when clicked allows a user to upload files that satisfy the specified file type or generic files (if file_type not set).\n', 'members': {'__init__': {'label': {'type': 'str', 'default': '"Upload a File"', 'description': 'Text to display on the button. Defaults to "Upload a File".'}, 'value': {'type': 'str | list[str] | Callable | None', 'default': 'None', 'description': 'File or list of files to upload by default.'}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': 'Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.'}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': 'Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.'}, 'variant': {'type': 'Literal["primary", "secondary", "stop"]', 'default': '"secondary"', 'description': "'primary' for main call-to-action, 'secondary' for a more subdued style, 'stop' for a stop button."}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'size': {'type': 'Literal["sm", "lg"] | None', 'default': 'None', 'description': 'Size of the button. Can be "sm" or "lg".'}, 'icon': {'type': 'str | None', 'default': 'None', 'description': 'URL or path to the icon file to display within the button. If None, no icon will be displayed.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int | None', 'default': 'None', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool', 'default': 'True', 'description': 'If False, the NeoUploadButton will be in a disabled state.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': 'if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.'}, 'type': {'type': 'Literal["filepath", "bytes"]', 'default': '"filepath"', 'description': 'Type of value to be returned by component. "file" returns a temporary file object with the same base name as the uploaded file, whose full path can be retrieved by file_obj.name, "binary" returns an bytes object.'}, 'file_count': {'type': 'Literal["single", "multiple", "directory"]', 'default': '"single"', 'description': 'if single, allows user to upload one file. If "multiple", user uploads multiple files. If "directory", user uploads all files in selected directory. Return type will be list for each file in case of "multiple" or "directory".'}, 'file_types': {'type': 'list[str] | None', 'default': 'None', 'description': 'List of type of files to be uploaded. "file" allows any file to be uploaded, "image" allows only image files to be uploaded, "audio" allows only audio files to be uploaded, "video" allows only video files to be uploaded, "text" allows only text files to be uploaded.'}, 'loading_message': {'type': 'str | None', 'default': 'None', 'description': None}}, 'postprocess': {'value': {'type': 'str | list[str] | None', 'description': 'Expects a `str` filepath or URL, or a `list[str]` of filepaths/URLs.'}}, 'preprocess': {'return': {'type': 'bytes | str | list[bytes] | list[str] | None', 'description': 'Passes the file as a `str` or `bytes` object, or a list of `str` or list of `bytes` objects, depending on `type` and `file_count`.'}, 'value': None}}, 'events': {'click': {'type': None, 'default': None, 'description': 'Triggered when the NeoUploadButton is clicked.'}, 'upload': {'type': None, 'default': None, 'description': 'This listener is triggered when the user uploads a file into the NeoUploadButton.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'NeoUploadButton': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_neouploadbutton`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_neouploadbutton/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_neouploadbutton"></a>  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_neouploadbutton
```

## Usage

```python
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

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `NeoUploadButton`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["NeoUploadButton"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["NeoUploadButton"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes the file as a `str` or `bytes` object, or a list of `str` or list of `bytes` objects, depending on `type` and `file_count`.
- **As output:** Should return, expects a `str` filepath or URL, or a `list[str]` of filepaths/URLs.

 ```python
def predict(
    value: bytes | str | list[bytes] | list[str] | None
) -> str | list[str] | None:
    return value
```
""", elem_classes=["md-custom", "NeoUploadButton-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          NeoUploadButton: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
