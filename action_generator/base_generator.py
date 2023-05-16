import abc


class BaseGenerator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate(self, query: str, stop_tokens=None, max_output_len=None):
        pass
