import json
from collections import OrderedDict
from typing import Any, Dict, List, Union


class TupleEncoder(json.JSONEncoder):
    """
    Customize the json encoding in order to have a tuple save conversion
    """

    __tuple_key__ = "__is_tuple__"
    __tuple_content__ = "content"

    def encode(self, obj: Any) -> str:
        """Return a JSON string representation of a Python data structure.

        >>> from json.encoder import JSONEncoder
        >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
        '{"foo": ["bar", "baz"]}'

        REMARK: The encoding will only work for top level tupels and not for nested tuples

        Args:
            obj: The object to encode

        Returns:
            The encoded object as json string
        """

        def tuple_save_encoding(value: Any) -> Any:
            if isinstance(value, tuple):
                return {
                    TupleEncoder.__tuple_key__: True,
                    TupleEncoder.__tuple_content__: value,
                }
            elif isinstance(value, list):
                return [tuple_save_encoding(e) for e in value]
            elif isinstance(value, dict) or isinstance(value, OrderedDict):
                return {k: tuple_save_encoding(v) for k, v in value.items()}
            else:
                return value

        return str(json.JSONEncoder.encode(self, tuple_save_encoding(value=obj)))

    @staticmethod
    def tuple_save_loading_hook(obj: Any) -> Any:
        """
        Method that is designed to be used as object_hook in json.loads
        when decoding a json string, which has been encoded via TupleEncoder.encode

        Args:
            obj: The object to decode

        REMARK: The decoding will only work for top level tuples and not for nested tuples

        Returns:
            The correct representation of the object
        """
        if TupleEncoder.__tuple_content__ in obj and TupleEncoder.__tuple_key__ in obj:
            return tuple(obj[TupleEncoder.__tuple_content__])
        return obj

    @staticmethod
    def decode(data: Any) -> Any:
        """Dedicated method to decode data that has been encoded via TupleEncoder.encode.

        Typically, the input is a dictionary which is recursively decoded by the respective
        calls of TupleEncoder.decode.

        Args:
            data: The (encoded) data that should be decoded.

        Returns:
            The decoded data.
        """
        if isinstance(data, dict):
            # Decode and return tuple object
            if (
                TupleEncoder.__tuple_content__ in data
                and TupleEncoder.__tuple_key__ in data
            ):
                return tuple(data[TupleEncoder.__tuple_content__])

            new_data = {}
            for key, value in data.items():
                # Decode and tuple object
                if isinstance(value, dict):
                    if (
                        TupleEncoder.__tuple_content__ in value
                        and TupleEncoder.__tuple_key__ in value
                    ):
                        new_data[key] = tuple(value[TupleEncoder.__tuple_content__])
                        continue

                # Recursively call decoding method for each dictionary value
                new_data[key] = TupleEncoder.decode(value)
            return new_data
        elif isinstance(data, list):
            # Recursively call decoding method for each list element
            return [TupleEncoder.decode(element) for element in data]
        else:
            # Nothing to decode, end of recursion
            return data
