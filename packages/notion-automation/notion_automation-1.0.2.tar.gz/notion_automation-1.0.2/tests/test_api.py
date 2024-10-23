import pytest

from notion_automation.notion_client.api import NotionClient
from notion_automation.notion_client.models import SchemaConfig


@pytest.fixture
def notion_client():
    return NotionClient(api_key="fake_api_key")

def test_create_database(notion_client, requests_mock):
    schema = SchemaConfig(title="Test DB", properties={})
    requests_mock.post(
        'https://api.notion.com/v1/databases',
        json={"id": "fake_database_id"},
        status_code=200
    )
    database_id = notion_client.create_database(parent_id="fake_page_id", schema=schema)
    assert database_id == "fake_database_id"

def test_create_database_failure(notion_client, requests_mock):
    schema = SchemaConfig(title="Test DB", properties={})
    requests_mock.post(
        'https://api.notion.com/v1/databases',
        json={"error": "Unauthorized"},
        status_code=401
    )
    with pytest.raises(Exception):
        notion_client.create_database(parent_id="fake_page_id", schema=schema)
