####################################################################################################
"""Helpers contains methods that can be used in a template"""
####################################################################################################

from dependencies.utils.src.names import snakecase, singular

# ---------------------------------------------------------------------------------------------------
# Config helpers
# ---------------------------------------------------------------------------------------------------

config = None


def set_config(_config):
    """Set the configuration used to generate code"""
    global config
    config = _config


def get_config():
    """Get the configuration used to generate code"""
    global config
    return config


# ---------------------------------------------------------------------------------------------------
# Filename helpers
# ---------------------------------------------------------------------------------------------------


def get_model_filename(name, ext):
    """Returns a filename based on the name and extension provided"""
    return f"{snakecase(get_prefixed_name(name))}.{ext}"


def get_header_filename(name):
    """Returns a header filename based on the name and extension provided"""
    return get_model_filename(name, "h")


def get_class_filename(name):
    """Returns a class filename based on the name and extension provided"""
    return get_model_filename(name, "cpp")


# ---------------------------------------------------------------------------------------------------
# Model helpers
# ---------------------------------------------------------------------------------------------------


def get_models():
    """Return a list of models"""
    return config.get("models", [])


def get_model(name):
    """Returns a model with the specified name, or None if not found"""
    return next((model for model in get_models() if model["name"] == name), None)


def get_model_names():
    """Returns a list of all model names (without prefix)"""
    return [model["name"] for model in get_models()]


def get_prefixed_model_names():
    """Returns a list of all model names (with prefix)"""
    return [get_prefixed_name(model["name"]) for model in get_models()]


def is_model(name):
    """Returns True if name is the name of a model, False if not"""
    return name in get_model_names()


def get_prefixed_name(name):
    """Return the model name including the prefix"""
    return get_setting("prefix") + name


def get_define_name(name):
    """Return the string used in the model header to stop reading the header file twice"""
    return f"_{get_prefixed_name(name)}_H_".upper()


def get_type(name, list=False, containment=False):
    """If name is the name of a model then return the prefixed name, or just return the specified name"""
    new_name = name

    if is_model(new_name):
        new_name = get_prefixed_name(new_name)
        new_name = f"shared_ptr<{new_name}>"

    if list:
        new_name = f"list<{new_name}>"

    return new_name


# ---------------------------------------------------------------------------------------------------
# Setting helpers
# ---------------------------------------------------------------------------------------------------


def get_settings():
    """Returns a list of settings"""
    return config.get("settings", {})


def get_setting(name):
    """Returns a setting with the specified name, or None if not found"""
    return get_settings().get(name, None)


# ---------------------------------------------------------------------------------------------------
# Attribute helpers
# ---------------------------------------------------------------------------------------------------


def get_model_includes(name):
    """Get a list of include filenames for all attribute types"""
    model = get_model(name)
    return [
        get_header_filename(attribute["type"])
        for attribute in model["attributes"]
        if is_model(attribute["type"])
    ]


def get_model_forwards(name):
    """Get a list of forwards for all attributes"""
    model = get_model(name)
    return [
        get_prefixed_name(attribute["type"])
        for attribute in model["attributes"]
        if is_model(attribute["type"])
    ]


def list_attributes(name):
    """Returns a list of attributes that have list: true"""
    model = get_model(name)
    return [
        attribute for attribute in model["attributes"] if attribute.get("list", False)
    ]


def has_a_list(name):
    """Returns True if the model has one or more list attributes, False if not"""
    return len(list_attributes(name))


def get_attribute_type(attribute):
    """Returns the type for the specified attribute"""
    return get_type(
        attribute["type"],
        list=attribute.get("list", False),
        containment=attribute.get("containment", False),
    )


def get_attribute_type_without_list(attribute):
    """Returns the type for the specified attribute"""
    return get_type(
        attribute["type"],
        list=False,
        containment=attribute.get("containment", False),
    )


def get_singular_attribute_name(attribute):
    return singular(attribute["name"])
