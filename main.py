import gradio as gr
import numpy as np
from clearml.binding.gradio_bind import PatchGradio
import clearml
import argparse
import gradio.routes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ClearML Gradio arguments")
    parser.add_argument("--some_string_param", type=str)
    parser.add_argument("--some_int_param", type=int)
    args = parser.parse_args()
    print("String param:", args.some_string_param, type(args.some_string_param))
    print("Int param:", args.some_int_param, type(args.some_int_param))

    clearml.Task.init()
    task = clearml.Task.current_task()


    print(clearml.__version__)
    print(PatchGradio._current_task)


    def image_generator(text):
        return np.random.randint(0, 255, size=(244, 244, 3))


    with gr.Blocks() as demo:
        button = gr.Button(label="Generate Image")
        button.click(fn=image_generator, inputs=gr.Textbox(), outputs=gr.Image())

    demo.queue(concurrency_count=3)
    demo.launch(server_name="0.0.0.0")  #, root_path=f"/service/{task.id}")
