import argparse
import json
import os
import re
import sys

from dotenv import load_dotenv

from notion_automation.notion_client.api import NotionClient
from notion_automation.notion_client.logger import logger
from notion_automation.notion_client.models import EntryConfig, EntryProperty, PropertyConfig, PropertyOption, SchemaConfig

# Load environment variables from .env
load_dotenv()

def create_database(schema_path, entries_path=None, page_id=None):
    """Creates a Notion database and optionally adds entries."""
    notion_api_key = os.getenv("NOTION_API_KEY")
    notion_page_id_env = os.getenv("NOTION_PAGE_ID")

    # Determine the page ID to use
    notion_page_id = page_id if page_id else notion_page_id_env

    if not notion_api_key or not notion_page_id:
        print(
            "Error: Please set the NOTION_API_KEY and NOTION_PAGE_ID in the .env file or provide them as CLI arguments."
        )
        sys.exit(1)

    try:
        with open(schema_path, "r") as schema_file:
            schema_data = json.load(schema_file)

        # Parse the schema
        properties = parse_schema(schema_data)

        schema_config = SchemaConfig(title=schema_data["title"], properties=properties)

    except FileNotFoundError as e:
        error_message = f"Error: {e}"
        logger.error(error_message)
        print(error_message)
        sys.exit(1)
    except json.JSONDecodeError as e:
        error_message = f"Error parsing JSON: {e}"
        logger.error(error_message)
        print(error_message)
        sys.exit(1)
    except Exception as e:
        error_message = f"Error processing schema: {e}"
        logger.error(error_message)
        print(error_message)
        sys.exit(1)

    entries_config = []

    if entries_path:
        try:
            with open(entries_path, "r") as entries_file:
                entries_data = json.load(entries_file)

            for entry in entries_data.get("entries", []):
                entry_properties = {}
                if "properties" in entry:
                    # Existing format
                    for name, prop in entry["properties"].items():
                        entry_properties[name] = EntryProperty(**prop)
                else:
                    # Simplified format
                    for name, value in entry.items():
                        entry_properties[name] = EntryProperty.from_value(
                            name, value, properties
                        )
                # Use keyword argument here
                entries_config.append(EntryConfig(properties=entry_properties))

        except FileNotFoundError as e:
            error_message = f"Error: {e}"
            logger.error(error_message)
            print(error_message)
            sys.exit(1)
        except json.JSONDecodeError as e:
            error_message = f"Error parsing JSON: {e}"
            logger.error(error_message)
            print(error_message)
            sys.exit(1)
        except Exception as e:
            error_message = f"Error processing entries: {e}"
            logger.error(error_message)
            print(error_message)
            sys.exit(1)

    try:
        notion_client = NotionClient(notion_api_key)
        database_id = notion_client.create_database(
            parent_id=notion_page_id, schema=schema_config
        )
        print(f"Database created successfully with ID: {database_id}")

        if entries_config:
            for entry in entries_config:
                notion_client.create_entry(database_id, entry)
            print("Entries added successfully.")
    except Exception as e:
        error_message = f"Error creating database or entries: {e}"
        logger.error(error_message)
        print(error_message)
        sys.exit(1)

def parse_schema(schema_data):
    """Parses the schema data into properties."""
    properties = {}

    if isinstance(schema_data["properties"], list):
        # Check if it's natural language descriptions
        if all(isinstance(p, str) for p in schema_data["properties"]):
            properties = parse_natural_language_properties(schema_data["properties"])
        else:
            # List of property dicts
            for prop in schema_data["properties"]:
                name = prop.get("name")
                property_type = prop.get("type")
                if not name or not property_type:
                    raise ValueError(f"Property definition is missing 'name' or 'type': {prop}")
                options = prop.get("options", [])
                property_options = [
                    PropertyOption(name=opt) if isinstance(opt, str) else PropertyOption(**opt)
                    for opt in options
                ]
                properties[name] = PropertyConfig(
                    property_type=property_type, options=property_options
                )
    elif isinstance(schema_data["properties"], dict):
        # Existing logic for dict format
        for name, prop in schema_data["properties"].items():
            if 'property_type' not in prop:
                raise ValueError(f"Property '{name}' is missing 'property_type'")
            property_type = prop["property_type"]
            options_data = prop.get("options", [])
            options = [PropertyOption(**option) for option in options_data]
            properties[name] = PropertyConfig(
                property_type=property_type, options=options
            )
    else:
        raise ValueError("Invalid schema format for 'properties' field.")

    return properties

def parse_natural_language_properties(property_descriptions):
    """Parses natural language property descriptions into PropertyConfig."""
    properties = {}
    for desc in property_descriptions:
        # Simple parsing logic
        try:
            name, rest = desc.split(":", 1)
        except ValueError:
            raise ValueError(f"Invalid property description format: '{desc}'")
        rest = rest.strip()
        options = None
        property_type = 'rich_text'  # Default type

        # Check for keywords to determine property type
        if "date" in rest.lower():
            property_type = "date"
        elif any(keyword in rest.lower() for keyword in ["status", "select", "category"]):
            property_type = "select"
        
        # Detect options in parentheses
        match = re.search(r'\((.*?)\)', rest)
        if match:
            options_str = match.group(1)
            options = [PropertyOption(name=opt.strip()) for opt in options_str.split(",")]

        properties[name.strip()] = PropertyConfig(
            property_type=property_type, options=options
        )
    return properties

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Create a Notion database and add entries."
    )
    parser.add_argument("--schema", required=True, help="Path to the JSON schema file.")
    parser.add_argument("--entries", required=False, help="Path to the JSON entries file.")
    parser.add_argument("--page-id", required=False, help="Target Notion Page ID to create the database in.")

    # Parse the arguments
    args = parser.parse_args()

    # Call the create_database function with the provided arguments
    create_database(args.schema, args.entries, args.page_id)
