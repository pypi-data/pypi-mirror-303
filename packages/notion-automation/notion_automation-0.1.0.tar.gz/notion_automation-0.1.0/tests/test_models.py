import pytest
from pydantic import ValidationError

from notion_client.models import EntryProperty, PropertyConfig, SchemaConfig


def test_schema_config():
    data = {
        "title": "Test Schema",
        "properties": {
            "Name": PropertyConfig(property_type="title"),
            "Description": PropertyConfig(property_type="rich_text")
        }
    }
    schema = SchemaConfig(**data)
    assert schema.title == "Test Schema"
    assert "Name" in schema.properties
    assert schema.properties["Name"].property_type == "title"

def test_invalid_property_config():
    data = {
        "property_type": "invalid_type"
    }
    with pytest.raises(ValidationError) as exc_info:
        prop = PropertyConfig(**data)
    error_message = str(exc_info.value)
    assert "Unsupported property type: invalid_type" in error_message

def test_property_config_validator():
    with pytest.raises(ValidationError) as exc_info:
        PropertyConfig(property_type="invalid_type")
    error_message = str(exc_info.value)
    assert "Unsupported property type: invalid_type" in error_message

def test_entry_property_validator():
    with pytest.raises(ValidationError) as exc_info:
        EntryProperty(type="unknown_type")
    error_message = str(exc_info.value)
    assert "Unsupported entry property type: unknown_type" in error_message

def test_entry_property_to_notion_format():
    entry_prop = EntryProperty(type="title", value="Sample Entry")
    notion_format = entry_prop.to_notion_format()
    expected_format = {
        "title": [{
            "type": "text",
            "text": {"content": "Sample Entry"}
        }]
    }
    assert notion_format == expected_format
