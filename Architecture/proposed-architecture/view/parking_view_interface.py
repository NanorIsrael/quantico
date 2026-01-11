from abc import ABC, abstractmethod
from typing import Iterable


class ParkingViewInterface(ABC):

    @abstractmethod
    def render(self, message: str) -> None:
        pass

    @abstractmethod
    def render_lines(self, lines: Iterable[str]) -> None:
        pass

    @abstractmethod
    def render_error(self, message: str) -> None:
        pass
