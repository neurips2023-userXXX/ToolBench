import abc
from typing import List


class BaseEvaluator(metaclass=abc.ABCMeta):
    def __init__(self, generator):
        # a list of dictionaries
        self.full_results = []

        # the action generator
        self.generator = generator

    def get_action(
        self, query: str, stop_tokens: List = None, max_output_len: int = None
    ):
        prompt, prediction, error = self.generator.generate(
            query, stop_tokens, max_output_len
        )
        return prompt, prediction, error

    @abc.abstractmethod
    def __call__(self, query: str, labels: List[str]):
        pass

    @abc.abstractmethod
    def aggregate_results(self):
        raise NotImplementedError
