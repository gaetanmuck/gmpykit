def print_object(obj, heading="", key=""):
    """Print out an object with indentation."""

    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, bool):
        print(heading + key + ": " + str(obj))

    elif isinstance(obj, list):
        for i, elt in enumerate(obj):
            print(heading + key + " " + str(i) + ": ")
            print_object(elt, heading + "    ")

    elif isinstance(obj, dict):
        for key, value in obj.items():
            print_object(heading=heading, key=key, obj=value)

    elif obj:
        print_object(obj.__dict__, heading)
