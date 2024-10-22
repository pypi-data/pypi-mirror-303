""" This module contains the PipelineError class. """


class PipelineError(Exception):
    """
    Exception raised when an error occurs in the pipeline.
    """

    def __init__(self, step_name: str, original_exception: Exception) -> None:
        self.step_name = step_name
        self.original_exception = "original_exception"
        self.message = f"Error occurred in <{step_name}> : {original_exception}"
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
