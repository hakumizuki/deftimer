class TimerError(Exception):
    def __init__(self, expression=None, message=None):
        self.expression = expression
        self.message = message

    def __str__(self):
        return f'{self.expression} --> {self.message}'


class TimerActionError(TimerError):
    pass
