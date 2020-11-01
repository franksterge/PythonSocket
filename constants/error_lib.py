class InternalException(Exception):
    """
    : Class that wraps an error exception to return to HTTP clients.
    """
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """
        : returns the dictionary representation of this error.
        """
        response_dict = dict(self.payload or ())
        response_dict['message'] = self.message
        response_dict['error'] = True
        return response_dict
