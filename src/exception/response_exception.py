class ResponseException(Exception):
    access_token: str
    status_code: int
    message: str
    content: dict

    def __init__(self, status_code: int, message: str, content: dict, access_token: str = "", ):
        self.access_token = access_token
        self.status_code = status_code
        self.message = message
        self.content = content
