import argparse
import gzip
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Union

import pytz
from bson.binary import Binary
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from mongo_analyser.shared import BaseAnalyser


class DataExtractor(BaseAnalyser):
    """
    This class provides functions to extract data from a MongoDB collection given a schema file
    that describes the structure of documents in the collection.
    """

    @staticmethod
    def infer_type(value: any) -> str:
        """Infers the type and returns it."""
        if isinstance(value, bool):
            return "bool"
        elif isinstance(value, int):
            return "int"
        elif isinstance(value, float):
            return "float"
        elif isinstance(value, str):
            return "str"
        elif isinstance(value, Binary):
            binary_type = DataExtractor.binary_type_map.get(value.subtype, "binary<unknown>")
            return binary_type
        elif isinstance(value, list):
            list_types = set(DataExtractor.infer_type(item) for item in value)
            if len(list_types) == 1:
                return f"array<{list_types.pop()}>"
            else:
                return "array<mixed>"
        elif isinstance(value, dict):
            return "dict"
        elif value is None:
            return "null"
        else:
            return "unknown"

    @staticmethod
    def infer_types_from_array(array_of_dicts: List[dict]) -> dict:
        """
        Infers the field types for an array of dictionaries.
        Returns a dictionary where the keys are field names and the values are inferred types.
        """
        field_types = {}

        for item in array_of_dicts:
            if isinstance(item, dict):
                for key, value in item.items():
                    inferred_type = DataExtractor.infer_type(value)
                    if key in field_types:
                        if field_types[key] != inferred_type:
                            field_types[key] = "mixed"
                    else:
                        field_types[key] = inferred_type
            else:
                raise ValueError("The array must contain dictionaries.")

        return field_types

    @staticmethod
    def convert_to_json_compatible(document: dict, schema: dict,
                                   tz: Union[pytz.timezone, None]) -> dict:
        """Converts a MongoDB document to a JSON-compatible format based on the given schema."""

        def convert_value(key: str, value: any, value_type: Union[str, None] = None) -> any:
            """Converts the value to the specified type."""
            try:
                if isinstance(value, list):
                    return [convert_value(key, item) for item in value]
                elif value_type == "binary<UUID>":
                    return str(uuid.UUID(bytes=value))
                elif value_type == "str":
                    return str(value)
                elif value_type in ["int64", "int32"]:
                    return int(value)
                elif value_type == "bool":
                    return bool(value)
                elif value_type == "double":
                    return float(value)
                elif value_type == "datetime":
                    if isinstance(value, datetime):
                        localized_value = value.astimezone(tz)
                        return localized_value.isoformat()
                elif value_type == "dict":
                    return {k: convert_value(k, v) for k, v in value.items()}
                elif value_type == "empty":
                    return None
                elif value_type == "binary":
                    return value.hex() if hasattr(value, 'hex') else str(value)
                else:
                    try:
                        return value.hex() if hasattr(value, 'hex') else str(value)
                    except AttributeError:
                        return str(value)
            except Exception as e:
                print(
                    f"Failed to convert value '{value}' to type '{value_type}'"
                    f" for field '{key}': {e}"
                )
                return None

        result = {}
        for key, value_schema in schema.items():
            if key in document:
                if isinstance(value_schema, dict):
                    if 'type' in value_schema and not isinstance(value_schema['type'], dict):
                        if value_schema['type'].startswith('array'):
                            array_element_type = value_schema['type'].split('<')[1].strip('>')
                            result[key] = [convert_value(key, item, array_element_type) for item in
                                           document[key]]
                        else:
                            result[key] = convert_value(key, document[key], value_schema['type'])
                    else:
                        result[key] = DataExtractor.convert_to_json_compatible(document[key],
                                                                               value_schema, tz)
                else:
                    result[key] = None
            else:
                result[key] = None
        return result

    @staticmethod
    def extract_data(mongo_uri: str, db_name: str, collection_name: str, schema: dict,
                     output_file: Union[str, Path], tz: Union[None, pytz.timezone],
                     batch_size: int, limit: int) -> None:
        """Extracts data from MongoDB and exports it to a compressed JSON file."""

        # Connect to MongoDB
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db[collection_name]

        # Initialize the data cursor
        data_cursor = collection.find().batch_size(batch_size)

        # Apply limit if specified otherwise read all records in the collection
        if limit >= 0:
            data_cursor = data_cursor.limit(limit)
            print(f"Reading up to {limit} records from the collection...")
        else:
            print("Reading all records from the collection...")

        # Convert and store documents as per the schema
        converted_data = [DataExtractor.convert_to_json_compatible(doc, schema, tz) for doc in
                          data_cursor]

        # Write data to compressed JSON file
        with gzip.open(output_file, 'wt', encoding="utf-8") as f:
            json.dump(converted_data, f, indent=4)


def main() -> None:
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Extract data from MongoDB and export it to a compressed JSON file"
    )

    # MongoDB connection parameters
    parser.add_argument('--host', type=str, default='localhost',
                        help="MongoDB host (default: localhost)")
    parser.add_argument('--port', type=int, default=27017,
                        help="MongoDB port (default: 27017)")
    parser.add_argument('--username', type=str, default=None,
                        help="MongoDB username (optional)")
    parser.add_argument('--password', type=str, default=None,
                        help="MongoDB password (optional)")
    parser.add_argument('--database', type=str, default='assets',
                        help="MongoDB database name (default: assets)")
    parser.add_argument('--collection', type=str, default='devices',
                        help="MongoDB collection name (default: devices)")

    # Schema and output parameters
    parser.add_argument('--schema_file', type=str, default='schema.json',
                        help="Schema file path (default: schema.json)")
    parser.add_argument('--output_file', type=str, default='output.json.gz',
                        help="Output compressed JSON file path (default: output.json.gz)")

    # Timezone parameter
    parser.add_argument('--timezone', type=str, default='CET',
                        help="Timezone for datetime fields (default: CET)")

    # Batch size and record limit parameters
    parser.add_argument('--batch_size', type=int, default=10000,
                        help="Batch size for reading data (default: 10000)")
    parser.add_argument('--limit', type=int, default=-1,
                        help="Max number of records to read (default: -1 for no limit)")

    args = parser.parse_args()

    # Build MongoDB URI
    mongo_uri = DataExtractor.build_mongo_uri(args.host, args.port, args.username, args.password)

    # Load schema from JSON file
    with open(args.schema_file, 'r') as f:
        schema_file = json.load(f)

    # Get the timezone from the argument
    tz = pytz.timezone(args.timezone)

    # Try to connect and extract data
    try:
        DataExtractor.extract_data(mongo_uri, args.database, args.collection, schema_file,
                                   args.output_file, tz, args.batch_size, args.limit)
        print(f"Data successfully exported to {args.output_file}")
    except ConnectionFailure as e:
        print(f"Failed to connect to MongoDB: {e}")


if __name__ == "__main__":
    main()
