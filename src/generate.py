from . import config
from . import helpers
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

template_env = Environment(
    loader=FileSystemLoader(f"{os.path.dirname(__file__)}/templates/"),
    autoescape=select_autoescape(),
)


def run(filename: str, output="."):
    """Generate C++ models based on configuration file"""
    helpers.set_config(config.load(filename))

    # CPP/HPP files for each model
    templates = {
        "cpp": template_env.get_template("model.cpp.j2"),
        "h": template_env.get_template("model.h.j2"),
    }

    for model in helpers.get_models():
        for ext in templates.keys():
            fn = os.path.join(output, helpers.get_model_filename(model["name"], ext))
            with open(fn, "w") as f:
                f.write(templates[ext].render(model, h=helpers))
