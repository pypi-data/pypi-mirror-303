from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator


class Param(BaseModel):
    model_config = ConfigDict(populate_by_name=True, frozen=True)

    description: str
    expected_type: str = Field(description="The expected type of the parameter as a string", alias="type")
    optional: bool = Field(description="Whether the parameter is optional or not", alias="optional", default=False)
    data_type: Any = Field(description="The allowed data type of the parameter")

    @model_validator(mode="before")
    def set_data_type(cls, values) -> Any:
        """
        Set the data type of the parameter based on the expected type

        :param values: The values of the model
        :return: The data type of the parameter
        :rtype: Any
        """
        if expected_type := values.get("type"):
            values["data_type"] = cls._map_types(expected_type)
        return values

    @classmethod
    def _map_types(cls, type_str: str) -> Any:
        """
        Map the string type to the actual type

        :param str type_str: The data type as a string
        :return: The actual data type
        :rtype: Any
        """
        data_types = {
            "string": str,
            "object": dict,
            "array": list,
            "number": float,
            "integer": int,
            "boolean": bool,
        }
        if type_str in data_types:
            return data_types[type_str]
        try:
            return eval(type_str)
        except NameError:
            raise ValueError(f"Invalid type: {type_str}")
