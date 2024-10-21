import time
from typing import Optional, Union, List, Any, Dict, Type

from flask import g
from marshmallow import Schema, ValidationError

from flarchitect.schemas.utils import dump_schema_if_exists
from flarchitect.utils.core_utils import get_count


class CustomResponse:
    """
    Custom response class to be used for serializing output.
    """
    #todo Not really sure why this is here anymore - needs really looking at. Was a use for it once, but no loger it seems.

    def __init__(
        self,
        value: Optional[Union[List, Any]] = None,
        count: Optional[int] = 1,
        error: Optional[Union[List, Dict, Any]] = None,
        status_code: Optional[int] = 200,
        next_url: Optional[str] = None,
        previous_url: Optional[str] = None,
        many: Optional[bool] = False,
        response_ms: Optional[float] = None,
    ):
        self.response_ms = response_ms
        self.value = value
        self.count = count
        self.error = error
        self.status_code = status_code
        self.next_url = next_url
        self.previous_url = previous_url
        self.many = many


def serialize_output_with_mallow(
    output_schema: Type[Schema], data: Any
) -> CustomResponse:
    """
    Utility function to serialize output using a given Marshmallow schema.

    Args:
        output_schema (Type[Schema]): The Marshmallow schema to be used for serialization.
        data (Any): The data to be serialized.

    Returns:
        CustomResponse: The serialized data wrapped in a CustomResponse object.
    """

    try:
        is_list = isinstance(data, list) or (isinstance(data, dict) and ("value" in data or ("query" in data and isinstance(data["query"], list))))
        dump_data = data.get("query", data) if isinstance(data, dict) else data
        value = dump_schema_if_exists(output_schema, dump_data, is_list)
        count = get_count(data, value)

        #Added this is the create_response function as errors were missing the response time
        # response_ms = (time.time() - g.start_time) * 1000 if g.get("start_time") else "n/a"

        return CustomResponse(
            value=value,
            count=count,
            next_url= data.get("next_url") if isinstance(data, dict) else None,
            previous_url=data.get("previous_url") if isinstance(data, dict) else None,
            # response_ms=response_ms,
            many=is_list,
        )

    except ValidationError as err:
        return CustomResponse(value=None, count=None, error=err.messages, status_code=500)


def check_serialise_method_and_return(result: Dict, schema: "AutoSchema", model_columns: List[str], schema_columns: List[str]) -> Union[List[Dict], Any]:
    """
    Checks if the serialization matches the schema or model columns. If not, returns the raw result.

    Args:
        result (Dict): The result dictionary.
        schema (AutoSchema): The schema used for serialization.
        model_columns (List[str]): The model columns.
        schema_columns (List[str]): The schema columns.

    Returns:
        Union[List[Dict], Any]: Serialized data or the original result.
    """
    output_list = result.pop("dictionary", [])
    if output_list:
        output_keys = list(output_list[0].keys())
        if any(x not in model_columns for x in output_keys) or any(x not in schema_columns for x in output_keys):
            return output_list

    return serialize_output_with_mallow(schema, result)
