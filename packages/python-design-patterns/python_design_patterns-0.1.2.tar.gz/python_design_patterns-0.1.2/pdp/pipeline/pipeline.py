""" Pipeline class for the pipeline module """

from typing import Any, Dict, List, Union

from pdp.pipeline.pipeline_error import PipelineError

from .step import Step


class Pipeline:
    """Pipeline class for the pipeline module"""

    def __init__(self, steps: List[Step] = None) -> None:
        self.steps: List[Step] = steps if self._validate_steps(steps) else []

        self.data: Dict[str, Any] = {}

    def _validate_steps(self, steps: Union[Step, List[Step]]) -> bool:
        """Validate the steps

        :param steps: the steps to validate
        :type steps: Union[Step, List[Step]]

        :return: whether the steps are valid
        :rtype: bool
        """
        if not isinstance(steps, list):
            steps = [steps]

        for step in steps:
            if not isinstance(step, Step):
                return False
        return True

    def add_step(self, step: Step) -> None:
        """Add a step to the pipeline

        :param step: the step to add
        :type step: Step

        :raises ValueError: if the step is not a valid Step object
        """
        if self._validate_steps(step):
            self.steps.append(step)
        else:
            raise ValueError("step is not a valid Step object")

    def run(self, **kwargs: Any) -> Any:
        """Run the pipeline with the given keyword arguments

        :param kwargs: keyword arguments
        :type kwargs: Any

        :return: the result of the pipeline
        :rtype: Any
        """
        self.data = kwargs
        for step in self.steps:
            func_args = step.get_args()
            filtered_args = {k: v for k, v in self.data.items() if k in func_args}

            try:
                result = step(**filtered_args)
            except Exception as e:
                raise PipelineError(step.name, e) from e

            self.data[step.name] = result

        return self.data
