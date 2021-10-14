import os

root_path = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir)
)
input_path = os.path.abspath(os.path.join(root_path, "input"))
output_path = os.path.abspath(os.path.join(root_path, "output"))
