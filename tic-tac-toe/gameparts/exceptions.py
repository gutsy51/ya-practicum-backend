class FieldIndexError(IndexError):
    """Raise when index is out of bounds of the field."""

    def __str__(self):
        return 'The index is out of bounds of the field.'


class CellOccupiedError(Exception):
    """Raise when cell is already occupied."""

    def __str__(self):
        return 'The cell is already occupied.'
