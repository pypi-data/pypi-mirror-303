import argparse
import os

from notion_automation.notion_client.api import NotionClient
from notion_automation.notion_client.config import ConfigManager


def main(schema_name, entries_name):
    config_manager = ConfigManager(config_path=args.config_path)

    schema = config_manager.load_schema(schema_name)
    entries = config_manager.load_entries(entries_name)

    notion_api_key = os.getenv('NOTION_API_KEY')
    notion_page_id = os.getenv('NOTION_PAGE_ID')

    notion_client = NotionClient(api_key=notion_api_key)
    database_id = notion_client.create_database(parent_id=notion_page_id, schema=schema)

    for entry in entries:
        notion_client.create_entry(database_id, entry)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Notion database.")
    parser.add_argument('schema', type=str, help="Schema name without extension.")
    parser.add_argument('entries', type=str, help="Entries name without extension.")
    parser.add_argument('--config-path', type=str, default='plugins', help="Path to the configuration directory.")
    args = parser.parse_args()
    main(args.schema, args.entries)
