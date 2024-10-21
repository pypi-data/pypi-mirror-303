def safe_list_get(l_, *, idx=0, default=None):
    """get element from list safely"""
    try:
        if not isinstance(l_, list):
            raise TypeError
        return l_[idx]
    except (IndexError, TypeError):
        return default


def safe_list_index(l_, element, default=None):
    """get index of element from list safely"""
    try:
        if not isinstance(l_, list):
            raise TypeError
        return l_.index(element)
    except (ValueError, TypeError):
        return default
