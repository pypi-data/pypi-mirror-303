import argparse
import csv
import io
import json
import uuid
from collections import OrderedDict
from pathlib import Path
from typing import Union, List

from bson import ObjectId, Binary, Int64, Decimal128
from pymongo import MongoClient
from pymongo.synchronous.collection import Collection

from mongo_analyser.shared import BaseAnalyser


class SchemaAnalyser(BaseAnalyser):
    """
    This class provides functions to infer the schema of a MongoDB collection and save it to a JSON
    file. It also generates a table with statistics about the values of each field in the collection.
    """

    @staticmethod
    def extract_schema_and_stats(document: dict, schema: Union[dict, OrderedDict, None] = None,
                                 stats: Union[dict, OrderedDict, None] = None,
                                 prefix: str = "") -> tuple:
        """Extracts schema and statistics from a MongoDB document."""
        if schema is None:
            schema = OrderedDict()
        if stats is None:
            stats = OrderedDict()

        for key, value in document.items():
            full_key = f"{prefix}.{key}" if prefix else key

            # Initialize the stats dictionary for each field
            if full_key not in stats:
                stats[full_key] = {"values": set(), "count": 0}

            if isinstance(value, dict):
                SchemaAnalyser.extract_schema_and_stats(value, schema, stats, full_key)
            elif isinstance(value, list):
                SchemaAnalyser.handle_array(value, schema, stats, full_key)
            else:
                SchemaAnalyser.handle_simple_value(value, schema, stats, full_key)

            # Track how often the field appears
            stats[full_key]["count"] += 1

        return schema, stats

    @staticmethod
    def handle_array(value: list, schema: Union[dict, OrderedDict],
                     stats: Union[dict, OrderedDict],
                     full_key: str) -> None:
        """Handles the extraction of array data from a BSON document."""

        # Initialize the schema dictionary for the full_key if it doesn't exist
        if full_key not in schema:
            schema[full_key] = {}

        if len(value) > 0:
            first_elem = value[0]
            if isinstance(first_elem, dict):
                # Stop recursion here; just mark as "array<dict>"
                schema[full_key]["type"] = "array<dict>"
            elif isinstance(first_elem, ObjectId):
                schema[full_key] = {"type": "array<ObjectId>"}
            elif isinstance(first_elem, uuid.UUID):
                schema[full_key] = {"type": "array<UUID>"}
            elif isinstance(first_elem, Binary):
                SchemaAnalyser.handle_binary(first_elem, schema, full_key, is_array=True)
            elif isinstance(first_elem, bool):
                schema[full_key] = {"type": "array<bool>"}
            elif isinstance(first_elem, int):
                schema[full_key] = {"type": "array<int32>"
                if isinstance(first_elem, int) and
                   not isinstance(first_elem, Int64) else "array<int64>"}
            elif isinstance(first_elem, float):
                schema[full_key] = {"type": "array<double>"}
            else:
                elem_type = type(first_elem).__name__
                schema[full_key] = {"type": f"array<{elem_type}>"}
        else:
            schema[full_key] = {"type": "array<empty>"}

        if full_key not in stats:
            stats[full_key] = {"values": set(), "count": 0}

        def make_hashable(item: [dict, list]) -> any:
            """Converts an unhashable list or dictionary object to a hashable object."""
            if isinstance(item, dict):
                return frozenset((k, make_hashable(v)) for k, v in item.items())
            elif isinstance(item, list):
                return tuple(make_hashable(i) for i in item)
            else:
                return item

        hashable_value = make_hashable(value)
        stats[full_key]["values"].add(hashable_value)

    @staticmethod
    def handle_simple_value(value: any, schema: Union[dict, OrderedDict],
                            stats: Union[dict, OrderedDict], full_key: str) -> None:
        """Handles the extraction of primary data types from a BSON document."""
        if isinstance(value, ObjectId):
            schema[full_key] = {"type": "binary<ObjectId>"}
        elif isinstance(value, uuid.UUID):
            schema[full_key] = {"type": "binary<UUID>"}
        elif isinstance(value, Binary):
            SchemaAnalyser.handle_binary(value, schema, full_key)
        elif isinstance(value, bool):
            schema[full_key] = {"type": "bool"}
        elif isinstance(value, int):
            schema[full_key] = {"type": "int32" if isinstance(value, int) and
                                                   not isinstance(value, Int64) else "int64"}
        elif isinstance(value, float):
            schema[full_key] = {"type": "double"}
        elif isinstance(value, Decimal128):
            schema[full_key] = {"type": "decimal128"}
        else:
            schema[full_key] = {"type": type(value).__name__}

        if full_key not in stats:
            stats[full_key] = {"values": set(), "count": 0}

        stats[full_key]["values"].add(value)

    # MongoDB connection setup
    @staticmethod
    def connect_mongo(uri: str, db_name: str, collection_name: str) -> Collection:
        """Connects to a MongoDB collection and returns the collection object."""
        client = MongoClient(uri)
        db = client[db_name]
        collection = db[collection_name]
        return collection

    # Function to infer schema and statistics from sample documents with batch processing
    @staticmethod
    def infer_schema_and_stats(collection: Collection, sample_size: int,
                               batch_size: int = 10000) -> tuple:
        """Infers the schema of a MongoDB collection using a sample of documents."""
        schema = OrderedDict()
        stats = OrderedDict()
        total_docs = 0

        # If sample_size is negative, fetch all documents from the collection
        if sample_size < 0:
            documents = collection.find().batch_size(batch_size)
        else:
            documents = collection.aggregate([{'$sample': {'size': sample_size}}]).batch_size(
                batch_size)

        for doc in documents:
            total_docs += 1
            schema, stats = SchemaAnalyser.extract_schema_and_stats(doc, schema, stats)

            if sample_size > 0 and total_docs >= sample_size:
                break

        final_stats = OrderedDict()
        for key, stat in stats.items():
            cardinality = len(stat["values"])
            # Calculate missing values based on how many times the field appeared vs total documents
            missing_count = total_docs - stat["count"]
            missing_percentage = (missing_count / total_docs) * 100 if total_docs > 0 else 0
            final_stats[key] = {
                "cardinality": cardinality,
                "missing_percentage": missing_percentage
            }

        sorted_schema = OrderedDict(sorted(schema.items()))
        sorted_stats = OrderedDict(sorted(final_stats.items()))
        return dict(sorted_schema), sorted_stats

    # Function to create a Unicode table
    @staticmethod
    def draw_unicode_table(headers: List[str], rows: List[List[str]]) -> None:
        """Draws a table with Unicode characters using the provided headers and rows."""
        col_widths = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]

        def draw_separator(sep_type):
            parts = {
                'top': ('┌', '┬', '┐'),
                'mid': ('├', '┼', '┤'),
                'bottom': ('└', '┴', '┘'),
                'line': '─'
            }
            start, sep, end = parts[sep_type]
            separator = start + sep.join([parts['line'] * (w + 2) for w in col_widths]) + end
            print(separator)

        def draw_row(items):
            row = "│ " + " │ ".join(
                f"{str(item):<{w}}" for item, w in zip(items, col_widths)) + " │"
            print(row)

        draw_separator('top')
        draw_row(headers)
        draw_separator('mid')
        for row in rows:
            draw_row(row)
        draw_separator('bottom')

    @staticmethod
    def schema_to_hierarchical(schema: dict) -> dict:
        """Converts a flat schema to a hierarchical schema."""
        hierarchical_schema = {}
        for field, details in schema.items():
            parts = field.split('.')
            current_level = hierarchical_schema
            for part in parts[:-1]:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]
            current_level[parts[-1]] = {"type": details['type']}
        return hierarchical_schema

    @staticmethod
    def save_schema_to_json(schema: dict, schema_file: Union[str, Path]) -> None:
        """Saves the schema to a JSON file."""
        hierarchical_schema = SchemaAnalyser.schema_to_hierarchical(schema)
        with io.open(schema_file, 'w') as f:
            json.dump(hierarchical_schema, f, indent=4)
        print(f"Schema has been saved to {schema_file}.")

    @staticmethod
    def save_table_to_csv(headers: List[str], rows: List[List[str]],
                          csv_file: Union[str, Path]) -> None:
        """Writes the rows to a CSV file with the provided headers."""
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)
        print(f"Table has been saved to {csv_file}.")


