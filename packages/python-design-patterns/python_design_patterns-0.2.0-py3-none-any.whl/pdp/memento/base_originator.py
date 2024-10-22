""" Base originator class for the memento pattern. """

from abc import ABC, abstractmethod
import copy

from pdp.memento.memento import Memento


class BaseOriginator(ABC):
    """Base class for originators in the memento pattern."""

    @abstractmethod
    def get_state(self) -> dict:
        """Get the current state of the originator."""
        raise NotImplementedError

    @abstractmethod
    def set_state(self, state: dict):
        """Set the state of the originator."""
        raise NotImplementedError

    def save_state(self) -> Memento:
        """Save the current state of the originator."""
        return Memento(copy.deepcopy(self.get_state()))

    def restore_state(self, memento: Memento):
        """Restore the state of the originator."""
        self.set_state(copy.deepcopy(memento.get_state()))
