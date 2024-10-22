""" Memento """

from datetime import datetime


class Memento:
    """Class to store the state of an originator."""

    def __init__(self, state: dict):
        if state is None:
            state = {}
        if not isinstance(state, dict):
            raise TypeError("state must be a dict")
        self._state = state
        self._timestamp = datetime.now()

    def get_state(self) -> dict:
        """Get the state of the memento."""
        return self._state

    def get_timestamp(self) -> datetime:
        """Get the creation time of the memento."""
        return self._timestamp

    def __eq__(self, other):
        return self._state == other._state

    def __str__(self) -> str:
        return f"Memento(timestamp={self._timestamp}, state={self._state})"
