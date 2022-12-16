from . import config
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

template_env = Environment(
    loader=FileSystemLoader(f"{os.path.dirname(__file__)}/templates/"),
    autoescape=select_autoescape(),
)


def run(filename: str, output="."):
    """Generate C++ models based on configuration file"""
    c = config.load(filename)

    # CPP files for each model
    template = template_env.get_template("model.cpp.j2")
    for model in c["models"]:
        model_fn = os.path.join(output, f"{model['name']}.cpp")
        with open(model_fn, "w") as f:
            f.write(template.render(model))
