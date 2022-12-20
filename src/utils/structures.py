def merge(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            merge(value, destination.setdefault(key, {}))
        else:
            destination[key] = value
    return destination
