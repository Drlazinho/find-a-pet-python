class HttpUnprocessableEntityError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.status_code = 422
        self.namme = "UnprocessableEntity"
        self.message = message
