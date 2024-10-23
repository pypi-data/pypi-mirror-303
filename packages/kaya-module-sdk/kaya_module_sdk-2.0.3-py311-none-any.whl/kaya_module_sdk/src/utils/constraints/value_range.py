def krange(range_min_value, range_max_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg_value in args:
                if isinstance(arg_value, (int, float)) and (
                    arg_value < range_min_value or arg_value > range_max_value
                ):
                    raise ValueError(
                        f"Value should be in the {range_min_value}-{range_max_value} range"
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator
