import config
import helpers
from jinja2 import Template
import os
from templates import (
    model_base_cpp_j2,
    model_base_h_j2,
    model_cpp_j2,
    model_h_j2,
    iobserver_h_j2,
)


def run(filename: str, output="."):
    """Generate C++ models based on configuration file"""
    helpers.set_config(config.load(filename))

    # CPP/HPP files for each model
    templates = {
        "base": {
            "files": {
                "cpp": Template(model_base_cpp_j2.TEMPLATE),
                "h": Template(model_base_h_j2.TEMPLATE),
            },
            "override": True,
            "suffix": "Base",
        },
        "custom": {
            "files": {
                "cpp": Template(model_cpp_j2.TEMPLATE),
                "h": Template(model_h_j2.TEMPLATE),
            },
            "override": False,
        },
    }

    for model in helpers.get_models():
        print(f"INFO: writing model {model['name']}")

        for type in templates.keys():
            for ext in templates[type]["files"].keys():
                fn = os.path.join(
                    output,
                    helpers.get_model_filename(
                        model["name"] + templates[type].get("suffix", "").capitalize(),
                        ext,
                    ),
                )
                print(f"      {fn}")
                if templates[type].get("override", False) or not os.path.exists(fn):
                    with open(fn, "w") as f:
                        f.write(templates[type]["files"][ext].render(model, h=helpers))

    print(f"INFO: writing supporting classes and headers")
    fn = os.path.join(
        output,
        helpers.get_model_filename(
            "Observer",
            "h",
        ),
    )
    print(f"      {fn}")
    with open(fn, "w") as f:
        f.write(Template(iobserver_h_j2.TEMPLATE).render(h=helpers))
