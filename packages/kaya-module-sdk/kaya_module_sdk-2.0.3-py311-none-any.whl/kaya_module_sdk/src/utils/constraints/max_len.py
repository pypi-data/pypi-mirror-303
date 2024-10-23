def kmaxlen(max_len_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args)-1 > max_len_value:
                raise ValueError(
                    f"Composite type length should not be above {max_len_value}"
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator
