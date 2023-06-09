import gradio as gr
import numpy as np
from clearml.binding.gradio_bind import PatchGradio

print(PatchGradio._current_task)


def image_generator(text):
    return np.random.randint(0, 255, size=(244, 244, 3))


with gr.Blocks() as demo:
    button = gr.Button(label="Generate Image")
    button.click(fn=image_generator, inputs=gr.Textbox(), outputs=gr.Image())

demo.queue(concurrency_count=3)
demo.launch(server_name="0.0.0.0") # , root_path=f"/service/{task.id}")

