def flatten_dict(dict_obj: dict, parent_key='', sep='.'):
    """Flattens a nested dictionary.

    :param dict_obj: The dictionary to flatten.
    :param parent_key: The base key string (used for recursion).
    :param sep: The separator between keys in the flattened dictionary.
    :return: A flattened dictionary.
    """
    items = []

    for k, v in dict_obj.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))

    return dict(items)
