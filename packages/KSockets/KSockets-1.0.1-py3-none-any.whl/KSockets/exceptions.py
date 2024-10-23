class SocketException(BaseException):
    "General Socket Exception"
    def __init__(self, message, property, *args, **kwargs):
        self.message=message
        self.property=property
        super().__init__(message,*args,**kwargs)
    
class client_protocol_mismatch(SocketException):
    "The server protocol does not follow the steps that the client knows"
    def __init__(self, message, property, *args, **kwargs):
        super().__init__(message, property, *args, **kwargs)

class decode_error(SocketException):
    "The message type is incorrect from what was declared"
    def __init__(self, message, property, *args, **kwargs):
        super().__init__(message, property, *args, **kwargs)

class ReconnectionFailure(SocketException):
    "Failure to reconnect"
    def __init__(self, message, property, *args, **kwargs):
        super().__init__(message, property, *args, **kwargs)

class NotReadyError(SocketException):
    "The server/client is not ready for use or has not been properly initialized"
    def __init__(self, message, property, *args, **kwargs):
        super().__init__(message, property, *args, **kwargs)