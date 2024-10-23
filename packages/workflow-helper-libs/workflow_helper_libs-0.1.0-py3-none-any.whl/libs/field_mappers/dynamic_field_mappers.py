"""Dynamic field mapper class."""

from abc import ABC


class DynamicFieldMapper(ABC):
    """Abstract base class for providing dynamic field mappings.

    Attributes:
        source (dict): The dictionary containing the source value.
        required_set_fields (list): List of mandatory fields to be found in source.
    """

    def __init__(self, source: dict, required_set_fields: list):
        """Initialize the DynamicFieldMapper.

        Args:
            source (dict): The dictionary containing the source value.
            required_set_fields (list): List of mandatory fields to be found in source.
        """
        self.source = source
        self.required_set_fields = required_set_fields
