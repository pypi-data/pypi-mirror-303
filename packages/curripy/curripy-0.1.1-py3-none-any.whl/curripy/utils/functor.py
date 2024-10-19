from ast import TypeVar
from typing import Callable, Generic, Self
from abc import ABCMeta, abstractmethod
from ..__generics import ParamTCov

class Functor(ABCMeta):
    @abstractmethod
    def fmap(self, f: Callable): ...

class Maybe(Functor):
    def __init__(self, x):
        self.x = x
        return 