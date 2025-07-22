class SubprocessError(RuntimeError):
    """Custom error for subprocess execution failures."""

    def __init__(self, message, completed_process):
        super().__init__(message)
        self.completed_process = completed_process
