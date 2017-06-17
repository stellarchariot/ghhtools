class GHHConfigError(Exception):
    """Exception raised for errors in the config.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message