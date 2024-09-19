def introspection_info(obj):
    info = {'type': type(obj).__name__, 'attributes': [], 'methods': [], 'module': __name__}
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            info['methods'].append(attr)
        else:
            info['attributes'].append(attr)
    return info


number_info = introspection_info(42)
print(number_info)
