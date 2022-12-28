import config
import helpers
from jinja2 import Template
import os
from templates import model_base_cpp_j2, model_base_h_j2, model_cpp_j2, model_h_j2


def run(filename: str, output="."):
    """Generate C++ models based on configuration file"""
    helpers.set_config(config.load(filename))

    # CPP/HPP files for each model
    templates = {
        "base": {
            "cpp": Template(model_base_cpp_j2.TEMPLATE),
            "h": Template(model_base_h_j2.TEMPLATE),
        },
        "custom": {
            "cpp": Template(model_cpp_j2.TEMPLATE),
            "h": Template(model_h_j2.TEMPLATE),
        },
    }

    for model in helpers.get_models():
        print(f"INFO: writing model {model['name']}")

        # Always write base files
        for ext in templates["base"].keys():
            fn = os.path.join(
                output, helpers.get_model_filename(model["name"] + "Base", ext)
            )
            with open(fn, "w") as f:
                f.write(templates["base"][ext].render(model, h=helpers))

        # Only write custom files if they don't exist
        for ext in templates["custom"].keys():
            fn = os.path.join(output, helpers.get_model_filename(model["name"], ext))
            if not os.path.exists(fn):
                with open(fn, "w") as f:
                    f.write(templates["custom"][ext].render(model, h=helpers))
