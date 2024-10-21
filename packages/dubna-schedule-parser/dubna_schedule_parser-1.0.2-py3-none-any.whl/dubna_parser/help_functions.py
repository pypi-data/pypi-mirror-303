def join_dicts(dict1: dict, dict2: dict) -> dict:
    if (not dict1) and (not dict2):
        return dict()
    if not dict1:
        return dict2
    if not dict2:
        return dict1

    merged_dict = {}
    for key, values in dict1.items():
        merged_dict[key] = values.copy()

    for key, values in dict2.items():
        if key in merged_dict:
            merged_dict[key].extend(values)
        else:
            merged_dict[key] = values

    for key in merged_dict:
        merged_dict[key] = list(set(merged_dict[key]))
    return merged_dict
