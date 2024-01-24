class ServerError(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.name = "ServerError"
        self.message = message
