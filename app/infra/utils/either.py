from typing import TypeVar, Generic

L = TypeVar('L')
A = TypeVar('A')


class Either(Generic[L, A]):
    pass


class Left(Either[L, A]):
    def __init__(self, value: L):
        self.value = value

    def is_left(self) -> bool:
        return True

    def is_right(self) -> bool:
        return False


class Right(Either[L, A]):
    def __init__(self, value: A):
        self.value = value

    def is_left(self) -> bool:
        return False

    def is_right(self) -> bool:
        return True


def left(l: L) -> Either[L, A]:
    return Left(l)


def right(a: A) -> Either[L, A]:
    return Right(a)
