def snake_to_camel(snake_str, upper_first=False):
    """
    Convert a snake_case string to a CamelCase string

    :param snake_str: The snake_case string to convert
    :param upper_first: Whether to capitalize the first letter
    """

    # Split the string into words at underscores
    components = snake_str.split("_")
    # Capitalize the first letter of each component except the first one
    # and join them together
    first = components[0].capitalize() if upper_first else components[0]
    return first + "".join(x.capitalize() for x in components[1:])
