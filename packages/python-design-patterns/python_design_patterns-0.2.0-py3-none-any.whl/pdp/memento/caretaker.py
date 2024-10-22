""" Module to implement the caretaker class for the memento pattern."""

import json
from typing import List
from pdp.memento.base_originator import BaseOriginator
from pdp.memento.memento import Memento


class Caretaker:
    """Class to manage mementos for an originator."""

    def __init__(self, originator: BaseOriginator, max_states: int = -1):
        """Initialize the caretaker.

        :param originator: The originator to manage mementos for.
        :type originator: BaseOriginator
        :param max_states: The maximum number of states to store -1 = no limit, defaults to -1
        :type max_states: int, optional
        """
        self._originator = originator
        self._history: List[Memento] = []
        self._current_index = -1
        self.max_states = max_states

    def _check_max_states(self):
        """Check if the maximum number of states has been reached."""
        if self.max_states != -1 and len(self._history) > self.max_states:
            self._history.pop(0)
            self._current_index -= 1

    def save(self):
        """Save the current state of the originator."""
        self._history.append(self._originator.save_state())
        self._current_index = len(self._history) - 1
        self._check_max_states()

    def restore(self, index: int):
        """Restore the originator to a previous state."""
        if 0 <= index < len(self._history):
            self._originator.restore_state(self._history[index])
            self._current_index = index
        else:
            raise ValueError("Index out of range")

    def undo(self):
        """Undo the last operation."""
        if self._current_index >= 0:
            self._originator.restore_state(self._history[self._current_index])

    def save_to_file(self, filename: str):
        """Save the mementos to a file."""
        history_states = [memento.get_state() for memento in self._history]
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(history_states, file)

    def load_from_file(self, filename: str):
        """Load mementos from a file."""
        with open(filename, "r", encoding="utf-8") as file:
            history_states = json.load(file)
        self._history = [Memento(state) for state in history_states]
        self._current_index = len(self._history) - 1
        self._originator.restore_state(self._history[self._current_index])
        self._check_max_states()
