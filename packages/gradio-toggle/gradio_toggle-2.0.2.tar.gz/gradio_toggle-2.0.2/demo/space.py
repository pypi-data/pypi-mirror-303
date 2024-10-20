
import gradio as gr
from app import demo as app
import os

_docs = {'Toggle': {'description': 'Creates a checkbox that can be set to `True` or `False`. Can be used as an input to pass a boolean value to a function or as an output\nto display a boolean value.\n', 'members': {'__init__': {'value': {'type': 'bool | Callable', 'default': 'False', 'description': ''}, 'label': {'type': 'str | None', 'default': 'None', 'description': ''}, 'info': {'type': 'str | None', 'default': 'None', 'description': ''}, 'color': {'type': 'str | Callable | None', 'default': 'None', 'description': ''}, 'radius': {'type': 'Literal["sm", "lg"]', 'default': '"lg"', 'description': ''}, 'transition': {'type': 'float', 'default': '0.3', 'description': ''}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': ''}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': None}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': ''}, 'container': {'type': 'bool', 'default': 'True', 'description': ''}, 'scale': {'type': 'int | None', 'default': 'None', 'description': ''}, 'min_width': {'type': 'int', 'default': '160', 'description': ''}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': ''}, 'visible': {'type': 'bool', 'default': 'True', 'description': ''}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': ''}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': ''}, 'render': {'type': 'bool', 'default': 'True', 'description': ''}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': ''}}, 'postprocess': {'value': {'type': 'bool | None', 'description': 'The toggle state to be returned.'}}, 'preprocess': {'return': {'type': 'bool | None', 'description': 'The toggle state as a boolean value.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the Toggle changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the Toggle.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the Toggle. Uses event data gradio.SelectData to carry `value` referring to the label of the Toggle, and `selected` to refer to state of the Toggle. See EventData documentation on how to use this event data'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'Toggle': []}}}

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
# `gradio_toggle`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_toggle/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_toggle"></a>  
</div>

A custom Gradio component that toggles between on and off states.
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_toggle
```

## Usage

```python
# Toggle - A Gradio Custom Component
# Created by Daniel Ialcin Misser Westergaard
# https://huggingface.co/dwancin
# https://github.com/dwancin
# (c) 2024

import gradio as gr
from gradio_toggle import Toggle

def update_toggle_state(input_component):
    print(f"Updating toggle: {input_component}")
    return input_component

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            input_component = Toggle()
        with gr.Column():
            output_component = Toggle(color="red", info="this is the output", show_label=False, interactive=False, radius="sm", transition=1)

    input_component.change(fn=update_toggle_state, inputs=input_component, outputs=output_component)

if __name__ == '__main__':
    demo.launch()
```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `Toggle`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["Toggle"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["Toggle"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, the toggle state as a boolean value.
- **As output:** Should return, the toggle state to be returned.

 ```python
def predict(
    value: bool | None
) -> bool | None:
    return value
```
""", elem_classes=["md-custom", "Toggle-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          Toggle: [], };
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
