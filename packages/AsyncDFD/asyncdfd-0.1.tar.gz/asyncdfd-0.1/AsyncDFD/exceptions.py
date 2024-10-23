class IllegalArgumentError(Exception):
    def __init__(self, data, func) -> None:
        super().__init__(f"IllegalArgumentError in function {func}: {data}")


class NodeProcessingError(Exception):
    def __init__(self, data, func, error, stack) -> None:
        super().__init__(
            f"NodeProcessingError in function {func.__name__}: {data}, Error type {error}\n {stack}"
        )
        self.data = data
        self.func_name = func.__name__
        self.origin_error = error
        self.stack = stack
