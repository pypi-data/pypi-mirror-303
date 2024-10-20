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