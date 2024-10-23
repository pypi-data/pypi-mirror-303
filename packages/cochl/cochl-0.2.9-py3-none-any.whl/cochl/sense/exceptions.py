class CochlSenseException(BaseException):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message} Please contact support@cochl.ai"


# TODO: need to rename to TimeoutException, it's using same name as built-in type TimeoutError(OSError)
class TimeOutError(BaseException):
    def __init__(self, session_id: str, timeout: float):
        super().__init__()
        self.session_id = session_id
        self.timeout = timeout

    def __str__(self):
        return f"Prediction (session_id={self.session_id}) has timed out '{self.timeout}s'"
