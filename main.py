# import gradio


# def greet(name):
#     return "Hello " + name + "!"


# demo = gradio.Interface(
#     fn=greet, inputs="text", title='Hello from main', outputs="text"
# )
# demo.launch()

import subprocess

subprocess.run("python -m fastchat.serve.gradio_web_server", check=True, shell=True)

