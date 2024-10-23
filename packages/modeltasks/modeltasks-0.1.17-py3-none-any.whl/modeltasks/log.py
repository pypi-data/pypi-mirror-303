from logging import getLogger, LoggerAdapter


logger = getLogger('modeltasks')


class TaskLogger(LoggerAdapter):
    """
    A logging adapter used within model task execution
    """

    def process(self, message, kwargs):
        return f'''Task "{self.extra}": {message}''', kwargs
