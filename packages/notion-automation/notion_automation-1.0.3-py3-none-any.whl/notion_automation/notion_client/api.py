import requests

from .logger import logger
from .models import EntryConfig, SchemaConfig


class NotionClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

    def create_database(self, parent_id: str, schema: SchemaConfig) -> str:
        url = 'https://api.notion.com/v1/databases'
        data = {
            "parent": {"type": "page_id", "page_id": parent_id},
            "title": [{"type": "text", "text": {"content": schema.title}}],
            "properties": schema.to_notion_properties()
        }
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            database_id = response.json()["id"]
            logger.info(f"Database '{schema.title}' created with ID: {database_id}")
            return database_id
        except requests.exceptions.HTTPError as e:
            logger.error(f"Failed to create database: {e.response.text}")
            raise

    def create_entry(self, database_id: str, entry: EntryConfig):
        url = 'https://api.notion.com/v1/pages'
        data = {
            "parent": {"database_id": database_id},
            "properties": entry.to_notion_properties()
        }
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            logger.info(f"Entry created in database '{database_id}'.")
        except requests.exceptions.HTTPError as e:
            logger.error(f"Failed to create entry: {e.response.text}")
            raise