def main() -> None:
    parser = argparse.ArgumentParser(description='MongoDB schema extractor')
    parser.add_argument('--host', type=str, default="localhost", help='MongoDB host')
    parser.add_argument('--port', type=int, default=27017, help='MongoDB port')
    parser.add_argument('--username', type=str, help='MongoDB username (optional)')
    parser.add_argument('--password', type=str, help='MongoDB password (optional)')
    parser.add_argument('--database', type=str, default="assets", help='Database name.')
    parser.add_argument('--collection', type=str, default="devices", help='Collection name')
    parser.add_argument('--sample_size', type=int, default=10000,
                        help='Number of documents to sample.')
    parser.add_argument('--show_table', type=SchemaAnalyser.str2bool, nargs='?',
                        const=True, default=True,
                        help='Show the schema and stats as a table (True/False)')
    parser.add_argument('--schema_file', type=str, default='schema.json',
                        help='Schema file path for saving schema in JSON format')
    parser.add_argument('--metadata_file', type=str, default='metadata.csv',
                        help='Metadata file path for saving the table in CSV format')

    args = parser.parse_args()

    mongo_uri = SchemaAnalyser.build_mongo_uri(args.host, args.port, args.username,
                                               args.password)
    collection = SchemaAnalyser.connect_mongo(mongo_uri, args.database, args.collection)
    schema, stats = SchemaAnalyser.infer_schema_and_stats(collection,
                                                          sample_size=args.sample_size)

    print(
        f'Using a sample size of {args.sample_size} documents to infer the schema and statistics.')

    headers = ["Field", "Type", "Cardinality", "Missing (%)"]
    rows = []
    for field, details in schema.items():
        field_stats = stats.get(field, {})
        cardinality = field_stats.get("cardinality", "N/A")
        missing_percentage = field_stats.get("missing_percentage", "N/A")
        rows.append([field, details['type'], cardinality, round(missing_percentage, 1)])

    if args.show_table:
        SchemaAnalyser.draw_unicode_table(headers, rows)
    else:
        print("Schema with Cardinality and Missing Percentage:")
        for i, row in enumerate(rows, start=1):
            print(
                f"Field[{i}]: {row[0]}, Type: {row[1]}, Cardinality: {row[2]}, Missing (%): {row[3]}")

    if args.schema_file:
        SchemaAnalyser.save_schema_to_json(schema, args.schema_file)

    if args.metadata_file:
        SchemaAnalyser.save_table_to_csv(headers, rows, args.metadata_file)


if __name__ == '__main__':
    main()
