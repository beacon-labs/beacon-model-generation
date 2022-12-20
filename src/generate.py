from . import config
from . import helpers
from jinja2 import Template
import os
from .templates import model_cpp_j2, model_h_j2


def run(filename: str, output="."):
    """Generate C++ models based on configuration file"""
    helpers.set_config(config.load(filename))

    # CPP/HPP files for each model
    templates = {
        "cpp": Template(model_cpp_j2.TEMPLATE),
        "h": Template(model_h_j2.TEMPLATE),
    }

    for model in helpers.get_models():
        for ext in templates.keys():
            fn = os.path.join(output, helpers.get_model_filename(model["name"], ext))
            with open(fn, "w") as f:
                f.write(templates[ext].render(model, h=helpers))
