import json

import pytest

from notion_automation.cli import parse_schema
from notion_automation.notion_client.api import NotionClient
from notion_automation.notion_client.models import EntryProperty, PropertyConfig, SchemaConfig


@pytest.fixture
def notion_client():
    return NotionClient(api_key="fake_api_key")

def test_load_schema_alternative_format():
    schema_json = '''
    {
        "title": "Test Schema",
        "properties": [
            {"name": "Name", "type": "title"},
            {"name": "Status", "type": "select", "options": ["To Do", "Done"]}
        ]
    }
    '''
    schema_data = json.loads(schema_json)
    properties = parse_schema(schema_data)
    schema_config = SchemaConfig(title=schema_data['title'], properties=properties)
    assert schema_config.title == "Test Schema"
    assert "Name" in schema_config.properties
    assert schema_config.properties["Name"].property_type == "title"

def test_invalid_schema_format():
    schema_json = '''
    {
        "title": "Invalid Schema",
        "properties": {
            "Name": {"unknown_type": {}}
        }
    }
    '''
    schema_data = json.loads(schema_json)
    with pytest.raises(ValueError) as exc_info:
        parse_schema(schema_data)
    assert "missing 'property_type'" in str(exc_info.value)

def test_entry_with_missing_property(notion_client, requests_mock):
    entry_data = {
        "Name": "Sample Entry",
        "Undefined Property": "Some Value"
    }
    schema_properties = {
        "Name": PropertyConfig(property_type="title"),
        # "Undefined Property" is not defined in the schema
    }
    with pytest.raises(ValueError):
        entry_properties = {}
        for name, value in entry_data.items():
            entry_properties[name] = EntryProperty.from_value(name, value, schema_properties)

def test_database_creation_failure(notion_client, requests_mock):
    schema = SchemaConfig(title="Test DB", properties={})
    requests_mock.post(
        'https://api.notion.com/v1/databases',
        json={"message": "Validation error"},
        status_code=400
    )
    with pytest.raises(Exception):
        notion_client.create_database(parent_id="fake_page_id", schema=schema)
