from notion_automation.notion_client.config import ConfigManager
from notion_automation.notion_client.models import SchemaConfig


def test_load_schema(tmp_path):
    schema_content = '{"title": "Test Schema", "properties": {}}'
    schema_file = tmp_path / "test_schema.json"
    schema_file.write_text(schema_content)

    config_manager = ConfigManager(config_path=str(tmp_path))
    schema = config_manager.load_schema("test_schema")
    assert isinstance(schema, SchemaConfig)
    assert schema.title == "Test Schema"
