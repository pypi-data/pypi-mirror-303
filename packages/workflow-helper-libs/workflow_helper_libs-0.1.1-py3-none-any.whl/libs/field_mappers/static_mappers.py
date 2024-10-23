"""Field mapper class."""


class FieldMapper:
    """Class to map and retrieve fields from a source dictionary."""

    def __init__(self, source: dict, field_mappings: dict, required_set_fields: list):
        """Initialize the FieldMapperPE.

        Based on the defined field mappings, this method first extracts
        the field names from a possible string, dict, or list depending
        on the desired field format. It then checks if this field is
        included in the source dictionary. If so, it calls the set_field
        method with the desired field mapping.

        If one of the required fields is missing, the `map_fields` raises an error.

        Args:
            source (dict): The dictionary containing the source values.
            field_mappings (dict): The mappings between target fields and source fields.
            required_set_fields (list): List of mandatory fields that must be set.

        Usage:
            This method is used to map fields from a source dictionary
            into a new target dictionary according to the `field_mappings`.
            The class can be initialized with field mappings and required fields,
            which ensures that all required fields are properly populated in the target.

            Example:
                Assuming the source dictionary contains field data, and some values
                are computed dynamically through methods, the class can handle both
                static and dynamic field mappings.

                If one of the values in `source` refers to a method (e.g., `get_dynamic_value`),
                you can define a dynamic method in the `DynamicFieldMapper` class and map it
                in the source:

                class MyDynamicFieldMapper(DynamicFieldMapper):
                    @staticmethod
                    def get_dynamic_value(source):
                        return f"Dynamic-{source.get('dynamic_key', 'default')}"

                source_data = {
                    "FullName__c": "Jane Doe",
                    "dynamic_key": "Special",
                    "IsActive__c": True
                }

                field_mappings = {
                    "full_name": "FullName__c",
                    "dynamic_field": DynamicFieldMapper.get_dynamic_value,  # Dynamic method reference
                    "is_active": "IsActive__c"
                }

                required_fields = ["FullName__c", "IsActive__c"]

                mapper = FieldMapper(source=source_data, field_mappings=field_mappings,
                                        required_set_fields=required_fields)
                result = mapper.map_fields()

                # Output would include:
                # result = {
                #   'full_name': 'Jane Doe',
                #   'dynamic_field': 'Dynamic-Special',  # dynamically generated field
                #   'is_active': True
                # }
        """
        self.source = source
        self.field_mappings = field_mappings
        self.required_set_fields = required_set_fields

    def map_fields(self):
        """Set the target fields to the provided fields after mapping.

        Returns:
            dict: The target dictionary with mapped fields.

        Raises:
            ValueError: if a one of the required fields is included in the list of missing fields.
        """
        target = {}
        missing_fields = []

        for target_field, source_field in self.field_mappings.items():
            if callable(source_field):
                field_name = source_field.__name__ if hasattr(source_field, "__name__") else str(source_field)
            if isinstance(source_field, dict):
                field_name = [list(source_field.values())[0]]
            elif isinstance(source_field, list):
                field_name = source_field
            else:
                field_name = [source_field]

            did_set = self._set_field(target, target_field, source_field)

            if not did_set:
                missing_fields.extend(field_name)

        if len(missing_fields) > 0:
            raise ValueError(f"Required field(s) {missing_fields!r} not set in source dictionary")

        return target

    def _set_field(self, target: dict, target_field: str, source_field):
        """Set the target[target_field] to source[source_field] if it exists.

        Args:
            target (dict): The dictionary where the value will be set.
            target_field (str): The field name in the target dictionary.
            source_field (any): The field name in the source dictionary.

        Returns:
            bool: Indicates whether or not the source field was set in the target dictionary.

        Note:
            - If the source field's value is a callable function, the return value of this function is
            used.
            - If the source field's value is a dictionary with a "value" key, that value is used.
            - If the source field's value is a string representation of a boolean ("true" or "false"),
            it is converted to a Python boolean.
            - If the source field is passed as a dict (e.g. {"refName": "Currency__c"}), it will set the
            target field to a dict {"refName": source["Currency__c"]}
            - If the source field is passed as a list (e.g. ["Department_Code__c", " - ", "Department2__c"]),
            it will set the target field to a concatenation of the source fields separated by delimiters.
            - The above two rules can be combined i.e. if the source field is passed as a dict
            {"refName": ["Department_Code__c", " - ", "Department2__c"]}, it will set the target field
            to a dict {"refName": f"{source['Department_Code__c']} - {source['Department2__c']}"}
        """
        if callable(source_field):
            return self._handle_callable_field(target, target_field, source_field)

        if isinstance(source_field, dict):
            return self._handle_dict_field(target, target_field, source_field)

        if isinstance(source_field, list):
            return self._handle_list_field(target, target_field, source_field)

        return self._handle_simple_field(target, target_field, source_field)

    def _handle_callable_field(self, target: dict, target_field: str, source_field: callable) -> bool:
        """Handle setting a callable source field."""
        try:
            value = source_field(self.source)
            target[target_field] = value
            return True
        except ValueError:
            return False

    def _handle_dict_field(self, target: dict, target_field: str, source_field: dict) -> bool:
        """Handle setting a dictionary source field."""
        for key, value in source_field.items():
            if isinstance(value, list):
                v, did_set = self._compile_array(value)
                if not did_set:
                    return False
            else:
                if value in self.required_set_fields and self.source.get(value) is None:
                    return False
                v = self.source.get(value)
            target[target_field] = {key: v}
            return True

    def _handle_list_field(self, target: dict, target_field: str, source_field: list) -> bool:
        """Handle setting a list source field."""
        v, did_set = self._compile_array(source_field)
        if not did_set:
            return False
        target[target_field] = v
        return True

    def _handle_simple_field(self, target: dict, target_field: str, source_field) -> bool:
        """Handle setting a simple source field."""
        if source_field in self.required_set_fields and self.source.get(source_field) is None:
            return False
        value = self.source.get(source_field)
        if isinstance(value, dict) and "value" in value:
            value = value["value"]
        elif isinstance(value, str) and value.lower() in ["true", "false"]:
            value = value.lower() == "true"
        target[target_field] = value
        return True

    def _compile_array(self, arr: list) -> (str, bool):
        """Compile a string from the array of source fields."""
        delimiters = [" - ", " "]
        value = ""
        for key in arr:
            if key in delimiters:
                value += key
            else:
                if key in self.required_set_fields and self.source.get(key) is None:
                    return None, False
                value += self.source.get(key)
        return value, True
