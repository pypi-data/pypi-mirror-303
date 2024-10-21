import ujson


def transfer_to_dict(data: dict | str):
    if isinstance(data, dict):
        return data
    if isinstance(data, list):
        return data
    if  not data:
        return None
    return ujson.loads(data)