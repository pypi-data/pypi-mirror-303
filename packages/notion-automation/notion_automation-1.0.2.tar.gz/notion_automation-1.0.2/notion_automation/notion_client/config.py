import json
import os

from .models import EntryConfig, SchemaConfig


class ConfigManager:
    def __init__(self, config_path='plugins'):
        self.config_path = config_path

    def load_schema(self, schema_name: str) -> SchemaConfig:
        file_path = os.path.join(self.config_path, f"{schema_name}.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Schema file '{file_path}' not found.")
        with open(file_path, 'r') as file:
            data = json.load(file)
        return SchemaConfig(**data)

    def load_entries(self, entries_name: str) -> list:
        file_path = os.path.join(self.config_path, f"{entries_name}.json")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Entries file '{file_path}' not found.")
        with open(file_path, 'r') as file:
            data = json.load(file)
        entries = [EntryConfig(**entry) for entry in data.get("entries", [])]
        return entries
