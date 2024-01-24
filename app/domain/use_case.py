from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Optional

from infra.utils.either import Either, left, right

Input = TypeVar("Input")
Output = TypeVar("Output")
Error = Exception


class UseCase(ABC, Generic[Input, Output]):

    @abstractmethod
    def execute(self, input: Optional[Input] = None) -> Output:
        pass

    def perform(self, input: Optional[Input] = None) -> Either[Error, Output]:
        try:
            output = self.execute(input)
            return right(output)
        except Exception as error:
            return left(error)
