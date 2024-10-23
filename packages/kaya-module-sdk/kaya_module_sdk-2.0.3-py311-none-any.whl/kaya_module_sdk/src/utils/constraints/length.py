def klen(len_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len_value:
                raise ValueError(
                    f"Composite type length should be equal to {len_value}"
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator
