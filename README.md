To run cli chat `python -m fastchat.serve.cli --model-path gpt2 --device cpu`

Architecture for FastChat:

Model 1--1> Worker(s) *--1> Controller <1--1 Gradio FE Server

To serve the controller `python -m fastchat.serve.controller`
To serve the worker node `python -m fastchat.serve.model_worker --model-path gpt2-medium --device cpu --host 0.0.0.0 --port 2007 --worker-address 0.0.0.0:2007`
