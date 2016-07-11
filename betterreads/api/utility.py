def pluralize(singular):
    if singular.endswith('y'):
        return singular[:-1] + 'ies'
    return singular + 's'
