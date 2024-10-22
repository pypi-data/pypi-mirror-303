# "from ... import ..." does not work here because of a circular dependency
# between nxlib.api and this module's classes.

import nxlib

__all__ = ["NxLibError", "NxLibException"]


class NxLibError(Exception):
    """
    This class represents an NxLib API error.

    Args:
        message (str, optional): The error messgae to be displayed.
            Defaults to None.
    """
    def __init__(self, message=None):
        self._message = message

    def __str__(self):
        return self._message


class NxLibException(NxLibError):
    """
    This class encapsulates NxLib API errors. All methods of
    :class:`~nxlib.item.NxLibItem` and :class:`~nxlib.command.NxLibCommand` not
    taking a return code pointer will throw an NxLibException when the API
    return code indicates an error.

    It is possible to store the ``NxLibCommand`` object that caused the
    exception to keep temporary slots alive while an exception exists.

    Args:
        path (str): The path to the NxLibItem that caused the exception.
        error_code (int): The NxLib error code.
        command (``NxLibCommand``, optional): The command object that cause the
            exception. Defaults to None.
    """
    def __init__(self, path, error_code, command=None):
        self._path = path
        self._error_code = error_code
        # Save command object in the exception to keep temporary slots alive
        # while an exception exists.
        self._command = command

    def get_error_code(self):
        """
        Retrieves the API return code that has caused this exception.

        Returns:
            int: The error code because of which the exception was raised.
        """
        return self._error_code

    def get_error_text(self):
        """
        Retrieves the error text, corresponding to the API return code that has
        caused this exception. This is the error text return by
        :meth:`nxlib.api.translate_error_code`.

        Returns:
            int: The text corresponding to the error code.
        """
        return nxlib.api.translate_error_code(self._error_code)

    def get_item_path(self):
        """
        Retrieves the path of the item that was attempted to access when the
        exception was raised.

        Returns:
            str: The path of the item that has caused the exception.
        """
        return self._path

    def __str__(self):
        message = (f"NxLib error {self._error_code} ({self.get_error_text()}) "
                   f"for item {self._path}")
        try:
            if self._path:
                json_str = nxlib.NxLibItem(self._path).as_json(True)
                message += f"\nCurrent item value: {json_str}"
        except NxLibError:
            pass
        return message
