def required_last(schema: dict) -> dict:
    """Modify JSON schema to recursively put all 'required' fields at the end of the schema.

    This is done because otherwise the 'required' fields
    are checked by jsonschema before filling the defaults,
    which can cause the validation to fail.

    Returns
    -------
    dict
        Modified schema.
        Note that the input schema is modified in-place,
        so the return value is a reference to the (now modified) input schema.
    """
    if "required" in schema:
        schema["required"] = schema.pop("required")
    for key in ["anyOf", "allOf", "oneOf", "prefixItems"]:
        if key in schema:
            for subschema in schema[key]:
                required_last(subschema)
    for key in ["if", "then", "else", "not", "items", "unevaluatedItems", "contains", "additionalProperties", "patternProperties", "unevaluatedProperties"]:
        if key in schema and isinstance(schema[key], dict):
            required_last(schema[key])
    if "properties" in schema and isinstance(schema["properties"], dict):
        for subschema in schema["properties"].values():
            required_last(subschema)
    return schema


def add_property(schema: dict, prop: str, value: dict) -> dict:
    """Recursively add a property to a JSON schema.

    Parameters
    ----------
    schema : dict
        The JSON schema to modify.
    prop : str
        The name of the property to add.
    value : Any
        The value of the property to add.

    Returns
    -------
    dict
        The modified schema.
    """
    if "properties" in schema:
        schema["properties"][prop] = value
        for subschema in schema["properties"].values():
            add_property(subschema, prop, value)
    for key in ["anyOf", "allOf", "oneOf", "prefixItems"]:
        if key in schema:
            for subschema in schema[key]:
                add_property(subschema, prop, value)
    for key in ["if", "then", "else", "not", "items", "unevaluatedItems", "contains", "additionalProperties", "patternProperties", "unevaluatedProperties"]:
        if key in schema and isinstance(schema[key], dict):
            add_property(schema[key], prop, value)
    return schema