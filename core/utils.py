
def error_as_dict(error_dict):
    result = {}
    for field in error_dict:
        result[field] = []
        for message in error_dict[field]:
            result[field].append(message)

    return result
